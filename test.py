import sys
import yfinance as yf

if len(sys.argv) > 1:
  argm = str(sys.argv[1])
  argm_u = argm.upper()
  stock = yf.Ticker(argm_u)
  hist = stock.history(period="1mo")

  print(hist)
  
else:
  print("Please enter stock name as an argument!")