import yfinance as yf

aapl = yf.Ticker("AAPL")
hist = aapl.history(period="1mo")

print(hist)