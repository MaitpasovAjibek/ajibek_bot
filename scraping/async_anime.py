from parsel import Selector
import requests
import httpx
import asyncio
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

    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def parse_data(self):
        async with httpx.AsyncClient(headers=self.headers) as client:
            async for page in self.async_generator(limit=5):
                data = await self.get_url(client=client,url=self.MAIN_URL.format(page=page))
                return data

    async def scrape_responses(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.X_PATH).extract()
        for link in links:
            print("PLUS_URL: ", self.PLUS_URL + link)
        return links


if __name__ == '__main__':
    scraper = AnimeScraper
    scraper.parse_data()
