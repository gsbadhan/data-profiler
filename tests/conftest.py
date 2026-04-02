import pytest
import sqlite3

@pytest.fixture
def sample_db():
    db_path = "unit_testing.db"
    conn = sqlite3.connect(db_path)

    try:
        conn.execute("""CREATE TABLE users (
            id INTEGER,
            age INTEGER,
            salary REAL
        )""")

        conn.executemany(
            "INSERT INTO users VALUES (?, ?, ?)",
            [
                (1, 25, 50000),
                (2, 30, 60000),
                (3, None, 70000),
            ]
        )

        conn.commit()
    except Exception as e:
        print(e) 
    finally:
        conn.close()

    return str(db_path)