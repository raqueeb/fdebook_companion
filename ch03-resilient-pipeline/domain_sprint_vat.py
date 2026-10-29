"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 3 - দ্য নিউ এসডিএলসি ও পাইপলাইন
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-3/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
২০ মিনিটের ডোমেইন স্প্রিন্ট: ফিল্ড একাউন্টেন্টের লাল খাতার নিয়ম অনুযায়ী
ভ্যাট (VAT) ও ট্রান্সপোর্ট রিবেট গার্ডরেইল ক্যালকুলেটর ইঞ্জিন।
"""

def calculate_net_vat(commercial_amount: float, transport_cost: float = 0.0) -> float:
    # ১. ইনপুট গার্ডরেইল: চালানের অঙ্ক কখনোই ঋণাত্মক হতে পারবে না
    if commercial_amount < 0 or transport_cost < 0:
        raise ValueError("GUARDRAIL_ERROR: Amount cannot be negative")

    gross_vat = commercial_amount * 0.15       # কমার্শিয়াল মালের ওপর ১৫% ভ্যাট
    transport_rebate = transport_cost * 0.05   # নিজস্ব ট্রান্সপোর্টে ৫% রিবেট ছাড়
    return round(max(0.0, gross_vat - transport_rebate), 2)

if __name__ == "__main__":
    # ২. টেস্ট-ফার্স্ট গার্ডরেইল: লাল খাতার আসল চালানের হিসাব দিয়ে অটো-ভেরিফিকেশন
    assert calculate_net_vat(100000, 20000) == 14000.0, "Rebate calculation failed!"
    assert calculate_net_vat(50000, 0) == 7500.0, "Standard VAT calculation failed!"
    print("Domain Sprint Verified! Net Payable VAT:", calculate_net_vat(100000, 20000))
