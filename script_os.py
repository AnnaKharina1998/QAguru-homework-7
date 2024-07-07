import os.path
import shutil

CURRENT_FILE = os.path.abspath(__file__)

PROJECT_DIR = os.path.dirname(CURRENT_FILE)

if not os.path.exists("tmp"):
    os.mkdir("tmp")

TMP_DIR = os.path.join(PROJECT_DIR, "tmp")

TESTS_DIR = os.path.join(PROJECT_DIR, "tests")


