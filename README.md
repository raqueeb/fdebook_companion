# ফরওয়ার্ড ডেপ্লয়েড ইঞ্জিনিয়ারিং (FDE) - ফিল্ড ম্যানুয়াল (কমপ্যানিয়ন কোডবেস)

> **বইয়ের লাইভ সাইট:** [https://aiwithr.github.io/fde_book/](https://aiwithr.github.io/fde_book/)  
> **লেখক:** রকিবুল হাসান (Rakibul Hassan)  
> **কমপ্যানিয়ন রিপোজিটরি:** [https://github.com/raqueeb/fdebook_companion](https://github.com/raqueeb/fdebook_companion)

এই রিপোজিটরিতে **ফরওয়ার্ড ডেপ্লয়েড ইঞ্জিনিয়ারিং (FDE) - ফিল্ড ম্যানুয়াল** বইয়ের প্রতিটা অধ্যায়ের **কোড-স্যান্ডউইচ (Code-Sandwich)** স্ক্রিপ্ট, মক ডেটাসেট এবং সেলফ-হিলিং সিআই/সিডি পাইপলাইন সাজিয়ে রাখা হয়েছে। প্রতিটা স্ক্রিপ্ট পাইথনের স্ট্যান্ডার্ড লাইব্রেরিতে লেখা - তাই কোনো পেইড ক্লাউড বা এক্সটার্নাল এপিআই ছাড়াই নিজের ল্যাপটপে সরাসরি চালিয়ে দেখা যাবে।

---

## চ্যাপ্টারভিত্তিক ফোল্ডার ও স্ক্রিপ্ট তালিকা

| অধ্যায় | ফোল্ডার ও ফাইল | কাজ ও বিবরণ |
| :--- | :--- | :--- |
| **ইন্ট্রোডাকশন** | `intro-silent-churn/detect_silent_abandonment.py` | ডেটাবেজ লগ থেকে সাইলেন্ট চর্ন ও শ্যাডো আইটি ডিটেক্টর |
| **চ্যাপ্টার ১** | `ch01-field-discovery/bottleneck_analyzer.py` | শ্যাডো সেশন বনাম কাগুজে এসওপির বটলনেক ডায়াগনস্টিক ইঞ্জিন |
| **চ্যাপ্টার ১** | `ch01-field-discovery/otp_sla_tracker.py` | ১-ট্যাপ ওটিপি অনুমোদন ও ১০ মিনিটের ফলসিফায়েবল মেট্রিক ট্র্যাকার |
| **চ্যাপ্টার ২** | `ch02-local-triage-engine/sqlite_wal_queue.py` | ক্যাফকা ছাড়াই `SQLite WAL` মোডে হাই-কনকারেন্সি লোকাল কিউ |
| **চ্যাপ্টার ২** | `ch02-local-triage-engine/triage.py` | লোকাল এলএলএম (`Ollama` + `Qwen 2.5`) কাস্টমার টিকিট ট্রায়াজ ইঞ্জিন |
| **চ্যাপ্টার ২** | `ch02-local-triage-engine/mock_tickets.json` | ফিল্ড টেস্টের জন্য বাস্তব বাংলা ও বাংলিশ কাস্টমার কমপ্লেইন্ট ডেটাসেট |
| **চ্যাপ্টার ৩** | `ch03-resilient-pipeline/domain_sprint_vat.py` | ২০ মিনিটের ডোমেইন স্প্রিন্ট: লাল খাতার ভ্যাট ও রিবেট গার্ডরেইল ইঞ্জিন |
| **চ্যাপ্টার ৩** | `ch03-resilient-pipeline/eval_harness.py` | বিল্ডের আগেই গোল্ডেন ডেটাসেট ইভ্যালুয়েশন হারনেস টেস্টবেঞ্চ |
| **চ্যাপ্টার ৩** | `ch03-resilient-pipeline/.github/workflows/field-deploy.yml` | সেলফ-হিলিং অন-প্রেম ডেপ্লয়মেন্ট ও অটো-রোলব্যাক পাইপলাইন |
| **চ্যাপ্টার ৪** | `ch04-isp-routing-worker/worker.py` | ট্র্যাক এ: ঢাকার আইএসপি ফাইবার কাট (`OLT LOS`) অ্যাসিনক্রোনাস রাউটার |
| **চ্যাপ্টার ৪** | `ch04-supply-chain-reconciler/audit.py` | ট্র্যাক বি: চট্টগ্রাম বন্দরের থ্রি-ওয়ে ইনভয়েস ও ওয়েব্রিজ রিকনসিলার |
| **চ্যাপ্টার ৪** | `ch04-supply-chain-reconciler/manager_hero_report.py` | ফিল্ড পলিটিক্স: মিড-লেভেল ম্যানেজারের জন্য ১-ক্লিক সামারি জেনারেটর |
| **চ্যাপ্টার ৫** | `ch05-org-scaling/field_to_core_module.py` | প্যালান্টির প্যাটার্ন: ফিল্ড-টু-কোর কনফিগ ডিকাপলার ইঞ্জিন |
| **চ্যাপ্টার ৫** | `ch05-org-scaling/quick_win_scorer.py` | প্রথম সপ্তাহের কুইক-উইন বাছাইয়ের র‍্যাংকিং অ্যালগরিদম |
| **কনক্লুশন** | `conclusion-handover/health_check.py` | অটোমেটেড অন-প্রেম সার্ভার হেলথ চেক ক্রন স্ক্রিপ্ট |
| **কনক্লুশন** | `conclusion-handover/hypercare_watchdog.py` | হাইপার-কেয়ার প্রোঅ্যাকটিভ মেমোরি ও লেটেন্সি ওয়াচডগ |

---

## দ্রুত রান করার গাইড

```bash
git clone https://github.com/raqueeb/fdebook_companion.git
cd fdebook_companion

# যেকোনো স্ক্রিপ্ট সরাসরি রান করুন (Python 3.10+)
python3 intro-silent-churn/detect_silent_abandonment.py
python3 ch01-field-discovery/bottleneck_analyzer.py
python3 ch01-field-discovery/otp_sla_tracker.py
python3 ch02-local-triage-engine/sqlite_wal_queue.py
python3 ch02-local-triage-engine/triage.py
python3 ch03-resilient-pipeline/domain_sprint_vat.py
python3 ch03-resilient-pipeline/eval_harness.py
python3 ch04-isp-routing-worker/worker.py
python3 ch04-supply-chain-reconciler/audit.py
python3 ch04-supply-chain-reconciler/manager_hero_report.py
python3 ch05-org-scaling/field_to_core_module.py
python3 ch05-org-scaling/quick_win_scorer.py
python3 conclusion-handover/health_check.py
python3 conclusion-handover/hypercare_watchdog.py
```
