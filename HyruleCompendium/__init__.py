import requests
import json

class compendium(object):
    def __init__(self, url="https://botw-compendium.herokuapp.com/api/v1"):
        self.url = url

    def categoryList(self):
        return ["creatures", "equipment", "materials", "monsters", "treasure"]

    def getCategory(self, categoryName: str, timeout=None):
        categoryData = requests. \
            get(f"{self.url}/category/{categoryName.lower()}", timeout=timeout). \
            json()
        return categoryData["data"]

    def getEntry(self, entry, timeout=None):
        try:
            target = entry.replace(" ", "%20").lower()
        except:
            target = entry
        try:
            entryData = requests. \
                get(f"{self.url}/entry/{target}", timeout=timeout). \
                json()
        except json.decoder.JSONDecodeError:
            raise ValueError("Invalid entry.")

        return entryData["data"]

    def getAll(self, timeout=None):
        allData = requests. \
            get(self.url, timeout=timeout). \
            json()

        return allData["data"]