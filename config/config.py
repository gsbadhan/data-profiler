
""" configurations for SQLite """
sqlite_profiler = {
    "database": "employee.db",
    "sample_ratio": 1.0,    # 0 < x <= 1; how much % data you scan from a table
    "workers": 1,   # table scan parallelism; should be between 1 to 10
    "include_nulls": True,
    "include_histogram": True,
    "histogram_bins": 10,
    "output_filename":"output_sqlite_employeedb.json"   # start with prefix "output_"
}

""" configurations for Snowflake """
snowflake_profiler = {
    "database": "??",
    "sample_ratio": 1.0,    # 0 < x <= 1; how much % data you scan from a table
    "workers": 10,  # table scan parallelism; should be between 1 to 10
    "include_nulls": True,
    "include_histogram": True,
    "histogram_bins": 10,
    "output_filename":"output_??.json"  # start with prefix "output_"
}

""" configurations for Databrick """
snowflake_profiler = {
    "database": "??",
    "sample_ratio": 1.0,    # 0 < x <= 1; how much % data you scan from a table
    "workers": 10,  # table scan parallelism; should be between 1 to 10
    "include_nulls": True,
    "include_histogram": True,
    "histogram_bins": 10,
    "output_filename":"output_??.json"  # start with prefix "output_"
}

