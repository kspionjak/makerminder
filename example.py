import yfinance as yf

goog = yf.Ticker("GOOG")
hist = goog.history(period="1mo")

print(hist)