# FDE On-Prem Engine: Zero-Dependency SQLite WAL Concurrent Queue
import sqlite3, os, tempfile

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
