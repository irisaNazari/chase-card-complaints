import sys
import pandas as pd
import duckdb

print(sys.executable)
print("pandas", pd.__version__)
print("duckdb", duckdb.__version__)
print(duckdb.sql("SELECT 42 AS answer").df())