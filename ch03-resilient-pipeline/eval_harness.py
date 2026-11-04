"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 3 - দ্য নিউ এসডিএলসি ও পাইপলাইন
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-3/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
বিল্ডের আগেই গোল্ডেন ডেটাসেট ইভ্যালুয়েশন হারনেস (Evaluation Harness Testbench) -
এলএলএম বা রুল-বেইজড ট্রায়াজ ইঞ্জিনের স্কিমা ও অ্যাকুরেসি ভ্যালিডেশন।

চালালে চ্যাপ্টার ২-এর mock_tickets.json (৩০টা বাংলা ও বাংলিশ মেসেজ) পড়ে:
  - লোকালহোস্টে Ollama চালু থাকলে চ্যাপ্টার ২-এর আসল triage_customer_ticket() দিয়ে মাপে,
  - না থাকলে একটা সাধারণ কিওয়ার্ড-ভিত্তিক মক ফাংশন দিয়ে মাপে এবং স্ক্রিনে সেটা পরিষ্কার জানায়।
"""

import json
import sys
import urllib.request
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VALID_CATEGORIES = {"DELIVERY", "BILLING", "STOCK"}
VALID_PRIORITIES = {"HIGH", "MEDIUM", "LOW"}

def evaluate_triage_model(golden_dataset: list, triage_fn) -> dict:
    valid_schema_count = 0
    correct_category_count = 0
    total = len(golden_dataset)

    for sample in golden_dataset:
        try:
            result = triage_fn(sample["text"])
            # ১. স্কিমা ভ্যালিডিটি পরীক্ষা: category আর priority দুটো কি-ই কি সঠিক ফরম্যাটে আছে?
            if (isinstance(result, dict)
                    and result.get("category") in VALID_CATEGORIES
                    and result.get("priority") in VALID_PRIORITIES):
                valid_schema_count += 1
                # ২. অ্যাকুরেসি পরীক্ষা: আসল গ্রাউন্ড ট্রুথের সাথে কি মিলেছে?
                if result["category"] == sample["expected_category"]:
                    correct_category_count += 1
        except Exception:
            continue

    return {
        "schema_pass_rate": round((valid_schema_count / total) * 100, 1),
        "accuracy_score": round((correct_category_count / total) * 100, 1)
    }

# ---------- নিচের অংশটুকু গ্লু কোড: গোল্ডেন সেট লোড করা আর কোন ট্রায়াজ ফাংশন চলবে তা ঠিক করা ----------

GOLDEN_SET_PATH = Path(__file__).resolve().parent.parent / "ch02-local-triage-engine" / "mock_tickets.json"

def ollama_is_up(url: str = "http://localhost:11434/api/tags") -> bool:
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return r.status == 200
    except Exception:
        return False

def mock_triage_fn(text: str) -> dict:
    """Ollama না থাকলে হারনেস দেখানোর জন্য কিওয়ার্ড-ভিত্তিক মক। আসল মডেলের বিকল্প নয়।"""
    low = text.lower()
    if any(k in low for k in ("স্টক", "গোডাউন", "গুদাম", "ইনভেন্টরি", "stock")):
        return {"category": "STOCK", "priority": "MEDIUM"}
    if any(k in low for k in ("বিল", "ইনভয়েস", "ভ্যাট", "রিবেট", "পেমেন্ট", "স্টেটমেন্ট", "প্রাইস", "ক্রেডিট",
                              "bill", "invoice", "vat", "rebate", "credit")):
        return {"category": "BILLING", "priority": "HIGH"}
    return {"category": "DELIVERY", "priority": "HIGH"}

if __name__ == "__main__":
    golden_set = json.loads(GOLDEN_SET_PATH.read_text(encoding="utf-8"))
    print(f"Golden set: {len(golden_set)} tickets from {GOLDEN_SET_PATH.name}")

    if ollama_is_up():
        sys.path.insert(0, str(GOLDEN_SET_PATH.parent))
        from triage import triage_customer_ticket  # চ্যাপ্টার ২-এর আসল লোকাল এলএলএম ট্রায়াজ
        print("Ollama chalu ache: qwen2.5:1.5b diye asol eval cholche (ektu somoy lagbe)...")
        score = evaluate_triage_model(golden_set, triage_customer_ticket)
    else:
        print("[MOCK MODE] Ollama paoa jay ni; keyword-based mock_triage_fn diye harness dekhano hocche.")
        print("            Asol score pete: ollama pull qwen2.5:1.5b, tarpor abar chalan.")
        score = evaluate_triage_model(golden_set, mock_triage_fn)

    print("Eval Harness Score:", score)
    verdict = "DEPLOY OK" if score["schema_pass_rate"] == 100.0 and score["accuracy_score"] >= 90.0 else "DO NOT DEPLOY"
    print(f"Gate (schema 100% & accuracy >= 90%): {verdict}")
