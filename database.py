import sqlite3

def init_db():
    conn = sqlite3.connect("retail.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER,
            dwell_time REAL
        )
    """)

    conn.commit()
    conn.close()


def insert_data(person_id, dwell_time):
    conn = sqlite3.connect("retail.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO visitors VALUES (?, ?)",
                   (person_id, dwell_time))

    conn.commit()
    conn.close()
