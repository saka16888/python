# content of conftest.py
 
import pytest
import tempfile
import os
 
@pytest.fixture()
def cleandir():
    print("\ncall cleandir ")
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    