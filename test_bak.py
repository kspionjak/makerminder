import yfinance as yf
import pandas as pd
import sqlite3 as sq

# collecting stock information
aapl = yf.Ticker("AAPL")
data = aapl.history(period="1mo")

sql_data = 'data.db'
conn = sq.connect(sql_data)
data.to_sql('tbl_records', conn, if_exists='append', index=True)

cur = conn.cursor()
cur.execute("SELECT * FROM tbl_records LIMIT 10")
rows = cur.fetchall()

for row in rows:
  print(row)

conn.close()