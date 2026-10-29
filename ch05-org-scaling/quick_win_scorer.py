# FDE Field Tool: First-Week Quick-Win Prioritization Scorer
discovered_tasks = [
    {"name": "ম্যানেজারের ফিজিক্যাল সইয়ের অপেক্ষা", "daily_freq": 20, "mins_each": 6, "rules_clear": True},
    {"name": "সন্ধ্যার এক্সেল সামারি রিপোর্ট তৈরি", "daily_freq": 1, "mins_each": 90, "rules_clear": True},
    {"name": "কাগুজে চালান ও গেট পাসের জটিল মিলানো", "daily_freq": 15, "mins_each": 8, "rules_clear": False},
    {"name": "ভ্যাট ও রিবেটের ম্যানুয়াল ক্যালকুলেশন", "daily_freq": 2, "mins_each": 30, "rules_clear": True},
]

def calculate_quick_win_score(task: dict) -> float:
    daily_wasted_mins = task["daily_freq"] * task["mins_each"]
    # বিজনেস রুল অস্পষ্ট হলে প্রথম সপ্তাহে ঝুঁকি বেশি, তাই স্কোর ৭০% কমিয়ে দেওয়া হয়
    risk_multiplier = 1.0 if task["rules_clear"] else 0.3
    return round(daily_wasted_mins * risk_multiplier, 1)

if __name__ == "__main__":
    ranked_tasks = sorted(discovered_tasks, key=calculate_quick_win_score, reverse=True)
    for t in ranked_tasks:
        print(f"Score: {calculate_quick_win_score(t):5.1f} | Task: {t['name']}")
