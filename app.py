import requests
from lxml import html
import re
import pandas as pd


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


def load_webpage(page):
    path = "html_response\\page_%d.html" % page
    with open(path, 'r', encoding='utf8') as f:
        return html.fromstring(f.read())


def run():
    
    # Save all webpages
    # for page in range(1, 14):
        # save_webpages(page)
    
    # Parse webpages for "hospital name", "website link"
    # hospital_names = []
    # hospital_links = []
    
    # for page in range(1, 14):
    #     etree = load_webpage(page)
    #     hospital_titution_list_div = etree.xpath("//div[contains(@class, 'hospital-titution-list')]")[0]
    #     for h_li in hospital_titution_list_div.xpath("./ul/li"):
    #         try:
    #             hospital_name = h_li.xpath('.//h3/text()')[0]
    #             hospital_link = h_li.xpath('.//div[contains(@class, "hospital-titution-Information")]//a/@href')[0]
    #             hospital_names.append(hospital_name)
    #             hospital_links.append(hospital_link)
    #         except Exception as e:
    #             print(e)

    #     df = pd.DataFrame({
    #         'name': hospital_names,
    #         'link': hospital_links
    #     })   
    
    # df.to_csv('hospital_links.csv')
    # df.to_json('hospital_links.jsonl', orient='records', lines=True)

    # Test hospital links
    df = pd.read_csv("hospital_links.csv", header=0)
    for index, row in df.iterrows():
        name = row['name']
        link = row['link']
        try:
            resp = requests.get(link)
        except requests.ConnectionError as e:
            print(name, e)
        except requests.RequestException as e:
            print(name, e)
        except requests.HTTPError as e:
            print(name, e)

    return 


if __name__ == "__main__":
    run()