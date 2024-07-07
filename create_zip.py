from script_os import TMP_DIR, PROJECT_DIR
import shutil
import os.path


def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    shutil.make_archive(name, format, source)
    shutil.move('%s.%s' % (name, format), destination)

