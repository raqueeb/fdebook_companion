# হাতেকলমে ফরওয়ার্ড ডেপ্লয়েড ইঞ্জিনিয়ারিং (FDE)
### অফিশিয়াল কমপ্যানিয়ন কোডবেস

[![Read Online](https://img.shields.io/badge/Book-Read%20Online-1a73e8?style=for-the-badge&logo=gitbook&logoColor=white)](https://aiwithr.github.io/fde_book/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Zero Cloud Cost](https://img.shields.io/badge/Cloud%20Cost-%240.00%20(On--Prem)-brightgreen?style=for-the-badge&logo=server)](https://aiwithr.github.io/fde_book/chapter-2/)
[![Author Portal](https://img.shields.io/badge/Author-aiwithr.github.io-black?style=for-the-badge&logo=github)](https://aiwithr.github.io/)

---

> **"সফটওয়্যার আর্কিটেকচার থেকে কাস্টমারের গ্রাউন্ড রিয়েলিটি।"**  
> এই রিপোজিটরি রকিবুল হাসান রচিত **[হাতেকলমে ফরওয়ার্ড ডেপ্লয়েড ইঞ্জিনিয়ারিং (FDE)](https://aiwithr.github.io/fde_book/)** বইটির অফিশিয়াল ওপেন-সোর্স কমপ্যানিয়ন কোডবেস। বইটিতে আলোচিত প্রতিটা আর্কিটেকচারাল প্যাটার্ন, লোকাল ট্রায়াজ ইঞ্জিন, মূল্যায়ন টেস্টবেঞ্চ এবং সেলফ-হিলিং সিআই/সিডি অটোমেশন স্ক্রিপ্ট এখানে সাজানো রয়েছে।

---

## ইকোসিস্টেম ও প্রয়োজনীয় ক্রস-রেফারেন্স লিংক

| রিসোর্স | লিংক | সংক্ষিপ্ত বিবরণ |
| :--- | :--- | :--- |
| **অনলাইন বই (Live Book)** | [aiwithr.github.io/fde_book](https://aiwithr.github.io/fde_book/) | পুরো বইয়ের সম্পূর্ণ অনলাইন সংস্করণ (ফ্রি রিডিং) |
| **বইয়ের মূল রিপোজিটরি** | [github.com/aiwithr/fde_book](https://github.com/aiwithr/fde_book) | বইটির সোর্স কোড ও ডকুমেন্টেশন রিপোজিটরি |
| **কমপ্যানিয়ন কোডবেস** | [github.com/raqueeb/fdebook_companion](https://github.com/raqueeb/fdebook_companion) | এই রিপোজিটরি (সব কোড-স্যান্ডউইচ ও স্ক্রিপ্ট) |
| **লেখকের মূল পোর্টাল** | [aiwithr.github.io](https://aiwithr.github.io/) | রকিবুল হাসানের অফিশিয়াল হোমপেজ |
| **রিসোর্স হাব** | [aiwithr.github.io/resources](https://aiwithr.github.io/resources/) | প্রকাশিত প্রযুক্তি রিসোর্স, টুলকিট ও নির্দেশিকা |
| **লেখক পরিচিতি** | [aiwithr.github.io/about](https://aiwithr.github.io/about/) | লেখকের বায়ো, ব্যাকগ্রাউন্ড ও কনসাল্টেশন |
| **প্রিন্ট মিডিয়া কলাম** | [aiwithr.github.io/print](https://aiwithr.github.io/print/) | জাতীয় পত্রপত্রিকায় লেখকের প্রকাশিত লেখালেখি |

---

## মূল আর্কিটেকচারাল বৈশিষ্ট্য

* **জিরো-ক্লাউড ও অন-প্রেম প্রাধান্য ($0.00 Cloud Cost):** কোনো পেইড ক্লাউড সাবস্ক্রিপশন বা বিদেশি সার্ভারের ওপর নির্ভরতা নেই। সরকারি দপ্তর, বন্দর কিংবা কারখানার ইন্টারনেট-বিচ্ছিন্ন (Air-Gapped) সাধারণ অন-প্রেম সার্ভারে পুরো সিস্টেমটি শতভাগ সচল থাকে।
* **জিরো এক্সটার্নাল ডিপেন্ডেন্সি (Standard Library First):** কোর স্ক্রিপ্টগুলো সাধারণ `Python 3.10+` এর স্ট্যান্ডার্ড লাইব্রেরি দিয়ে তৈরি। কোনো ভারী ভার্চুয়াল এনভায়রনমেন্ট বা প্যাকেজ জটিলতা ছাড়াই যেকোনো ফিল্ড মেশিনে সরাসরি রান করা যায়।
* **প্যালান্টির প্যাটার্ন ও লোকাল এআই:** ক্যাফকা ছাড়াই `SQLite WAL` মোডে হাই-কনকারেন্সি কিউ, `Ollama` ও `Qwen 2.5` দিয়ে লোকাল এআই টিকিট ট্রায়াজ, গোল্ডেন ডেটাসেট ইভ্যালুয়েশন হারনেস এবং টেস্ট ফেইল করলে সেলফ-হিলিং অটো-রোলব্যাক পাইপলাইন।

---

## ডিরেক্টরি কাঠামো

```
fdebook_companion/
├── LICENSE                                # এমআইটি ওপেন সোর্স লাইসেন্স
├── README.md                              # কমপ্যানিয়ন রানবুক ও আর্কিটেকচার গাইড
├── intro-silent-churn/
│   └── detect_silent_abandonment.py       # সাইলেন্ট চার্ন ও শ্যাডো আইটি ডিটেক্টর
├── ch01-field-discovery/
│   ├── bottleneck_analyzer.py             # কাগুজে এসওপি বনাম আসল ফিল্ড বটলনেক ডায়াগনস্টিক
│   └── otp_sla_tracker.py                 # ১-ট্যাপ ওটিপি অনুমোদন ও ১০ মিনিটের ফলসিফায়েবল মেট্রিক
├── ch02-local-triage-engine/
│   ├── sqlite_wal_queue.py                # ক্যাফকা ছাড়া SQLite WAL হাই-কনকারেন্সি লোকাল কিউ
│   ├── triage.py                          # Ollama + Qwen 2.5 লোকাল এআই ট্রায়াজ ইঞ্জিন
│   └── mock_tickets.json                  # বাংলা ও বাংলিশ কাস্টমার কমপ্লেইন্ট গোল্ডেন ডেটাসেট
├── ch03-resilient-pipeline/
│   ├── domain_sprint_vat.py               # ২০ মিনিটের ডোমেইন স্প্রিন্ট: লাল খাতার ভ্যাট গার্ডরেইল
│   ├── eval_harness.py                    # বিল্ড-পূর্ব গোল্ডেন ডেটাসেট ইভ্যালুয়েশন টেস্টবেঞ্চ
│   └── .github/workflows/
│       └── field-deploy.yml               # সেলফ-হিলিং অন-প্রেম ডেপ্লয়মেন্ট ও অটো-রোলব্যাক
├── ch04-isp-routing-worker/
│   └── worker.py                          # ট্র্যাক এ: ঢাকা আইএসপি ফাইবার কাট (OLT LOS) রাউটার
├── ch04-supply-chain-reconciler/
│   ├── audit.py                           # ট্র্যাক বি: চট্টগ্রাম বন্দর থ্রি-ওয়ে ইনভয়েস ও স্কেল অডিট
│   └── manager_hero_report.py             # ফিল্ড পলিটিক্স: মিড-লেভেল ম্যানেজারের ১-ক্লিক রিপোর্ট
├── ch05-org-scaling/
│   ├── field_to_core_module.py            # প্যালান্টির প্যাটার্ন: কোর ইঞ্জিন বনাম ব্রাঞ্চ কনফিগ ডিকাপলার
│   └── quick_win_scorer.py                # প্রথম সপ্তাহের কুইক-উইন প্রায়োরিটাইজেশন স্কোরার
└── conclusion-handover/
    ├── health_check.py                    # হ্যান্ডওভার-পরবর্তী অটোমেটেড সার্ভার হেলথ চেক ক্রন স্ক্রিপ্ট
    └── hypercare_watchdog.py              # হাইপার-কেয়ার প্রোঅ্যাকটিভ মেমোরি স্পাইক ও লেটেন্সি ওয়াচডগ
```

---

## চ্যাপ্টারভিত্তিক কোড ও রান ম্যাট্রিক্স

| অধ্যায় ও বইয়ের লিংক | স্ক্রিপ্ট পাথ | ফিল্ডের কাজ ও বিবরণ | রান করার কমান্ড |
| :--- | :--- | :--- | :--- |
| [**Introduction: গ্রাউন্ড রিয়েলিটি**](https://aiwithr.github.io/fde_book/intro/) | `intro-silent-churn/detect_silent_abandonment.py` | ডেটাবেজ স্ক্যান করে সাইলেন্ট চার্ন ও শ্যাডো আইটি শনাক্তকরণ | `python3 intro-silent-churn/detect_silent_abandonment.py` |
| [**Chapter 1: ফিল্ড ডিসকাভারি ও এসওপি**](https://aiwithr.github.io/fde_book/chapter-1/) | `ch01-field-discovery/bottleneck_analyzer.py` | শ্যাডো সেশনের আসল সময় মেপে এসওপির বটলনেক বিশ্লেষণ | `python3 ch01-field-discovery/bottleneck_analyzer.py` |
| [**Chapter 1: ফিল্ড ডিসকাভারি ও এসওপি**](https://aiwithr.github.io/fde_book/chapter-1/) | `ch01-field-discovery/otp_sla_tracker.py` | ম্যানেজারের ১-ট্যাপ ওটিপি অনুমোদন ও ১০ মিনিটের এসএলএ মেট্রিক | `python3 ch01-field-discovery/otp_sla_tracker.py` |
| [**Chapter 2: লোকাল আর্কিটেকচার**](https://aiwithr.github.io/fde_book/chapter-2/) | `ch02-local-triage-engine/sqlite_wal_queue.py` | ক্যাফকা ছাড়া `SQLite WAL` মোডে হাই-কনকারেন্সি কিউ সামলানো | `python3 ch02-local-triage-engine/sqlite_wal_queue.py` |
| [**Chapter 2: লোকাল আর্কিটেকচার**](https://aiwithr.github.io/fde_book/chapter-2/) | `ch02-local-triage-engine/triage.py` | লোকাল এআই (`Ollama`) দিয়ে বাংলা টিকিট ট্রায়াজ (ফলব্যাক সহ) | `python3 ch02-local-triage-engine/triage.py` |
| [**Chapter 3: দ্য নিউ এসডিএলসি**](https://aiwithr.github.io/fde_book/chapter-3/) | `ch03-resilient-pipeline/domain_sprint_vat.py` | ২০ মিনিটের ডোমেইন স্প্রিন্ট: ভ্যাট ও রিবেট টেস্ট গার্ডরেইল | `python3 ch03-resilient-pipeline/domain_sprint_vat.py` |
| [**Chapter 3: দ্য নিউ এসডিএলসি**](https://aiwithr.github.io/fde_book/chapter-3/) | `ch03-resilient-pipeline/eval_harness.py` | বিল্ডের আগে গোল্ডেন ডেটাসেটে মডেলের স্কিমা ও অ্যাকুরেসি টেস্ট | `python3 ch03-resilient-pipeline/eval_harness.py` |
| [**Chapter 3: দ্য নিউ এসডিএলসি**](https://aiwithr.github.io/fde_book/chapter-3/) | `ch03-resilient-pipeline/.github/workflows/field-deploy.yml` | অন-প্রেম টেস্ট ফেইল করলে সেলফ-হিলিং অটো-রোলব্যাক | GitHub Actions অটোমেটেড |
| [**Chapter 4: ফিল্ড প্লেবুক (আইএসপি)**](https://aiwithr.github.io/fde_book/chapter-4/) | `ch04-isp-routing-worker/worker.py` | ঢাকা ফাইবার কাটে কলসেন্টার ট্র্যাফিক কমাতে অ্যাসিনক্রোনাস রাউটার | `python3 ch04-isp-routing-worker/worker.py` |
| [**Chapter 4: ফিল্ড প্লেবুক (সাপ্লাই চেইন)**](https://aiwithr.github.io/fde_book/chapter-4/) | `ch04-supply-chain-reconciler/audit.py` | চট্টগ্রাম বন্দর কাস্টমস বিল, ইনভয়েস ও স্কেলের ১% অডিট | `python3 ch04-supply-chain-reconciler/audit.py` |
| [**Chapter 4: ফিল্ড প্লেবুক (পলিটিক্স)**](https://aiwithr.github.io/fde_book/chapter-4/) | `ch04-supply-chain-reconciler/manager_hero_report.py` | ম্যানেজারের জন্য ১-ক্লিক এক্সিকিউটিভ ডেমারেজ সেভিংস সামারি | `python3 ch04-supply-chain-reconciler/manager_hero_report.py` |
| [**Chapter 5: অর্গানাইজেশন স্কেলিং**](https://aiwithr.github.io/fde_book/chapter-5/) | `ch05-org-scaling/field_to_core_module.py` | প্যালান্টির প্যাটার্ন: কোর ইঞ্জিনে হাত না দিয়ে ফিল্ড কনফিগ ডিকাপল | `python3 ch05-org-scaling/field_to_core_module.py` |
| [**Chapter 5: অর্গানাইজেশন স্কেলিং**](https://aiwithr.github.io/fde_book/chapter-5/) | `ch05-org-scaling/quick_win_scorer.py` | প্রথম সপ্তাহের কুইক-উইন বাছাই করতে অপচয় ও ঝুঁকি স্কোরিং | `python3 ch05-org-scaling/quick_win_scorer.py` |
| [**Conclusion: হ্যান্ডওভার ও এক্সিট**](https://aiwithr.github.io/fde_book/conclusion/) | `conclusion-handover/health_check.py` | লোকাল আইটি টিমের জন্য অটোমেটেড ৫ মিনিটের হেলথ চেক স্ক্রিপ্ট | `python3 conclusion-handover/health_check.py` |
| [**Conclusion: হ্যান্ডওভার ও এক্সিট**](https://aiwithr.github.io/fde_book/conclusion/) | `conclusion-handover/hypercare_watchdog.py` | হাইপার-কেয়ার পর্বের প্রোঅ্যাকটিভ মেমোরি ও লেটেন্সি ওয়াচডগ | `python3 conclusion-handover/hypercare_watchdog.py` |

---

## দ্রুত শুরু করার গাইড (Quickstart)

### ১. রিপোজিটরি ক্লোন করুন
```bash
git clone https://github.com/raqueeb/fdebook_companion.git
cd fdebook_companion
```

### ২. স্ক্রিপ্ট এক্সিকিউট করুন (Python 3.10+)
সব স্ক্রিপ্ট সরাসরি পাইথন রানটাইমে চালানো যায়:
```bash
# উদাহরণ ১: শ্যাডো সেশনের বটলনেক ডায়াগনস্টিক
python3 ch01-field-discovery/bottleneck_analyzer.py

# উদাহরণ ২: ডোমেইন স্প্রিন্টের ভ্যাট ও রিবেট টেস্ট
python3 ch03-resilient-pipeline/domain_sprint_vat.py

# উদাহরণ ৩: চট্টগ্রাম বন্দর রিকনসিলার ও ১-ক্লিক ম্যানেজার রিপোর্ট
python3 ch04-supply-chain-reconciler/manager_hero_report.py
```

### ৩. লোকাল এআই সেটআপ (ঐচ্ছিক)
চ্যাপ্টার ২-এর এআই টিকিট ট্রায়াজ স্ক্রিপ্ট লোকাল লার্জ ল্যাঙ্গুয়েজ মডেল দিয়ে পরীক্ষা করতে চাইলে:
```bash
# Ollama ইনস্টল করার পর ১ জিবির হালকা মডেলটি নামিয়ে নিন
ollama pull qwen2.5:1.5b

# লোকাল ট্রায়াজ ইঞ্জিন রান করুন
python3 ch02-local-triage-engine/triage.py
```
> *নোট: কম্পিউটারে Ollama চালু না থাকলেও স্ক্রিপ্টটিতে অফলাইন সিমুলেশন ফলব্যাক দেওয়া আছে। ফলে কোনো পরিস্থিতিতেই প্রোগ্রাম ক্র্যাশ করবে না।*

---

## লেখক ও লাইসেন্স

* **লেখক:** রকিবুল হাসান ([Rakibul Hassan](https://aiwithr.github.io/about/)) | [রিসোর্স হাব](https://aiwithr.github.io/resources/) | [ওয়েবসাইট](https://aiwithr.github.io/)
* **লাইসেন্স:** এই কোডবেসের সমস্ত স্ক্রিপ্ট ও কনফিগারেশন [MIT License](LICENSE)-এর অধীনে উন্মুক্ত। ব্যক্তিগত শেখার কাজে কিংবা নিজস্ব প্রতিষ্ঠানের অন-প্রেম অটোমেশন প্রজেক্টে এই কোড মুক্তভাবে ব্যবহার ও পরিবর্তন করতে পারবেন।
