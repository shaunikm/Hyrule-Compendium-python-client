import requests
import json

class compendium(object):
    def __init__(self, url="https://botw-compendium.herokuapp.com/api/v1"):
        self.url = url

    def categoryList(self):
        return ["creatures", "equipment", "materials", "monsters", "treasure"]

    def getCategory(self, categoryName: str):
        categoryData = requests. \
            get(f"{self.url}/category/{categoryName.lower()}"). \
            json()
        return categoryData["data"]

    def getEntry(self, entry):
        try:
            target = entry.replace(" ", "%20").lower()
        except:
            target = entry
        try:
            entryData = requests. \
                get(f"{self.url}/entry/{target}"). \
                json()
        except json.decoder.JSONDecodeError:
            raise ValueError("Invalid entry.")

        return entryData["data"]

    def getAllData(self):
        allData = requests. \
            get(self.url). \
            json()

        return allData["data"]