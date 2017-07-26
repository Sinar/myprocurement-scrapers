import requests_cache
import json
import logging
import os
from sys import argv

from myprocurement import MyProcurementPage

config_filename = argv[1]
with open(config_filename) as config_file:
    config = json.load(config_file)

logging.getLogger().setLevel(logging.INFO)
requests_cache.install_cache(config['project_name'])

os.makedirs("{}-html".format(config['project_name']), exist_ok=True)

page_num = 1
while True:
    page = MyProcurementPage(config['url'], page_num)
    logging.info("Saving page {}...".format(page.page_num))
    with open("{}-html/{}.html".format(config['project_name'], page.page_num), "w") as html_file:
        html_file.write(page.html)
    if page.is_last_page:
        break
    page_num += 1
