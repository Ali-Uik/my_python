import requests
import json
from pprint import pprint

with open('comments.json', mode='w', encoding='utf-8') as file:
    json_data = []
    main_data = requests.get('https://jsonplaceholder.typicode.com/comments').json()
    for item in main_data:
        pprint(item['body'])


