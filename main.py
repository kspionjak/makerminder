import sys
import pandas as pd
import yfinance as yf
import cherrypy

class StringGenerator(object):
	@cherrypy.expose
	def index(self):
		stock = yf.Ticker('GOOG')
		hist = stock.history(period="1mo")
		js_srt = pd.DataFrame.to_json(hist, orient='records', lines=True)
		return js_srt

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.sessions.on': True
		}
	}

	cherrypy.quickstart(StringGenerator(), '/', conf)
