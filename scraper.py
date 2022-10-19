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

links= []
# def not_tip(href2):
#     return href2 and not re.compile("Синтетические").search(href2)


url = 'https://srv.oem.by/'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'lxml')
product_block = soup.select("#block-menu-menu-catalog")

# print(product_block)

for i in product_block:
    href = i.find_all('a', class_="nav-link dropdown-toggle")
    print(len(href))
    for z in range(1,3,1):
        for link in href:
            print(link)
            link="https://srv.oem.by" + link.get('href') +"?page={"+str(z)+"}"
            print(link)
            # links.append(link)
            # response = requests.get(link, verify=False)
            # soup = BeautifulSoup(response.text,'lxml')
            # product2_block = soup.select('#block-system-main > div > div.view-content > table > tbody')
# print(links)
print(len(links))
        # print(product2_block)
        # for j in product2_block:
        #     href2 = j.find_all('td', class_="views-field views-field-field-image")
        #     # print('1',href2)
        #     for link2 in href2:
        #         # link2= link2.get('href')
        #         print(link2)

# print(links)
