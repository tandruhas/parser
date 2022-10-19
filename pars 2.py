import logging
import bs4
import requests
import certifi
import urllib3
import collections
import re

HOST='https://srv.oem.by'
URL='https://srv.oem.by/products/brands/katalog/mannol?page='
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

urllib3.disable_warnings()

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger("oeml")

def get_html(url,params=''):
    r= requests.get(url, headers=HEADERS,params=params, verify=False)
    return r

def get_stranic(html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    items = soup.select('tr.odd.views-row-first,tr.odd.views-row-last, tr.even,tr.odd')
    cards=[]
    # print(items)

    for item in items:
        url_st = HOST + item.find(href=re.compile("/content/")).get('href')
        # print(url_st)
    # print(len(items))

    return url_st

def get_content(url_st):
    print(url_st)
    # response = requests.get(url_st, verify=False)
    # soup = bs4.BeautifulSoup(url_st, 'lxml')
    # product_block2 = soup.select("#block-system-main")
    # # print(product_block2)
    # opis = soup.find('div', class_="col-12 mt-40")
    #
    # print(product_block2)
    return



def parser():
    # PAGINATION = input('str: ')
    PAGINATION= 2
        # int(PAGINATION.strip())
    html=get_html(URL)

    for page in range(1,PAGINATION+1):
        print(f'parsim stranicy: {page}')
        html= get_html(URL,params={'page': page})
        get_stranic(html.text)
        url_st = get_stranic(html.text)
        get_content(url_st)



parser()


