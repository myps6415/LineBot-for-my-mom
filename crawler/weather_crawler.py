import requests
from bs4 import BeautifulSoup

url = 'https://www.cwb.gov.tw/m/sv/ecardFB.php?ecls=5'

def every_city():
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup