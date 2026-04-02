from adapter.sqlite_adapter import SQLiteAdapter

def test_list_tables(sample_db):
    adapter = SQLiteAdapter(sample_db)
    tables = adapter.list_tables()

    assert "users" in tables