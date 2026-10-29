"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Conclusion - হ্যান্ডওভার, সাসটেইনেবিলিটি ও এক্সিট
Book Reference URL: https://aiwithr.github.io/fde_book/conclusion/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
হ্যান্ডওভারের পর লোকাল আইটি টিমের জন্য অটোমেটেড অন-প্রেম সার্ভার হেলথ চেক ক্রন স্ক্রিপ্ট
(ডিস্ক স্পেস, পাইথন অ্যাপ সার্ভিস এবং লোকাল Ollama এআই স্ট্যাটাস ডায়াগনস্টিক)।
"""

import shutil
import urllib.request
import time
import sys
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def endpoint_alive(url: str) -> bool:
    try:
        return urllib.request.urlopen(url, timeout=3).status == 200
    except Exception:
        return False

def run_health_diagnostics() -> list:
    alerts = []
    disk = shutil.disk_usage("/")
    if (disk.used / disk.total) > 0.85:
        alerts.append("WARNING: সার্ভারের ডিস্ক ৮৫% এর বেশি ভরে গেছে")
    if not endpoint_alive("http://localhost:8000/healthz"):
        alerts.append("CRITICAL: মূল পাইথন অ্যাপ সাড়া দিচ্ছে না")
    if not endpoint_alive("http://localhost:11434/api/tags"):
        alerts.append("CRITICAL: লোকাল এআই মডেল (Ollama) বন্ধ হয়ে আছে")
    return alerts

if __name__ == "__main__":
    issues = run_health_diagnostics()
    status_msg = "OK: সব সিস্টেম সচল" if not issues else " | ".join(issues)
    print(f"{time.strftime('%Y-%m-%d %H:%M')} - {status_msg}")
