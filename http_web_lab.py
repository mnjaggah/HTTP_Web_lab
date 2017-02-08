import requests
import json
"""this function allows one to specify the exchange rate base
as a parameter and a json object specifying the foreign exchange rates is returned
"""
def get_base(n):

	url = "http://api.fixer.io/latest?base="+n
	r = requests.get(url)
	return (r.json())
