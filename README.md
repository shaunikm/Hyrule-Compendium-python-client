<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" width="10%">
<h3 align="center">Python Package for the Hyrule Compendium API<h3>
<p align="center">This package comes with a few functions to help work with the Hyrule Compendium API and get all the data you want in a jiffy!</p>
</p>

### Project(s) Made With This
- [Hyrule Compendium Discord Bot](https://github.com/shaunikm/HyruleCompendium-Bot)

### Recommendation
It's recommended that you read the [API documentation](https://github.com/Hyrule-Compendium-API/Hyrule-Compendium-API/blob/master/README.md) before getting started.

### Installation
```
pip install HyruleCompendium
```

### Docs

#### `categoryList()`
\
**Use** \
Print out the list of valid categories in the API.

**Parameters** \
None

**Example** \
Call:
```python
list_of_categories = categoryList()
print(list_of_categories)
```
Output:
```python
["creatures", "equipment", "materials", "monsters", "treasure"]
```
---
#### `getCategory(categoryName)`
\
**Use** \
Gets all the JSON data from a valid category in the form of a python dictionary.

**Parameters**
- categoryName [type: string] - valid name of the category you want to fetch data from

**Raises**
 - *ValueError* - if <code>categoryName</code> is not valid

**Example** \
Call:
```python
from pprint import pprint
pprint(getCategory("monsters"))
```
---
#### `getEntry(entryName)`
\
**Use** \
Fetches data from a specific entry in the API.

**Parameters**
- entryName [type: string] - valid name of the entry you want to fetch data from

**Raises**
- *ValueError* - if <code>entryName</code> is not valid

**Example** \
Call:
```python
from pprint import pprint
pprint(getEntry("silver lynel"))
```
Output:
```python
{'category': 'monsters',
 'description': 'Silver Lynels are not to be trifled with. They have been '
                "influenced by Ganon's fiendish magic, so they are the "
                'strongest among the Lynel species, surpassing even the '
                'strength of those with white manes. The term "silver" denotes '
                'not only their color but also their rarity. The purple '
                'stripes help them to stand out even more.',
 'drops': ['lynel horn',
           'lynel hoof',
           'lynel guts',
           'topaz',
           'ruby',
           'sapphire',
           'diamond',
           'star fragment'],
 'id': 124,
 'name': 'silver lynel'}
```
---
#### `getAllData()`
\
**Use** \
Fetches all the data in the Hyrule Compendium API.

**Parameters** \
None

**Example**
```python
pprint(getAllData())
```

## Author
Made with awesomness by [@shaunikm](https://github.com/shaunikm).
