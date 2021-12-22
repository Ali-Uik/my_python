from bs4 import BeautifulSoup
import requests
from configs import *


class BaseParser:
    def __init__(self):
        self.URL = URL
        self.HOSTS = HOSTS

    def get_html(self, url):
        response = requests.get(url)
        return response.text



