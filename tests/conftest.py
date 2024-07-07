import pytest
import os.path
from selene import browser
from script_os import TMP_DIR, PROJECT_DIR
from download_files import download_files
from create_zip import make_archive


@pytest.fixture(scope='session',  autouse=True)
def make_an_archive_to_test():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.base_url = 'https://www.online-convert.com/ru/file-type'
    download_files('pdf', 'csv', 'xlsx') # скачиваем примеры файлов
    make_archive(TMP_DIR, os.path.join(PROJECT_DIR, "tmp_archive.zip")) #создаём архив в корневой папке проекта

