import csv
import re
import pandas as pd
import lxml
import ssl
import urllib3
import certifi
import requests
from bs4 import BeautifulSoup

urllib3.disable_warnings()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

a = int(input('Сколько страниц: '))
# a=1
links= []
result_list = []



for o in range(1,a+1,1):
    url = "https://srv.oem.by/products/brands/katalog/mannol"+"?page="+str(o)
    print(url)
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    product_block = soup.select("#block-system-main > div > div.view-content > table > tbody")
    # print(product_block)
    for i in product_block:
        href = i.find_all(href=re.compile("/content/"))
            # ('td', class_="views-field views-field-rendered-entity-1")
        for link in href:
            link2 = "https://srv.oem.by"+link.get('href')
            links.append(link2)
            # print(link)
    # print(links)
links2=tuple(set(links))
# print(*links2,sep='\n')
print(len(links2))

for link2 in links2:
    # print(link2)
    response = requests.get(link2, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')

    h1=soup.h1.string
    # print(h1)

    product_block2 = soup.select("#block-system-main")
    # print(product_block2)
    opis= soup.find('div', class_="col-12 mt-40")
    opis=opis.get_text(strip=True)
    # print(opis)

    kol = soup.find('span', class_="stock-value")
    kol = kol.get_text(strip=True)
    # print(kol)

    art = soup.find('div', class_="col-12 pt-10 commerce-product-sku")
    art = art.get_text(strip=True)
    # print(art)

    tip = soup.find('div', class_="field field-name-field-catalog field-type-taxonomy-term-reference field-label-hidden")
    tip = tip.get_text(strip=True)
    # print(tip)

    price = soup.find('div', class_="row no-gutters price-row")
    price = price.get_text(strip=True)
    # print(price)

    img = soup.find('img', class_="img-responsive")
    img= img.get('src')
    # print(img)

    brend = soup.find('div', class_="field field-name-field-brand field-type-taxonomy-term-reference field-label-hidden")
    brend = brend.get_text(strip=True)
    # print(brend)

    vid = soup.find('div', class_="field field-name-field-kind field-type-taxonomy-term-reference field-label-hidden")
    vid = vid.get_text(strip=True)
    # print(vid)

    result_list.append(
        {
            'h1':h1,
            'brend': brend,
            'vid': vid,
            'img': img,
            'price': price,
            'tip': tip,
            'art': art,
            'kol': kol,
            'opis': opis
        }
    )
    # result_list['h1'].append(h1)
    # result_list['brend'].append(brend)
    # result_list['vid'].append(vid)
    # result_list['img'].append(img)
    # result_list['price'].append(price)
    # result_list['tip'].append(tip)
    # result_list['art'].append(art)
    # result_list['kol'].append(kol)
    # result_list['opis'].append(opis)

    # print(result_list)
with open('data.csv', 'w', newline='',encoding="utf-8") as f:
    # names = ['Название', 'Описание', 'Картинка', 'Количество', 'Цена', 'Артикул', 'Тип', 'Вид', 'Бренд']
    f_writer = csv.writer(f, delimiter=";")
    f_writer.writerow(['Название','Бренд','Вид','Картинка','Цена','Тип','Артикул','Количество','Описание'])
    for item in result_list:
        f_writer.writerow([item['h1'],item['brend'],item['vid'],item['img'],item['price'],item['tip'],item['art'],item['kol'],item['opis']])

# print(result_list)







