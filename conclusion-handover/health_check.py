# FDE Field Tool: Automated On-Prem Health Check (Run every 5 mins via cron)
import shutil, urllib.request, time

def endpoint_alive(url: str) -> bool:
    try:
        return urllib.request.urlopen(url, timeout=3).status == 200
    except Exception:
        return False

def run_health_diagnostics() -> list:
    alerts = []
    disk = shutil.disk_usage("/")
    if (disk.used / disk.total) > 0.85:
        alerts.append("WARNING: সার্ভারের ডিস্ক ৮৫% এর বেশি ভরে গেছে")
    if not endpoint_alive("http://localhost:8000/healthz"):
        alerts.append("CRITICAL: মূল পাইথন অ্যাপ সাড়া দিচ্ছে না")
    if not endpoint_alive("http://localhost:11434/api/tags"):
        alerts.append("CRITICAL: লোকাল এআই মডেল (Ollama) বন্ধ হয়ে আছে")
    return alerts

if __name__ == "__main__":
    issues = run_health_diagnostics()
    status_msg = "OK: সব সিস্টেম সচল" if not issues else " | ".join(issues)
    print(f"{time.strftime('%Y-%m-%d %H:%M')} - {status_msg}")
