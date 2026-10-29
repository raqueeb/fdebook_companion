# FDE Field Eval: Evaluation Harness Before Build
def evaluate_triage_model(golden_dataset: list, triage_fn) -> dict:
    valid_schema_count = 0
    correct_category_count = 0
    total = len(golden_dataset)

    for sample in golden_dataset:
        try:
            result = triage_fn(sample["text"])
            # ১. স্কিমা ভ্যালিডিটি পরীক্ষা: আউটপুট কি সঠিক ফরম্যাটে আছে?
            if isinstance(result, dict) and result.get("category") in {"DELIVERY", "BILLING", "STOCK"}:
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

if __name__ == "__main__":
    golden_set = [
        {"text": "চালানে ভ্যাটের হিসাব ভুল এসেছে", "expected_category": "BILLING"},
        {"text": "গুদামে স্টক মিলছে না", "expected_category": "STOCK"},
        {"text": "ট্রাক এখনো পৌঁছায়নি", "expected_category": "DELIVERY"}
    ]
    def mock_triage_fn(text: str) -> dict:
        if "চালান" in text or "ভ্যাট" in text:
            return {"category": "BILLING", "priority": "HIGH"}
        if "স্টক" in text:
            return {"category": "STOCK", "priority": "MEDIUM"}
        return {"category": "DELIVERY", "priority": "HIGH"}

    print("Eval Harness Score:", evaluate_triage_model(golden_set, mock_triage_fn))
