from os import path
import random
import json


def search():
    joke_data_path = path.join(path.abspath(path.dirname(__file__)), "data", "tl.json")

    with open(joke_data_path, encoding="UTF-8") as data_file:
        data = json.load(data_file)

    return{
        "text": data[random.randint(0, len(data) - 1)]
    }
