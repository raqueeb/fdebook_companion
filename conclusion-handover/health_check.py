"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Conclusion - পারফেক্ট হ্যান্ডওভার ও ফিউচার প্রুফিং
Book Reference URL: https://aiwithr.github.io/fde_book/conclusion/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
হ্যান্ডওভারের পর লোকাল আইটি টিমের জন্য অটোমেটেড অন-প্রেম সার্ভার হেলথ চেক ক্রন স্ক্রিপ্ট
(ডিস্ক স্পেস, মূল পাইথন অ্যাপের /healthz এবং Ollama-তে qwen2.5:1.5b মডেলের উপস্থিতি পরীক্ষা)।
"""

import json
import shutil
import sys
import time
import urllib.request

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def fetch(url: str):
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            return r.status, r.read()
    except Exception:
        return None, b""

def diagnose() -> list:
    alerts, disk = [], shutil.disk_usage("/")  # ডেটা অন্য পার্টিশনে থাকলে সেই পাথ দিন
    if disk.used / disk.total > 0.85:
        alerts.append("WARNING: সার্ভারের ডিস্ক ৮৫%-এর বেশি ভরে গেছে")
    if fetch("http://localhost:8000/healthz")[0] != 200:
        alerts.append("CRITICAL: মূল পাইথন অ্যাপ রেসপন্ড করছে না")
    code, body = fetch("http://localhost:11434/api/tags")
    if code != 200:
        alerts.append("CRITICAL: লোকাল এআই (Ollama) বন্ধ হয়ে আছে")
    elif "qwen2.5:1.5b" not in [m["name"] for m in json.loads(body)["models"]]:
        alerts.append("CRITICAL: Ollama চালু আছে, কিন্তু qwen2.5:1.5b মডেল নেই")
    return alerts

if __name__ == "__main__":
    issues = diagnose()  # issues থাকলে এখানে এসএমএস গেটওয়ে বা হোয়াটসঅ্যাপ ওয়েবহুক জুড়ুন
    print(f"{time.strftime('%Y-%m-%d %H:%M')} - " + (" | ".join(issues) or "OK: সব সিস্টেম সচল"))
