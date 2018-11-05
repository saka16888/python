import pytest
  
@pytest.fixture()
def setup():
    print('\ndata "setup"')
 
@pytest.fixture()
def setup2():
    print('\ndata2 "setup"')
 
 
def test_1_needs_prepare_data(setup):
    print('\ntest_1_needs_prepare_data()')
 
def test_2_does_not_need_prepare_data():
    print('\ntest_2_does_not_need_prepare_data()')
 
def test_3_does_need_prepare_data(setup):
    print('\ntest_3_that_does()')

def test_4_needs_prepare_data2(setup, setup2):
    print('test_4_needs_prepare_data2()')
