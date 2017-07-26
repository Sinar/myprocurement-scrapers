import requests_cache
import json
import logging
import sys

from myprocurement import MyProcurement

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} config_file.json\n".format(sys.argv[0]))
    sys.exit()

config_filename = sys.argv[1]
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
