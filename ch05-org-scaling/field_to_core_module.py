"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 5 - অর্গানাইজেশন স্কেলিং ও প্যাটার্ন
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-5/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
প্যালান্টির প্যাটার্ন (Palantir Pattern): কোর কোডে হাত না দিয়ে ক্লায়েন্ট কনফিগারেশন
ডিকাপল করার ফিল্ড-টু-কোর ইঞ্জিনিয়ারিং আর্কিটেকচার (Field-to-Core Engine)।
"""

from decimal import Decimal

def core_reconcile(customs: dict, invoice: dict, slip: dict, cfg: dict) -> dict:
    declared = Decimal(customs["gross_kg"])
    limit = declared * Decimal(cfg["tolerance_pct"]) / 100    # ছাড়ের সীমা আসছে কনফিগ থেকে
    weighed = Decimal(slip["scale_kg"] - slip["tare_kg"])      # ট্রাক আর কন্টেইনারের ট্যার বাদ
    invoiced = Decimal(invoice["net_kg"] + invoice["packing_kg"])
    hs_ok = customs["hs_code"].replace(".", "")[:6] == invoice["hs_code"].replace(".", "")[:6]
    ok = abs(weighed - declared) <= limit and abs(invoiced - declared) <= limit and hs_ok
    return {"client": cfg["name"], "status": "READY_FOR_GATE_PASS" if ok else "FLAGGED"}

if __name__ == "__main__":
    # কোর কোডে হাত না দিয়ে শুধু কনফিগ বদলেই তিনটা ক্লায়েন্টে ডেপ্লয়
    CLIENT_CONFIGS = [
        {"name": "ctg_port_cnf", "tolerance_pct": "1"},
        {"name": "ngj_cement", "tolerance_pct": "0.5"},
        {"name": "gzp_garments", "tolerance_pct": "2"},
    ]
    customs_doc = {"gross_kg": 25000, "hs_code": "8471.30"}
    invoice_doc = {"net_kg": 24750, "packing_kg": 250, "hs_code": "8471.30"}
    slip_doc = {"scale_kg": 40200, "tare_kg": 15000}
    for cfg in CLIENT_CONFIGS:
        print(core_reconcile(customs_doc, invoice_doc, slip_doc, cfg))
