"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Conclusion - পারফেক্ট হ্যান্ডওভার ও ফিউচার প্রুফিং
Book Reference URL: https://aiwithr.github.io/fde_book/conclusion/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
হ্যান্ডওভার-পরবর্তী হাইপার-কেয়ার (Hyper-Care) পর্বের প্রোঅ্যাকটিভ মেমোরি স্পাইক
ও লেটেন্সি ডিটেকশন ওয়াচডগ (২-স্ট্রাইক নিয়ম, রিস্টার্ট সিদ্ধান্ত ও প্রোঅ্যাকটিভ নোটিফিকেশন)।
"""

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAM_LIMIT_MB, LATENCY_LIMIT_SEC, STRIKES_TO_ACT = 1500, 2.5, 2  # উদাহরণ: বেসলাইন মেপে বদলাবেন

def monitor_hypercare_worker(name: str, ram_mb: int, latency_sec: float, strikes: int) -> dict:
    if ram_mb <= RAM_LIMIT_MB and latency_sec <= LATENCY_LIMIT_SEC:
        return {"worker": name, "action": "NONE", "strikes": 0}
    if strikes + 1 < STRIKES_TO_ACT:  # একবারের স্পাইকে রিস্টার্ট নয়, আগে নজর রাখা
        return {"worker": name, "action": "WATCH", "strikes": strikes + 1}
    return {
        "worker": name, "action": "RESTART_WORKER", "strikes": 0,
        "restart_cmd": f"sudo systemctl restart {name}",  # প্রোডাকশনে subprocess.run দিয়ে চালাবেন
        "proactive_msg": f"{name}-এর মেমোরি {ram_mb} এমবিতে উঠেছিল, আমি ওয়ার্কারটা রিস্টার্ট দিয়েছি। "
                         f"জমে থাকা টিকিট কিউতে নিরাপদ ছিল, রিস্টার্টের পর আবার চলছে।",
    }

if __name__ == "__main__":
    # দুপুর ১২টায় বড় পিডিএফ স্ক্যানের সময় পরপর দুবার সীমা পার
    print(monitor_hypercare_worker("invoice-parser", ram_mb=1750, latency_sec=3.1, strikes=0))
    print(monitor_hypercare_worker("invoice-parser", ram_mb=1780, latency_sec=3.4, strikes=1))
