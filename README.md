Python Info
-----------
- Developed in Python 3.6
- Tested working in Python 2.7

Usage
-----
1. Install requirements
1. Create a configuration file for the scraper, or use an existing one
1. Run `scrape.py your_config.json`
1. Output will be saved as `project_name.jsonl`

Configuration
-------------
Configuration is done via a JSON file. Several pre-made configuration files are provided in the `configs` directory. Below are the keys used:

- `project_name`: Filename (without extension) to be used for the output files
- `source_agency`: Value to be inserted into the `source_agency` field of the output
- `url`: URL to scrape
- `columns`: A list of dictionary keys corresponding to the columns of the table to be scraped

Caching
-------
Caching is transparently handled by the `requests-cache` module. Responses are cached in a SQLite database, and future requests will be retreived from that database, instead of over the Internet. The `cache.py` script is provided to interact with the cache.

`cache.py` is invoked the same way as `scrape.py`. If the pages are already in the cache, `cache.py` will retreive the pages from the cache and store them as HTML files in a folder named after the `project_name` setting. If the pages aren't in the cache, the pages will be downloaded and cached first, then stored as HTML files.
