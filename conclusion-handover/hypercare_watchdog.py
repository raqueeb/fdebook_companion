"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Conclusion - হ্যান্ডওভার, সাসটেইনেবিলিটি ও এক্সিট
Book Reference URL: https://aiwithr.github.io/fde_book/conclusion/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
হ্যান্ডওভার-পরবর্তী হাইপার-কেয়ার (Hyper-Care) পর্বের প্রোঅ্যাকটিভ মেমোরি স্পাইক
ও লেটেন্সি ডিটেকশন ওয়াচডগ (অটো-বাফার ফ্ল্যাশ ও প্রোঅ্যাকটিভ নোটিফিকেশন)।
"""

import sys
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def monitor_hypercare_worker(worker_name: str, ram_mb: int, latency_sec: float) -> dict:
    RAM_LIMIT_MB, LATENCY_LIMIT_SEC = 1500, 2.5

    # স্টাফদের চোখে পড়ার আগেই মেমোরি বা লেটেন্সি স্পাইক ধরা
    if ram_mb > RAM_LIMIT_MB or latency_sec > LATENCY_LIMIT_SEC:
        return {
            "worker": worker_name,
            "action": "AUTO_FLUSH_BUFFER_AND_RESTART",
            "proactive_msg": f"{worker_name}-এ সামান্য মেমোরি স্পাইক ({ram_mb}MB) হয়েছিল। "
                             f"বাফার বাড়িয়ে রিস্টার্ট দেওয়া হয়েছে, কাজে কোনো ব্যাঘাত ঘটেনি।"
        }
    return {"worker": worker_name, "action": "NONE", "proactive_msg": "STABLE"}

if __name__ == "__main__":
    # দুপুর ১২টায় বড় পিডিএফ স্ক্যানের সময় ১৭৫০ মেগাবাইট মেমোরি স্পাইক ডিটেকশন
    print(monitor_hypercare_worker("invoice-parser", ram_mb=1750, latency_sec=3.1))
