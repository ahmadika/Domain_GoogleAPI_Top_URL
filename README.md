# Domain Relevant Data Collection using Google Search API 

#### Objective

This project uses Google Search API to provide a list of most occurred urls based on domain keywords and phrases list. The code generates the phrases first based on the provided keywords and then uses them for searching. After each search, top 10 urls(or all active & working URLs from the first page) are considered and added to a dictionary. Iterating through all keywords, the dictionary is finally sorted based on the frequency of occurrence.

#### Install Google Search API
Using Google's Search API, we feed it with keywords and phrases and pick the top 10 results (or 1st page results) and build a URL pool

``` $ pip install git+https://github.com/abenassi/Google-Search-API/```

#### Run gSearch.py

```
$ cd Google-Search-API

$ python gSearch.py
```
