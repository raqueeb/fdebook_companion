"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 4 - ফিল্ড প্লেবুক ও রিয়েল ওয়ার্ল্ড কেস
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-4/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
ট্র্যাক এ (ISP কেস স্টাডি): ঢাকার আইএসপি ফাইবার কাট (OLT LOS Outage) হ্যান্ডলিংয়ের জন্য
অ্যাসিনক্রোনাস টিকেট কোরিলেশন ও স্মার্ট এসএমএস রাউটিং ওয়ার্কার।
"""

import asyncio

ZONE_STATUS = {
    "DHK-DHN-07": {"status": "LOS", "eta_min": 45},   # এনএমএস থেকে আসা ক্যাশ
    "DHK-MIR-02": {"status": "NORMAL", "eta_min": 0}
}
ALERTED_ZONES = set()  # যেসব জোনের অ্যালার্ট ফিল্ড টিমের কাছে চলে গেছে

async def route_ticket(t: dict) -> dict:
    info = ZONE_STATUS.get(t["zone"], {"status": "NORMAL"})
    await asyncio.sleep(0.05)  # এসএমএস গেটওয়ে বা কিউয়ে লেখার নন-ব্লকিং কলের সিমুলেশন
    if info["status"] != "LOS":
        ALERTED_ZONES.discard(t["zone"])  # জোন সেরে উঠলে পরের ফাইবার কাটায় আবার অ্যালার্ট যাবে
        return {"id": t["id"], "action": "QUEUE_FOR_LLM_TRIAGE", "dispatch": "SQLITE_QUEUE"}
    first = t["zone"] not in ALERTED_ZONES  # চেক আর অ্যাডের মাঝে কোনো await নেই
    ALERTED_ZONES.add(t["zone"])
    eta = info.get("eta_min")
    sms = f"ফাইবার মেরামতের কাজ চলছে। আনুমানিক {eta} মিনিট।" if eta else "ফাইবার মেরামতের কাজ চলছে। সংযোগ দ্রুত স্বাভাবিক হবে।"
    return {
        "id": t["id"],
        "action": "GROUP_UNDER_MASTER_OUTAGE",
        "sms": sms,
        "dispatch": "FIELD_FIBER_TEAM" if first else "ALREADY_DISPATCHED"
    }

async def main():
    burst = [
        {"id": 101, "zone": "DHK-DHN-07"},
        {"id": 102, "zone": "DHK-MIR-02"},
        {"id": 103, "zone": "DHK-DHN-07"}
    ]
    for r in await asyncio.gather(*(route_ticket(t) for t in burst)):
        print(f"Ticket #{r['id']}: {r['action']} -> {r['dispatch']}")

if __name__ == "__main__":
    asyncio.run(main())
