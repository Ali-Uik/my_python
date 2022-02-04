from bs4 import BeautifulSoup


# Миксин это - не самостоятельный класса который реалезует одну или несколько задач
class ProductDetailParserMixin:
    def get_detail_info(self, page):
        characteristics = {}
        soup = BeautifulSoup(page, 'html.parser')
        blocks = soup.find_all('div', class_='characteristic__item')
        for block in blocks:
            block_title = block.find('div', class_='title').get_text(strip=True)
            print(block_title)
        return characteristics
