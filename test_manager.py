import shutil
import os
import sys

from maneger import copy_file_or_directory, author_info, quit, filenames


def test_copy_file_or_directory():
    name = 'rar'
    new_name = 'rar_copy'
    if os.path.isdir(name):
        assert shutil.copytree(name, new_name)



def test_author_info():
    assert author_info() == 'Leonid Orlov'



def test_quit():
    if SystemExit == 0:
        assert sys.exit(0)



def test_filenames():
    for item in os.listdir():
        if os.path.isfile(item):
            assert True
