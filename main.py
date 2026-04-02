from adapter.sqlite_adapter import SQLiteAdapter
from profiler.table_profiler import TableProfiler
from persistence.writer import JsonWriter
from config.config import sqlite_profiler
import logging 

logging.basicConfig(level=logging.INFO)

def startup_message():
    logging.info("welcome to data-profiler app !!")
    logging.info(f"configurations sqlite-profiler={sqlite_profiler}")


def run_sqlite():
    logging.info(f"sqlite data profiling started for DB={sqlite_profiler['database']}...")
    adapter = SQLiteAdapter(sqlite_profiler['database'])
    profiler = TableProfiler(adapter, sqlite_profiler)
    results = profiler.run()
    JsonWriter().write(results, sqlite_profiler['output_filename'])
    logging.info(f"sqlite data profiling completed for DB={sqlite_profiler['database']}, file generated={sqlite_profiler['output_filename']}")


if __name__ == "__main__":
    startup_message()
    run_sqlite()

