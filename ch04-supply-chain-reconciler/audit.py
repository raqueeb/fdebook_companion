"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 4 - ফিল্ড প্লেবুক ও রিয়েল ওয়ার্ল্ড কেস
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-4/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
ট্র্যাক বি (সাপ্লাই চেইনের কেস স্টাডি): চট্টগ্রাম বন্দরের বিল অব এন্ট্রি,
ইনভয়েস এবং ওয়েব্রিজ স্কেল ওজনের থ্রি-ওয়ে রিকনসিলেশন ও ১% টলারেন্স অডিট ইঞ্জিন।
"""

def reconcile_shipment(customs: dict, invoice: dict, weighbridge: dict) -> dict:
    declared_kg = customs["gross_kg"]                          # বিল অব এন্ট্রির ঘোষিত ওজন
    invoiced_kg = invoice["net_kg"] + invoice["packing_kg"]    # ইনভয়েসের নিট + প্যাকিং ওজন
    weighed_kg = weighbridge["scale_kg"]                       # ওয়েব্রিজ স্কেলের আসল ওজন
    tolerance_kg = declared_kg * 0.01                          # ১% বাস্তব টলারেন্স সীমা

    weight_within_limit = (abs(weighed_kg - declared_kg) <= tolerance_kg and
                           abs(invoiced_kg - declared_kg) <= tolerance_kg)
    hs_code_matched = customs["hs_code"] == invoice["hs_code"]
    variance_kg = abs(weighed_kg - declared_kg)

    if weight_within_limit and hs_code_matched:
        return {"status": "APPROVED", "action": "AUTO_GATE_PASS", "variance_kg": variance_kg}
    return {"status": "FLAGGED", "action": "MANUAL_CUSTOMS_AUDIT", "variance_kg": variance_kg}

if __name__ == "__main__":
    # চট্টগ্রাম বন্দরের আসল চালানের নমুনা ডেটা
    customs_doc = {"gross_kg": 50000, "hs_code": "8471.30"}
    invoice_doc = {"net_kg": 49500, "packing_kg": 500, "hs_code": "8471.30"}
    scale_slip = {"scale_kg": 50150}
    print(reconcile_shipment(customs_doc, invoice_doc, scale_slip))
