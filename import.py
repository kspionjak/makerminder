import yfinance as yf
import pandas as pd
import sqlite3 as sq
import sys

# AMZN
# META
# AAPL
# GOOG
# TSLA
# NFLX

mark = str(sys.argv[1])
prefix = "tbl_rq_"

if mark:
  # collecing stock information
  stock_mark = yf.Ticker(mark)
  data = stock_mark.history(period="3mo")

  sql_data = 'data.db'
  conn = sq.connect(sql_data)
  data.to_sql(prefix + str.lower(mark), conn, if_exists='replace', index=True)
  
  conn.close()
else:
  print("You didn't entered stock symbol!")