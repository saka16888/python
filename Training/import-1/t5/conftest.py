import pytest
import tempfile
import os

@pytest.fixture(scope="module")
def cleandir():
    newpath = tempfile.mkdtemp()
    print("newpath : ",newpath)
    os.chdir(newpath)
