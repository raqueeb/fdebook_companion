"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 4 - ফিল্ড প্লেবুক ও রিয়েল ওয়ার্ল্ড কেস
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-4/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
ট্র্যাক বি (সাপ্লাই চেইনের কেস স্টাডি): চট্টগ্রাম বন্দরের বিল অব এন্ট্রি,
ইনভয়েস এবং ওয়েব্রিজ স্লিপ ওজনের থ্রি-ওয়ে রিকনসিলিয়েশন ও ১% টলারেন্স অডিট ইঞ্জিন।
"""

TOLERANCE_PCT = 1  # হেড ক্লার্কের মুখে শোনা নিয়ম, ক্লায়েন্ট ভেদে বদলাবে

def hs6(code: str) -> str:
    return code.replace(".", "")[:6]  # আন্তর্জাতিক এইচএস কোডের প্রথম ছয় ডিজিট

def reconcile(customs: dict, invoice: dict, slip: dict) -> dict:
    declared = customs["gross_kg"]                       # বিল অব এন্ট্রির ঘোষিত ওজন
    invoiced = invoice["net_kg"] + invoice["packing_kg"]  # নিট + প্যাকিং ওজন
    weighed = slip["scale_kg"] - slip["tare_kg"]          # ট্রাক আর খালি কন্টেইনারের ওজন বাদ

    def within(kg):  # পূর্ণসংখ্যার হিসাব, তাই ফ্লোটিং পয়েন্টের গোলমাল নেই
        return abs(kg - declared) * 100 <= declared * TOLERANCE_PCT

    hs_ok = hs6(customs["hs_code"]) == hs6(invoice["hs_code"])
    ok = within(weighed) and within(invoiced) and hs_ok
    return {
        "status": "READY_FOR_GATE_PASS" if ok else "FLAGGED",
        "variance_kg": weighed - declared,
        "hs_match": hs_ok
    }

if __name__ == "__main__":
    customs_doc = {"gross_kg": 25000, "hs_code": "8471.30"}
    invoice_doc = {"net_kg": 24750, "packing_kg": 250, "hs_code": "8471.30"}
    print(reconcile(customs_doc, invoice_doc, {"scale_kg": 40075, "tare_kg": 15000}))
    print(reconcile(customs_doc, invoice_doc, {"scale_kg": 40400, "tare_kg": 15000}))
