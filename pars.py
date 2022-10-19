import logging
import bs4
import requests
import certifi
import urllib3
import collections
import re



http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

urllib3.disable_warnings()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("oeml")

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand',
        'name',
        'url',
    ),
)

class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        self.result=[]

    def get_page(url, i):
        page = requests.get(url.__format__(i + 1))
        return page

    def main():
        i=0
        result=0
        url='https://srv.oem.by/products/brands/katalog/mannol?page={}'
        while True:
            page=get_page(url,i)
            if page.status_code !=200:
                break
            i+=1
            page_sum=sum(clean(read(page)))
            print(f'stranica #{i}', ':', page_sum)
            result+=page_sum
        print(result)




    def load_page(self):
        url = 'https://srv.oem.by/products/brands/katalog/mannol?page='
        res = self.session.get(url=url, verify=False)
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('tr.odd.views-row-first,tr.odd.views-row-last, tr.even,tr.odd')
            # '#block-system-main > div > div.view-content > table > tbody')
        for block in container:
            self.parse_block(block=block)
        print(len(container))

    def parse_block(self, block):
        # logger.info(block)
        # logger.info('='*100)

        url_block = block.find(href=re.compile("/content/"))
        # logger.info(url_block)
        if not url_block:
            logger.error('no url_block')
            return

        url = "https://srv.oem.by"+ url_block.get('href')
        if not url:
            logger.error('no href')
            return

        logger.info('%s',url)


    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

if __name__ == '__main__':
    parser = Client()
    parser.run()
    main()
    # parser = Client()
    # parser.run()

