import requests_cache
import json
import logging
from sys import argv

from myprocurement import MyProcurement

config_filename = argv[1]
with open(config_filename) as config_file:
    config = json.load(config_file)

logging.getLogger().setLevel(logging.INFO)
requests_cache.install_cache(config['project_name'])

scraper = MyProcurement(config['url'])
jsonl_file = open("{}.jsonl".format(config['project_name']), "w")

for row, url in scraper.get_rows():
    data = dict(zip(config['columns'], row))
    data['source_url'] = url
    data['source_agency'] = config['source_agency']
    jsonl = json.dumps(data)
    jsonl_file.write(jsonl)
    jsonl_file.write("\n")
