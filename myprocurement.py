import requests
from bs4 import BeautifulSoup, Comment
import re
import logging

class MyProcurement:
    def __init__(self, url, start_page=1):
        self.url = url
        self.page_num = start_page

    def get_rows(self):
        while True:
            logging.info("Processing page {}...".format(self.page_num))
            page = MyProcurementPage(self.url, self.page_num)
            for row in page.get_rows():
                yield row, page.url
            if page.is_last_page:
                break
            self.page_num += 1

class MyProcurementPage:
    def __init__(self, base_url, page_num):
        self.base_url = base_url
        self.page_num = page_num
        self._scrape_page()

    def _get_page(self):
        query = {'page': self.page_num}
        response = requests.get(self.base_url, query)
        self.url = response.url
        return response.text

    def _scrape_page(self):
        page = self._get_page()
        soup = BeautifulSoup(page, 'lxml')

        # Find table with data
        main_table = soup.find("table", bordercolor="#000000")
        self._rows = main_table.find_all("tr", recursive=False)[1:]

        # Find "Akhir" link to determine if last page
        last_page_text = soup.find(string=re.compile(r"Akhir"))
        last_page_button = last_page_text.find_parent("a")
        self.is_last_page = last_page_button is None

    def get_rows(self):
        for row in self._rows:
            tds = row.find_all("td", recursive=False)
            data = [br_to_newlines(td) for td in tds]
            yield data

def br_to_newlines(element):
    text = ""
    for elem in element.recursiveChildGenerator():
        if not isinstance(elem, Comment) and isinstance(elem, str):
            text += elem.strip()
        elif elem.name == "br":
            text += "\n"
    return text.strip()
