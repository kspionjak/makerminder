import yfinance as yf
import pandas as pd
import sqlite3 as sq

# collecting stock information
aapl = yf.Ticker("AAPL")
data = aapl.history(period="1mo")

sql_data = 'data.db'
conn = sq.connect(sql_data)

data.to_sql('tbl_records', conn, if_exists='replace', index=True)

conn.close()