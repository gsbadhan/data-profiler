from profiler.column_profiler import ColumnProfiler
from adapter.sqlite_adapter import SQLiteAdapter

def test_column_profile(sample_db):

    adapter = SQLiteAdapter(sample_db)

    config = {
        "sample_ratio": 1.0,
        "include_nulls": True
    }

    profiler = ColumnProfiler(adapter, config)

    result = profiler.profile("users", {
        "name": "age",
        "type": "INTEGER",
        "nullable": True
    })

    assert result["stats"]["min"] == 25