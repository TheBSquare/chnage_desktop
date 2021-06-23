import json
from random import choice
from os import system
from settings import images_json_path, update_json_path


def update_json_images():
    system('scrapy crawl main -O json/update_data.json')


def get_random():
    with open(images_json_path, 'r') as file:
        data = json.load(file)
        obj = choice(data)
        return obj


def get_by_key_name(key):
    with open(images_json_path, 'r') as file:
        temp = []
        data = json.load(file)
        for obj in data:
            if key in obj['keys']:
                temp.append(obj)
    try:
        return choice(temp)
    except IndexError:
        return None


def merge_jsons():
    with open(update_json_path, 'r') as file:
        new_data = json.load(file)
        file.close()

    with open(images_json_path, 'r') as file:
        data = json.load(file)
        file.close()

    with open(images_json_path, 'w') as file:
        for chunk in new_data:
            if not chunk in data:
                data.append(chunk)
        json.dump(data, file)
        file.close()
