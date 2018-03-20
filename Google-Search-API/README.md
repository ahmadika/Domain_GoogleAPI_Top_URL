
Google Search API
=====

[![Coverage Status](https://coveralls.io/repos/abenassi/Google-Search-API/badge.svg?branch=master)](https://coveralls.io/r/abenassi/Google-Search-API?branch=master)
[![Build Status](https://travis-ci.org/abenassi/Google-Search-API.svg?branch=master)](https://travis-ci.org/abenassi/Google-Search-API)
[![](https://img.shields.io/pypi/v/Google-Search-API.svg)](https://pypi.python.org/pypi/Google-Search-API)

*The original package was developed by Anthony Casagrande and can be downloaded at https://github.com/BirdAPI This is a forked package that I will continue maintaining in the foreseeable future. I will try to maintain a strongly modularized design so when something is broken anyone can quickly repair it. All contributions are very welcome.*

Google Search API is a python based library for searching various functionalities of google.  It uses screen scraping to retrieve the results, and thus is unreliable if the way google's web pages are returned change in the future. This package is currently under heavy refactoring so changes in the user interface should be expected for the time being.

*Disclaimer: This software uses screen scraping to retrieve search results from google.com, and therefore this software may stop working at any given time.  Use this software at your own risk. I assume no responsibility for how this software API is used by others.*

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Google Search API
](#google-search-api)
  - [Development current status
](#development-current-status)
  - [Installation
](#installation)
  - [Google Web Search](#google-web-search)
  - [Google Calculator](#google-calculator)
  - [Google Image Search](#google-image-search)
  - [Google Currency Converter (Exchange Rates)](#google-currency-converter-exchange-rates)
  - [Contributions](#contributions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Development current status
--------------------------

All methods are currently functioning and returning its primary target data. Although, some of the secondary data that is supposed to be collected in the result objects is not yet working.

Redesign of the package is still a work in progress. After completed, I will attempt to repair the gathering of secondary data. Contributions are welcome!

Installation
------------

The repo is structured like a package, so it can be installed from pip using
github clone url. From command line type:

```
pip install Google-Search-API
```

To upgrade the package if you have already installed it:

```
pip install Google-Search-API --upgrade
```

Please note that you should also install **Firefox browser** in order to use images search.

You could also just download or clone the repo and import the package from
Google-Search-API folder.

```python
import os
os.chdir("C:\Path_where_repo_is")
from google import google
```

## Google Web Search
You can search google web in the following way:

```python
from google import google
num_page = 3
search_results = google.search("This is my query", num_page)
```

`search_results` will contain a list of `GoogleResult` objects. num_page parameter is optional (default is 1 page)

```python
GoogleResult:
    self.name # The title of the link
    self.link # The external link
    self.google_link # The google link
    self.description # The description of the link
    self.thumb # The link to a thumbnail of the website (NOT implemented yet)
    self.cached # A link to the cached version of the page
    self.page # What page this result was on (When searching more than one page)
    self.index # What index on this page it was on
```

*Description text parsing has some encoding problems to be resolved.*
*Only google link of the search is being parsed right now, parse the external link is an implementation priority.*


## Google Calculator
Attempts to search google calculator for the result of an expression. Returns a `CalculatorResult` if successful or `None` if it fails.

```python
from google import google
google.calculate("157.3kg in grams")
```

```python
CalculatorResult
    value = None  # Result value (eg. 157300.0)
    from_value = None  # Initial value (eg. 157.3)
    unit = None  # Result unit (eg. u'grams') (NOT implemented yet)
    from_unit = None  # Initial unit (eg. u'kilograms') (NOT implemented yet)
    expr = None  # Initial expression (eg. u'157.3 grams') (NOT implemented yet)
    result = None  # Result expression  (eg. u'157300 kilograms') (NOT implemented yet)
    fullstring = None  # Result unit (eg. u'157.3 kilograms = 157300 grams') (NOT implemented yet)
```

*Parsing of the units must be implemented. The rest of the data members of CalculatorResult can be build from the values and units of the calculation.*

## Google Image Search
Searches google images for a list of images. Image searches can be filtered to produce better results. Image searches can be downloaded.

### Requirement
Image search uses the selenium & the Firefox driver, therefor you MUST have [Firefox installed](https://www.mozilla.org/en-US/firefox/new/) to use it.

Perform a google image search on "banana" and filter it:

```python
from google import google, images
options = images.ImageOptions()
options.image_type = images.ImageType.CLIPART
options.larger_than = images.LargerThan.MP_4
options.color = "green"
results = google.search_images("banana", options)
```

Sample Result:

```python
{'domain': 'shop.tradedoubler.com',
 'filesize': None,
 'format': None,
 'height': '2000',
 'index': 15,
 'link': 'http://tesco.scene7.com/is/image/tesco/210-8446_PI_1000013MN%3Fwid%3D2000%26hei%3D2000',
 'name': None,
 'page': 1,
 'site': 'http://shop.tradedoubler.com/shop/uk-01/a/2058674/productName/banana/sortBy/price/sortReverse/false',
 'thumb': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS8JPH_bgyvvyf5X67k32ZZYjf9MlWlxHIEXXxi91TVrNafpokI',
 'thumb_height': '199px',
 'thumb_width': '199px',
 'width': '2000'}
```

*filesize is to be implemented. format works, but sometimes the link of the image doesn't show the format. Google images right now seems to not have a names, so the method for that is not implemented.*

Filter options:

```python
ImageOptions:
    image_type  # face, body, clipart, line drawing
    size_category  # large, small, icon
    larger_than  # the well known name of the smallest image size you want
    exact_width  # the exact width of the image you want
    exact_height  # the exact height of the image you want
    color_type  # color, b&w, specific
    color  # blue, green, red
```

Enums of values that can be used to filter image searches:

```python
class ImageType:
    NONE = None
    FACE = "face"
    PHOTO = "photo"
    CLIPART = "clipart"
    LINE_DRAWING = "lineart"

class SizeCategory:
    NONE = None
    ICON = "i"
    LARGE = "l"
    MEDIUM = "m"
    SMALL = "s"
    LARGER_THAN = "lt"
    EXACTLY = "ex"

class LargerThan:
    NONE = None
    QSVGA = "qsvga" # 400 x 300
    VGA = "vga"     # 640 x 480
    SVGA = "svga"   # 800 x 600
    XGA = "xga"     # 1024 x 768
    MP_2 = "2mp"    # 2 MP (1600 x 1200)
    MP_4 = "4mp"    # 4 MP (2272 x 1704)
    MP_6 = "6mp"    # 6 MP (2816 x 2112)
    MP_8 = "8mp"    # 8 MP (3264 x 2448)
    MP_10 = "10mp"  # 10 MP (3648 x 2736)
    MP_12 = "12mp"  # 12 MP (4096 x 3072)
    MP_15 = "15mp"  # 15 MP (4480 x 3360)
    MP_20 = "20mp"  # 20 MP (5120 x 3840)
    MP_40 = "40mp"  # 40 MP (7216 x 5412)
    MP_70 = "70mp"  # 70 MP (9600 x 7200)

class ColorType:
    NONE = None
    COLOR = "color"
    BLACK_WHITE = "gray"
    SPECIFIC = "specific"

class License:
    NONE = None
    REUSE = "fc"
    REUSE_WITH_MOD = "fmc"
    REUSE_NON_COMMERCIAL = "f"
    REUSE_WITH_MOD_NON_COMMERCIAL = "fm"
```

You can download a list of images.

```python
images.download(image_results, path = "path/to/download/images")
```

Path is an optional argument, if you don't specify a path, images will be downloaded to an "images" folder inside the working directory.

If you want to download a large list of images, the previous method could be slow. A better method using multithreading is provided for this case.

```python
images.fast_download(image_results, path = "path/to/download/images", threads=12)
```

You may change the number of threads, 12 is the number that has offered the best speed after a number of informal tests that I've done.

## Google Currency Converter (Exchange Rates)
Convert between one currency and another using google calculator. Results are real time and can change at any time based on the current exchange rate according to google.

Convert 5 US Dollars to Euros using the official 3 letter currency acronym ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)):

```python
from google import google
euros = google.convert_currency(5.0, "USD", "EUR")
print "5.0 USD = {0} EUR".format(euros)
```

```python
5.0 USD = 3.82350692 EUR
```

Convert 1000 Japanese Yen to US Dollars:

```python
yen = google.convert_currency(1000, "yen", "us dollars")
print "1000 yen = {0} us dollars".format(yen)
```

```python
1000 yen = 12.379 us dollars
```

Instead you can get the exchange rate which returns what 1 `from_currency` equals in `to_currency` and do your own math:

```python
rate = google.exchange_rate("dollars", "pesos")
print "dollars -> pesos exchange rate = {0}".format(rate)
```

```python
dollars -> pesos exchange rate = 13.1580679
```

Perform your own math. The following 2 statements are equal:

```python
5.0 * google.exchange_rate("USD", "EUR")
```

```python
google.convert_currency(5.0, "USD", "EUR")
```

As a side note, `convert_currency` is always more accurate than performing your own math on `exchange_rate` because of possible rounding errors. However if you have more than one value to convert it is best to call `exchange_rate` and cache the result to use for multiple calculations instead of querying the google server for each one.


## Contributions

All contributions are very welcome! As you have seen, there is still some methods that are not implemented. The structure of the package is intended to facilitate that you can contribute implementing or improving any method without changing other code.

Other interesting things that you may do is to build a good command line interface for the package. You can also take a look to the [TODO list](https://github.com/abenassi/Google-Search-API/blob/master/TODO.md)

For all contributions, we intend to follow the [Google Ptyhon Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
