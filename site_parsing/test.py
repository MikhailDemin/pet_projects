import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import lxml

URL = "https://www.kinopoisk.ru/lists/movies/top250/"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
req = requests.get(URL, headers = headers)
# req = requests.get(URL)
print(req.status_code)

print(req.text)