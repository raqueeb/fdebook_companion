"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 4 - ফিল্ড প্লেবুক ও রিয়েল ওয়ার্ল্ড কেস
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-4/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
ট্র্যাক এ (ISP কেস স্টাডি): ঢাকার আইএসপি ফাইবার কাট হ্যান্ডলিংয়ের জন্য অ্যাসিনক্রোনাস
টিকিট কোরিলেশন ও রাউটিং ওয়ার্কার। দুই লেভেলের ওএলটি অ্যালার্ম পড়ে:
  - পন পোর্ট লেভেল LOS  -> মেইন ফাইবার কাটা, মাস্টার আউটেজ টিকিট, জোন প্রতি একটা ফিল্ড অ্যালার্ট
  - ওএনইউ লেভেল DGi     -> ডাইং গ্যাস্প, বাসায় পাওয়ার নেই, শুধু এসএমএস
  - ওএনইউ লেভেল LOSi    -> ওএনইউ চালু কিন্তু আলো নেই, ড্রপ ক্যাবল, ফিল্ড টেকনিশিয়ান
  - ওএনইউ ONLINE        -> রাউটার বা বিলিং, লোকাল এলএলএম ট্রায়াজ কিউ
"""

import asyncio

ZONE_STATUS = {
    "DHK-DHN-07": {"status": "LOS", "eta_min": 45},   # পন পোর্ট লেভেল: এনএমএস থেকে আসা ক্যাশ
    "DHK-MIR-02": {"status": "NORMAL", "eta_min": 0}
}
ONU_STATUS = {"CUST-5521": "DGi", "CUST-7310": "LOSi", "CUST-8804": "ONLINE"}  # ওএনইউ লেভেল: শেষ অ্যালার্ম
ALERTED_ZONES = set()  # যেসব জোনের অ্যালার্ট ফিল্ড টিমের কাছে চলে গেছে

async def route_ticket(t: dict) -> dict:
    zone = ZONE_STATUS.get(t["zone"], {"status": "NORMAL"})
    await asyncio.sleep(0.05)  # এসএমএস গেটওয়ে বা কিউয়ে লেখার নন-ব্লকিং কলের সিমুলেশন
    if zone["status"] == "LOS":  # পুরো পন পোর্ট অফলাইন: মেইন ফাইবার কাট
        first = t["zone"] not in ALERTED_ZONES  # চেক আর অ্যাডের মাঝে কোনো await নেই
        ALERTED_ZONES.add(t["zone"])
        return {"id": t["id"], "action": "GROUP_UNDER_MASTER_OUTAGE",
                "dispatch": "FIELD_FIBER_TEAM" if first else "ALREADY_DISPATCHED"}
    # জোন রিকভার করলে ALERTED_ZONES খালি করবে এনএমএসের Clear অ্যালার্ম শোনা আলাদা টাস্ক, এই ফাংশন নয়
    onu = ONU_STATUS.get(t["cust"], "ONLINE")
    if onu == "DGi":   # ডাইং গ্যাস্প: বাসায় কারেন্ট নেই বা ইউজার নিজে ওএনইউ অফ করেছেন
        return {"id": t["id"], "action": "SMS_CHECK_POWER", "dispatch": "NO_TECH_NEEDED"}
    if onu == "LOSi":  # ওএনইউ অন, কিন্তু সিগন্যাল আসছে না: বাসার ড্রপ ক্যাবল বা কানেক্টর
        return {"id": t["id"], "action": "DROP_CABLE_FAULT", "dispatch": "FIELD_TECHNICIAN"}
    return {"id": t["id"], "action": "QUEUE_FOR_LLM_TRIAGE", "dispatch": "SQLITE_QUEUE"}  # ওএনইউ অনলাইন: রাউটার বা বিলিং

async def main():
    burst = [
        {"id": 101, "zone": "DHK-DHN-07", "cust": "CUST-1001"},
        {"id": 102, "zone": "DHK-MIR-02", "cust": "CUST-5521"},
        {"id": 103, "zone": "DHK-DHN-07", "cust": "CUST-1002"},
        {"id": 104, "zone": "DHK-MIR-02", "cust": "CUST-7310"},
        {"id": 105, "zone": "DHK-MIR-02", "cust": "CUST-8804"},
    ]
    for r in await asyncio.gather(*(route_ticket(t) for t in burst)):
        print(f"Ticket #{r['id']}: {r['action']} -> {r['dispatch']}")

if __name__ == "__main__":
    asyncio.run(main())
