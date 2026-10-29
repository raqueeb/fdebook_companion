# FDE Hyper-Care Tool: Proactive Memory Spike & Latency Watchdog
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
