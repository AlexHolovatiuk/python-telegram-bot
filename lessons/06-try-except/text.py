import json

import text

data = {
    'name': 'Sasha',
    'city': 'K-P',
    'hobbies': ['walking']
}

with open('json.txt', 'w') as file:
    json.dump(data, file)

with open('json.txt', 'r') as file:
    text_data = json.load(file)
    print(text_data)