# FDE Intro Diagnostic: Silent Abandonment & Shadow-IT Detector
from datetime import date

def audit_system_adoption(total_staff: int, active_users_30d: int, last_tx_date: str) -> dict:
    adoption_rate = round((active_users_30d / total_staff) * 100, 1)
    days_stagnant = (date(2026, 10, 29) - date.fromisoformat(last_tx_date)).days

    # অ্যাক্টিভ ইউজার ২০%-এর কম বা ৭ দিন নতুন এন্ট্রি বন্ধ থাকলেই রেড অ্যালার্ট
    is_abandoned = adoption_rate < 20.0 or days_stagnant > 7
    return {
        "adoption_pct": adoption_rate,
        "stagnant_days": days_stagnant,
        "status": "SILENT_CHURN_ALERT" if is_abandoned else "HEALTHY_ADOPTION"
    }

if __name__ == "__main__":
    # নব্বই দিন পর সার্ভার রুমে পাওয়া আসল ডেটাবেজ লগ
    print(audit_system_adoption(total_staff=59, active_users_30d=4, last_tx_date="2026-09-12"))
