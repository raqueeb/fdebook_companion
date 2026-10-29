"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 4 - ফিল্ড প্লেবুক ও রিয়েল ওয়ার্ল্ড কেস
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-4/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
ফিল্ড পলিটিক্স ও স্টেকহোল্ডার অ্যালাইনমেন্ট: মিড-লেভেল ম্যানেজারের জন্য ১-ক্লিক
এক্সিকিউটিভ সামারি ও ডেমারেজ সেভিংস রিপোর্ট জেনারেটর (Manager Hero Report)।
"""

import sys
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def build_manager_hero_report(manager_name: str, logs: list) -> str:
    total = len(logs)
    auto_cleared = sum(1 for x in logs if x["status"] == "APPROVED")
    flagged = total - auto_cleared
    saved_usd = auto_cleared * 150  # প্রতি কন্টেইনারে গড় ১৫০ ডলার ডেমারেজ সাশ্রয়

    return (
        f"বিষয়: দৈনিক পোর্ট অপারেশন সামারি | তত্ত্বাবধানে: {manager_name}\n"
        f"- মোট কন্টেইনার প্রসেসড: {total} টি (অটো-গেটপাস: {auto_cleared} টি)\n"
        f"- কাস্টমস অডিটের জন্য ফ্ল্যাগড: {flagged} টি\n"
        f"- আনুমানিক ডেমারেজ সাশ্রয়: ${saved_usd:,} USD"
    )

if __name__ == "__main__":
    daily_logs = [{"status": "APPROVED"}, {"status": "APPROVED"}, {"status": "FLAGGED"}]
    print(build_manager_hero_report("কামরুল হাসান, ডেপুটি ম্যানেজার (পোর্ট অপারেশনস)", daily_logs))
