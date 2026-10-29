# FDE Stakeholder Aligner: 1-Click Executive Summary for Mid-Level Manager
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
