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

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SAVED_PER_CONTAINER_USD = 150  # ধরে নেয়া মান: ক্লায়েন্টের আসল ডেমারেজ ট্যারিফ থেকে বসাবেন

def build_manager_hero_report(manager_name: str, logs: list) -> str:
    total = len(logs)
    cleared = sum(1 for x in logs if x["status"] == "READY_FOR_GATE_PASS")
    flagged = total - cleared
    saved_usd = cleared * SAVED_PER_CONTAINER_USD

    return (
        f"বিষয়: দৈনিক পোর্ট অপারেশন সামারি | তত্ত্বাবধানে: {manager_name}\n"
        f"- মোট কন্টেইনার প্রসেসড: {total} টি (গেট পাসের জন্য তৈরি: {cleared} টি)\n"
        f"- কাস্টমস অডিটের জন্য ফ্ল্যাগড: {flagged} টি\n"
        f"- আনুমানিক ডেমারেজ সাশ্রয়: ${saved_usd:,}"
    )

if __name__ == "__main__":
    daily_logs = [
        {"status": "READY_FOR_GATE_PASS"},
        {"status": "READY_FOR_GATE_PASS"},
        {"status": "FLAGGED"}
    ]
    print(build_manager_hero_report("কামরুল হাসান, ডেপুটি ম্যানেজার (পোর্ট অপারেশনস)", daily_logs))
