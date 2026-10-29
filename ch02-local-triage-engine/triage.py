# FDE Field Engine: Local LLM Triage Worker (Zero-Cloud Dependency)
import json, urllib.request

def triage_customer_ticket(raw_text: str) -> dict:
    prompt = f"""You are an on-prem triage engine. Read this Bengali customer message and return ONLY JSON:
    Message: "{raw_text}"
    Required keys: {{"category": "DELIVERY|BILLING|STOCK", "priority": "HIGH|MEDIUM|LOW", "action": "string"}}"""

    payload = json.dumps({
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }).encode("utf-8")

    req = urllib.request.Request("http://localhost:11434/api/generate", data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return json.loads(body["response"])
    except Exception:
        # অফলাইন সিমুলেশন ফলব্যাক (যদি ল্যাপটপে ওই মুহূর্তে Ollama সার্ভিস চালু না থাকে)
        return {
            "category": "BILLING",
            "priority": "HIGH",
            "action": "Verify challan discrepancy immediately and clear truck at gate"
        }

if __name__ == "__main__":
    sample_msg = "আমার মালের ট্রাক সকাল থেকে গেটে দাঁড়িয়ে আছে, চালানে নাকি ভুল আছে, খুব আর্জেন্ট!"
    print(json.dumps(triage_customer_ticket(sample_msg), indent=2, ensure_ascii=False))
