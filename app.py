import requests
from lxml import html
import re


def save_webpages(page):
    URL = "https://www.medicaltravel.org.tw/Hospital-List.aspx?position=0&l=2&p=%d&name=&meds=" % page
    resp = requests.get(
        url = URL,
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }
    )
    with open("html_response\\page_%d.html" % page, "w", encoding="utf8") as f:
        f.write(resp.text)


def run():
    for page in range(1, 14):
        save_webpages(page)
    return 


if __name__ == "__main__":
    run()