<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" width="10%">
</p>
<h3 align="center">The official python wrapper for the Hyrule Compendium API, forked from the unnoficial [shaunikm/Hyrule-Compendium-python-client](shaunikm/Hyrule-Compendium-python-client).</h3>

It's recommended that you read the [API documentation](https://github.com/gadhagod/Hyrule-Compendium-API/blob/master/README.md) before getting started.

### Installation
```shell
pip3 install git+https://github.com/gadhagod/pyrule-compendium =
```
PyPi package coming soon.

### Docs

All functions are attributes of class `compendium`.
 
---

#### `getCategory(category)`
Get all entries in a category.

**Parameters**
- category [type: string] - name of category

**Example** \
Call:
```python
print(getCategory("monsters"))
```
---
#### `getEntry(entry)`
Get an entry.
**Parameters**
- entry [type: string, int] - name or ID of entry

**Example** \
Call:
```python
print(getEntry("silver lynel"))
```
---
#### `getAll()`
Get all data.

**Parameters** \
None

### Hosting locally
You can configure the URL to make requests to by setting the `compendium` class parameter `url`. 
See [here](https://github.com/gadhagod/Hyrule-Compendium-API) to host the API locally.

### Shoutouts
Thanks to [@shaunikm](https://github.com/shaunikm) for the original code.