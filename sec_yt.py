import requests
import pandas as pd
import time
import matplotlib.pyplot as plt

headers = {'User-Agent': 'youremail@gmail.com'}

tickers = requests.get("https://www.sec.gov/files/company_tickers.json")
tickers = pd.json_normalize(pd.json_normalize(tickers.json(), max_level=0).values[0])
tickers['cik_str'] = 'CIK000' + tickers['cik_str'].astype(str)