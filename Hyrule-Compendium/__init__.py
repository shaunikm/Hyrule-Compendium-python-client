import requests
from pprint import pprint
import json


def categoryList():
    return ["creatures", "equipment", "materials", "monsters", "treasure"]


def getCategory(categoryName: str):
    if categoryName.lower() in categoryList():
        categoryData = requests. \
            get(f"https://botw-compendium.herokuapp.com/api/v1/category/{categoryName.lower()}"). \
            json()
    else:
        raise ValueError("Invalid category. Run categoryList() for a list of valid categories.")

    return categoryData["data"]


def getEntry(entryName: str):
    entryName.replace(" ", "%20")
    try:
        entryData = requests. \
            get(f"https://botw-compendium.herokuapp.com/api/v1/entry/{entryName.lower()}"). \
            json()
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid entry.")

    return entryData["data"]


def getAllData():
    allData = requests. \
        get("https://botw-compendium.herokuapp.com/api/v1"). \
        json()

    return allData["data"]
