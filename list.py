import yfinance as yf
import pandas as pd
import sys

# AAPL
# AMZN
# META
# GOOG
# TSLA
# NFLX

mark = str(sys.argv[1])

if mark:
	mark_up = mark.upper()
	# stock_mark = yf.Ticker(mark_low)

	print(mark_up)

else:
	print("Error!")