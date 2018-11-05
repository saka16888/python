# content of test_mark.py
# 
# pytest -v -m webtest
# pytest -v -m "not webtest"
# 2-v ID py.test -v test_server.py::TestClass::test_method 
# 3-k  py.test -v -k http  py.test -k "not send_http" -v

import pytest
@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app
    
def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_1(self):
        pass
    def test_2(self):
        pass        