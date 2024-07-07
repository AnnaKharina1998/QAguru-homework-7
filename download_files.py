import os
import requests
from selene import query, browser, command

from script_os import TMP_DIR


def download_file(file_format):
    browser.open('/')
    browser.element(f"//a[descendant::p[text()='{file_format.upper()}']]").perform(command.js.scroll_into_view).click()
    download_url = browser.element(f"[title = 'Скачать example.{file_format.lower()}']").get(query.attribute("href"))
    content = requests.get(url=download_url).content
    with open(os.path.join(TMP_DIR, f"example.{file_format.lower()}"), 'wb') as file:
        file.write(content)
    browser.quit()

def download_files(*args):
    for file_format in args:
        download_file(file_format)
