import requests_cache
import json
import logging

from myprocurement import MyProcurement

PROJECT_NAME = "keputusan_rundingan"
SOURCE_AGENCY = "treasury"
URL = "http://myprocurement.treasury.gov.my/custom/p_keputusan_rundingan.php"
COLUMNS = ["id", "title", "category", "ministry", "agency", "company", "value", "criteria", "date"]

logging.getLogger().setLevel(logging.INFO)
requests_cache.install_cache(PROJECT_NAME)

scraper = MyProcurement(URL)
jsonl_file = open("{}.jsonl".format(PROJECT_NAME), "w")

for row, url in scraper.get_rows():
    data = dict(zip(COLUMNS, row))
    data['source_url'] = url
    data['source_agency'] = SOURCE_AGENCY
    jsonl = json.dumps(data)
    jsonl_file.write(jsonl)
    jsonl_file.write("\n")
