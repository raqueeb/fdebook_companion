# ফরওয়ার্ড ডেপ্লয়েড ইঞ্জিনিয়ারিং (FDE) - ফিল্ড ম্যানুয়াল
### Official Companion Codebase & Production Playbook

[![Read Online](https://img.shields.io/badge/Book-Read%20Online-1a73e8?style=for-the-badge&logo=gitbook&logoColor=white)](https://aiwithr.github.io/fde_book/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Zero Cloud Cost](https://img.shields.io/badge/Cloud%20Cost-%240.00%20(On--Prem)-brightgreen?style=for-the-badge&logo=server)](https://aiwithr.github.io/fde_book/chapter-2/)
[![Author Portal](https://img.shields.io/badge/Author-aiwithr.github.io-black?style=for-the-badge&logo=github)](https://aiwithr.github.io/)

---

> **"সফটওয়্যার আর্কিটেকচার থেকে কাস্টমারের গ্রাউন্ড রিয়েলিটি।"**  
> এই রিপোজিটরিটি রকিবুল হাসান রচিত **[ফরওয়ার্ড ডেপ্লয়েড ইঞ্জিনিয়ারিং (FDE) - ফিল্ড ম্যানুয়াল](https://aiwithr.github.io/fde_book/)** বইটির অফিশিয়াল ওপেন-সোর্স কমপ্যানিয়ন কোডবেস। বইটিতে আলোচিত প্রতিটা আর্কিটেকচারাল প্যাটার্ন, ফিল্ড ডায়াগনস্টিক, অন-প্রেম লোকাল এআই ওয়ার্কার এবং সেলফ-হিলিং সিআই/সিডি পাইপলাইনের স্বয়ংসম্পূর্ণ স্ক্রিপ্ট এখানে সুবিন্যস্তভাবে সাজানো রয়েছে।

---

## 🔗 ক্রস-রেফারেন্স ও প্রয়োজনীয় লিংক (Author & Ecosystem Links)

| রিসোর্স | লিংক | বিবরণ |
| :--- | :--- | :--- |
| 📖 **লাইভ বই (Live Book)** | [aiwithr.github.io/fde_book](https://aiwithr.github.io/fde_book/) | পুরো বইয়ের সম্পূর্ণ অনলাইন সংস্করণ (ফ্রি রিডিং) |
| 📦 **বইয়ের গিটহাব রিপোজিটরি** | [github.com/aiwithr/fde_book](https://github.com/aiwithr/fde_book) | বইটির মূল সোর্স কোড ও ডকুমেন্টেশন রিপোজিটরি |
| 💻 **কমপ্যানিয়ন কোডবেস** | [github.com/raqueeb/fdebook_companion](https://github.com/raqueeb/fdebook_companion) | এই রিপোজিটরি (সব কোড-স্যান্ডউইচ ও স্ক্রিপ্ট) |
| 🌐 **লেখকের মূল পোর্টাল** | [aiwithr.github.io](https://aiwithr.github.io/) | রকিবুল হাসানের অফিশিয়াল হোমপেজ |
| 📚 **রিসোর্স সেন্টার** | [aiwithr.github.io/resources](https://aiwithr.github.io/resources/) | প্রকাশিত প্রযুক্তি রিসোর্স, টুলকিট ও নির্দেশিকা |
| 👨‍💻 **লেখক পরিচিতি** | [aiwithr.github.io/about](https://aiwithr.github.io/about/) | লেখকের বায়ো, ব্যাকগ্রাউন্ড ও কনসাল্টেশন |
| 📰 **প্রিন্ট মিডিয়া কলাম** | [aiwithr.github.io/print](https://aiwithr.github.io/print/) | জাতীয় পত্রপত্রিকা ও মিডিয়াতে লেখকের প্রকাশিত লেখালেখি |

---

## 💡 আর্কিটেকচারাল ফিলোসফি (Core Design Ethos)

এই কমপ্যানিয়ন কোডবেসটি ৩টি মৌলিক ফিল্ড প্রিন্সিপালের ওপর ভিত্তি করে তৈরি:

1. **জিরো-ক্লাউড ফুটপ্রিন্ট ($0.00 Cloud Cost):**  
   কোনো পেইড ক্লাউড এপিআই বা বিদেশি ক্লাউড ইনফ্রাস্ট্রাকচারের ওপর নির্ভরতা নেই। সরকারি দপ্তর, বন্দর বা কারখানা যেখানে ইন্টারনেট বিচ্ছিন্ন (Air-Gapped) কিংবা ডেটা সিকিউরিটি বাধ্যতামূলক, সেখানেও সম্পূর্ণ অন-প্রেমে নির্বিঘ্নে চলবে।
2. **জিরো এক্সটার্নাল পাইথন ডিপেন্ডেন্সি (Standard Library First):**  
   কোর স্ক্রিপ্টগুলোর জন্য কোনো ভারী ভার্চুয়াল এনভায়রনমেন্ট বা থার্ড-পার্টি লাইব্রেরির প্রয়োজন হয় না। আধুনিক Python 3.10+ এর স্ট্যান্ডার্ড লাইব্রেরি দিয়ে তৈরি—যাতে যেকোনো ফিল্ড সার্ভারে ৩ সেকেন্ডে রান করা যায়।
3. **প্যালান্টির প্যাটার্ন ও লোকাল এআই (Palantir Pattern & Local LLM):**  
   বিল্ডের আগেই গোল্ডেন ডেটাসেট দিয়ে ইভ্যালুয়েশন হারনেস, Ollama ও Qwen 2.5 লোকাল ট্রায়াজ, SQLite WAL কনকারেন্ট কিউ এবং ফেইলিওর হলে অটোমেটেড সেলফ-হিলিং রোলব্যাক পাইপলাইন।

---

## 🗺️ চ্যাপ্টারভিত্তিক কোড ম্যাপ ও রান গাইড

বইয়ের প্রতিটি অধ্যায়ের সাথে সঙ্গতিপূর্ণ স্ক্রিপ্টগুলোর তালিকা নিচে দেওয়া হলো:

```
fdebook_companion/
├── intro-silent-churn/
│   └── detect_silent_abandonment.py       # সাইলেন্ট চার্ন ও শ্যাডো আইটি ডিটেক্টর
├── ch01-field-discovery/
│   ├── bottleneck_analyzer.py             # কাগুজে এসওপি বনাম আসল ফিল্ড বটলনেক
│   └── otp_sla_tracker.py                 # ১-ট্যাপ ওটিপি অনুমোদন ও ১০ মি. মেট্রিক
├── ch02-local-triage-engine/
│   ├── sqlite_wal_queue.py                # জিরো-ডিপেন্ডেন্সি SQLite WAL হাই-কনকারেন্সি কিউ
│   ├── triage.py                          # Ollama + Qwen 2.5 লোকাল এআই ট্রায়াজ ইঞ্জিন
│   └── mock_tickets.json                  # বাংলা ও বাংলিশ কাস্টমার টিকেট গোল্ডেন ডেটাসেট
├── ch03-resilient-pipeline/
│   ├── domain_sprint_vat.py               # লাল খাতার ২০ মিনিটের ভ্যাট গার্ডরেইল
│   ├── eval_harness.py                    # বিল্ড-পূর্ব গোল্ডেন সেট ইভ্যালুয়েশন টেস্টবেঞ্চ
│   └── .github/workflows/
│       └── field-deploy.yml               # সেলফ-হিলিং ডেপ্লয়মেন্ট ও অটো-রোলব্যাক CI/CD
├── ch04-isp-routing-worker/
│   └── worker.py                          # আইএসপি ফাইবার কাট (OLT LOS) অ্যাসিনক্রোনাস রাউটার
├── ch04-supply-chain-reconciler/
│   ├── audit.py                           # চট্টগ্রাম বন্দরের থ্রি-ওয়ে ইনভয়েস ও স্কেল অডিট
│   └── manager_hero_report.py             # মিড-লেভেল ম্যানেজারের জন্য ১-ক্লিক এক্সিকিউটিভ রিপোর্ট
├── ch05-org-scaling/
│   ├── field_to_core_module.py            # প্যালান্টির প্যাটার্ন: ফিল্ড-টু-কোর কনফিগ ইঞ্জিন
│   └── quick_win_scorer.py                # প্রথম সপ্তাহের কুইক-উইন প্রায়োরিটাইজেশন স্কোরার
└── conclusion-handover/
    ├── health_check.py                    # হ্যান্ডওভার-পরবর্তী অটোমেটেড সার্ভার হেলথ চেক
    └── hypercare_watchdog.py              # হাইপার-কেয়ার প্রোঅ্যাকটিভ মেমোরি ও লেটেন্সি ওয়াচডগ
```

---

## 📖 বিস্তারিত চ্যাপ্টার রেফারেন্স ও এক্সিকিউশন

| অধ্যায় ও বইয়ের লিংক | স্ক্রিপ্ট পাথ | মূল কাজ | রান করার কমান্ড |
| :--- | :--- | :--- | :--- |
| [**Introduction: গ্রাউন্ড রিয়েলিটি**](https://aiwithr.github.io/fde_book/intro/) | `intro-silent-churn/detect_silent_abandonment.py` | ডেটাবেজ অ্যাক্টিভিটি অডিট করে সিস্টেম বর্জন ও সাইলেন্ট চার্ন ধরা | `python3 intro-silent-churn/detect_silent_abandonment.py` |
| [**Chapter 1: ফিল্ড ডিসকভারি ও এসওপি**](https://aiwithr.github.io/fde_book/chapter-1/) | `ch01-field-discovery/bottleneck_analyzer.py` | শ্যাডো সেশনের আসল সময় দিয়ে এসওপির শুভঙ্করের ফাঁকি ধরা | `python3 ch01-field-discovery/bottleneck_analyzer.py` |
| [**Chapter 1: ফিল্ড ডিসকভারি ও এসওপি**](https://aiwithr.github.io/fde_book/chapter-1/) | `ch01-field-discovery/otp_sla_tracker.py` | ম্যানেজারের ১-ট্যাপ ওটিপি অনুমোদন ও ১০ মিনিটের ফলসিফায়েবল এসএলএ | `python3 ch01-field-discovery/otp_sla_tracker.py` |
| [**Chapter 2: লোকাল আর্কিটেকচার**](https://aiwithr.github.io/fde_book/chapter-2/) | `ch02-local-triage-engine/sqlite_wal_queue.py` | ক্যাফকা বা রেডিস ছাড়াই ১,০০০+ টিপিএস লোকাল কিউ সিস্টেম | `python3 ch02-local-triage-engine/sqlite_wal_queue.py` |
| [**Chapter 2: লোকাল আর্কিটেকচার**](https://aiwithr.github.io/fde_book/chapter-2/) | `ch02-local-triage-engine/triage.py` | লোকাল এলএলএম (Ollama) দিয়ে বাংলা কাস্টমার অভিযোগ ট্রায়াজ | `python3 ch02-local-triage-engine/triage.py` |
| [**Chapter 3: দ্য নিউ এসডিএলসি**](https://aiwithr.github.io/fde_book/chapter-3/) | `ch03-resilient-pipeline/domain_sprint_vat.py` | ২০ মিনিটের ডোমেইন স্প্রিন্ট: ১৫% ভ্যাট ও ৫% রিবেট টেস্ট গার্ডরেইল | `python3 ch03-resilient-pipeline/domain_sprint_vat.py` |
| [**Chapter 3: দ্য নিউ এসডিএলসি**](https://aiwithr.github.io/fde_book/chapter-3/) | `ch03-resilient-pipeline/eval_harness.py` | বিল্ডের আগে গোল্ডেন ডেটাসেটে মডেলের স্কিমা ও অ্যাকুরেসি পাসরেট যাচাই | `python3 ch03-resilient-pipeline/eval_harness.py` |
| [**Chapter 3: দ্য নিউ এসডিএলসি**](https://aiwithr.github.io/fde_book/chapter-3/) | `ch03-resilient-pipeline/.github/workflows/field-deploy.yml` | অন-প্রেম সেলফ-হিলিং ডিপ্লয় ও টেস্ট ফেইল করলে অটো-রোলব্যাক | GitHub Actions অটোমেটেড |
| [**Chapter 4: ফিল্ড প্লেবুক (আইএসপি)**](https://aiwithr.github.io/fde_book/chapter-4/) | `ch04-isp-routing-worker/worker.py` | ঢাকা ফাইবার কাটে কলসেন্টার ট্র্যাফিক কমাতে স্মার্ট অ্যাসিনক্রোনাস রাউটিং | `python3 ch04-isp-routing-worker/worker.py` |
| [**Chapter 4: ফিল্ড প্লেবুক (সাপ্লাই চেইন)**](https://aiwithr.github.io/fde_book/chapter-4/) | `ch04-supply-chain-reconciler/audit.py` | চট্টগ্রাম কাস্টমস বিল, ইনভয়েস ও স্কেলের ১% টলারেন্স থ্রি-ওয়ে অডিট | `python3 ch04-supply-chain-reconciler/audit.py` |
| [**Chapter 4: ফিল্ড প্লেবুক (পলিটিক্স)**](https://aiwithr.github.io/fde_book/chapter-4/) | `ch04-supply-chain-reconciler/manager_hero_report.py` | ম্যানেজারের ক্রেডিট ও ডেমারেজ সাশ্রয় তুলে ধরে ১-ক্লিক সামারি তৈরি | `python3 ch04-supply-chain-reconciler/manager_hero_report.py` |
| [**Chapter 5: অর্গানাইজেশন স্কেলিং**](https://aiwithr.github.io/fde_book/chapter-5/) | `ch05-org-scaling/field_to_core_module.py` | প্যালান্টির প্যাটার্ন: কোর ইঞ্জিনে হাত না দিয়ে ব্রাঞ্চ কনফিগারেশন ডিকাপল | `python3 ch05-org-scaling/field_to_core_module.py` |
| [**Chapter 5: অর্গানাইজেশন স্কেলিং**](https://aiwithr.github.io/fde_book/chapter-5/) | `ch05-org-scaling/quick_win_scorer.py` | প্রথম সপ্তাহের কুইক-উইন বাছাই করতে দৈনিক অপচয় ও রিস্ক স্কোরিং | `python3 ch05-org-scaling/quick_win_scorer.py` |
| [**Conclusion: হ্যান্ডওভার ও সাসটেইনেবিলিটি**](https://aiwithr.github.io/fde_book/conclusion/) | `conclusion-handover/health_check.py` | লোকাল টিমের জন্য অটোমেটেড ৫ মিনিটের হেলথ ডায়াগনস্টিক ক্রন স্ক্রিপ্ট | `python3 conclusion-handover/health_check.py` |
| [**Conclusion: হ্যান্ডওভার ও সাসটেইনেবিলিটি**](https://aiwithr.github.io/fde_book/conclusion/) | `conclusion-handover/hypercare_watchdog.py` | হাইপার-কেয়ার পর্বের প্রোঅ্যাকটিভ মেমোরি স্পাইক ও লেটেন্সি ওয়াচডগ | `python3 conclusion-handover/hypercare_watchdog.py` |

---

## 🚀 দ্রুত শুরু করুন (Quickstart)

### ১. ক্লোন করুন
```bash
git clone https://github.com/raqueeb/fdebook_companion.git
cd fdebook_companion
```

### ২. পরিবেশ পরীক্ষা (Python 3.10+)
সব স্ক্রিপ্ট সরাসরি পাইথন রানটাইমে এক্সিকিউট করা যায়:
```bash
python3 --version
```

### ৩. লোকাল এআই ট্রায়াজ রান (ঐচ্ছিক - Ollama Setup)
চ্যাপ্টার ২-এর এআই ট্রায়াজ স্ক্রিপ্ট লোকাল এলএলএম দিয়ে টেস্ট করতে চাইলে [Ollama](https://ollama.com/) নামিয়ে চালান:
```bash
# Ollama ইনস্টল করার পর মডেল নামিয়ে নিন (মাত্র ১ জিবি VRAM প্রয়োজন)
ollama pull qwen2.5:1.5b

# লোকাল ট্রায়াজ স্ক্রিপ্ট রান করুন
python3 ch02-local-triage-engine/triage.py
```
> *নোট: আপনার মেশিনে Ollama চালু না থাকলেও স্ক্রিপ্টটিতে বিল্ট-ইন অফলাইন ফলব্যাক দেওয়া আছে, তাই স্ক্রিপ্ট কোনো অবস্থাতেই ক্র্যাশ করবে না।*

---

## 🤝 লেখক ও পরামর্শ (Author & Community)

- **লেখক:** রকিবুল হাসান ([Rakibul Hassan](https://aiwithr.github.io/about/))
- **অফিশিয়াল রিসোর্স হাব:** [aiwithr.github.io/resources](https://aiwithr.github.io/resources/)
- **আলোচনা ও মতামত:** বই বা কোডবেস সম্পর্কিত যেকোনো আলোচনা বা পরামর্শ জানাতে রিপোজিটরির [Issues](https://github.com/raqueeb/fdebook_companion/issues) সেকশনে টিকিট খুলুন অথবা লেখকের [কন্ট্যাক্ট পেইজে](https://aiwithr.github.io/) যোগাযোগ করুন।

---

## 📄 লাইসেন্স (License)

এই রিপোজিটরির সমস্ত কোড ও স্ক্রিপ্ট [MIT License](LICENSE)-এর অধীনে মুক্তভাবে শিক্ষামূলক ও বাণিজ্যিক প্রজেক্টে ব্যবহারের জন্য উন্মুক্ত। বইটির লিখিত কনটেন্ট ও মেথডোলজির স্বত্ব রকিবুল হাসান সংরক্ষিত।
