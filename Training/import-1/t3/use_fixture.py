# content of test_setenv.py
import os
import pytest
 
@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        print("call test_cwd_starts_empty")
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")
 
    def test_cwd_again_starts_empty(self):
        print("call test_cwd_again_starts_empty")
        assert os.listdir(os.getcwd()) == []