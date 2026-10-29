"""
Forward Deployed Engineering (FDE) - Field Manual (Companion Codebase)
Author: Rakibul Hassan (https://aiwithr.github.io/)
Book Chapter: Chapter 2 - লোকাল আর্কিটেকচার ও এআই ইঞ্জিন
Book Reference URL: https://aiwithr.github.io/fde_book/chapter-2/
Repository: https://github.com/raqueeb/fdebook_companion
License: MIT

Description:
ক্লাউড বা ক্যাফকা ছাড়া অন-প্রেম সার্ভারে হাই-কনকারেন্সি প্রসেসিংয়ের জন্য
জিরো-ডিপেন্ডেন্সি SQLite WAL (Write-Ahead Logging) কিউ আর্কিটেকচার।
"""

import sqlite3
import os
import tempfile

def init_local_wal_queue(db_path: str = "fde_queue.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, timeout=10.0)
    # ১. WAL মোড চালু: রিড এবং রাইট একসাথে কোনো লক ছাড়াই চলবে
    conn.execute("PRAGMA journal_mode=WAL;")
    # ২. ডিস্ক সিঙ্ক অপ্টিমাইজেশন: ক্র্যাশ-সেফ থেকেও ৩ গুণ দ্রুত রাইট স্পিড
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("""CREATE TABLE IF NOT EXISTS ticket_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT, raw_msg TEXT, status TEXT DEFAULT 'PENDING'
    )""")
    return conn

if __name__ == "__main__":
    tmp_db = os.path.join(tempfile.gettempdir(), "fde_queue_demo.db")
    db = init_local_wal_queue(tmp_db)
    db.execute("INSERT INTO ticket_queue (raw_msg) VALUES (?)", ("চালানে ওজনের গরমিল",))
    mode = db.execute("PRAGMA journal_mode;").fetchone()[0]
    count = db.execute("SELECT count(*) FROM ticket_queue").fetchone()[0]
    print(f"Queue Mode: {mode.upper()} | Pending Tickets: {count}")
    db.close()
    for ext in ["", "-wal", "-shm"]:
        if os.path.exists(tmp_db + ext):
            os.remove(tmp_db + ext)
