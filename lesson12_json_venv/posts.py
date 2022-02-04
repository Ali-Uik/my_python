import requests
import json
from pprint import pprint


file = open('posts.json', mode='w', encoding='utf-8')
json_data = []


posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
pprint(posts)
for post in posts:
    # pprint(post['id'])
    if post['id'] % 2 == 0:
        json_data.append({post['id']: post['body']})
# pprint(json_data)
json.dump(json_data, file, indent=4, ensure_ascii=False)

file.close()
