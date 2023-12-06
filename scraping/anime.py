from parsel import Selector
import requests

class AnimeScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://animevost.tv/',
        'Connection': 'keep-alive',
               }


    MAIN_URL = 'https://animevost.tv/'
    X_PATH = '//div[@class="kino-item ignore-select"]/div/a/@href'
    PLUS_URL = 'https://animevost.tv'
    def parse_data(self):
        html = requests.get(url=self.MAIN_URL, headers=self.headers).text
        # print(html)
        tree = Selector(text=html)
        link = tree.xpath(self.X_PATH).extract
        print(link)
        for links in link:
            print(self.PLUS_URL + links)
        return link[:5]



if __name__ == '__main__':
    scraper = AnimeScraper
    scraper.parse_data()
