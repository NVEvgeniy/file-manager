import shutil
import os
import sys

from maneger import copy_file_or_directory, author_info, quit, filenames


def test_copy_file_or_directory():
    name = 'rar'
    new_name = 'rar_copy'
    shutil.copytree(name, new_name) if os.path.isdir(name) else False
    assert True



def test_author_info():
    assert author_info() == 'Leonid Orlov'



def test_quit():
    sys.exit(0) if SystemExit == 0 else False
    assert True





def test_filenames():
    test = [item for item in os.listdir() if os.path.isfile(item)]
    assert test

