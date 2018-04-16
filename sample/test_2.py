import pytest

def setup():
    print('         setup')

def setup_function():
    print('\n   setup_function')

def setup_module():
    print('\nsetup_module')

def teardown():
    print('\n         teardown')

def teardown_function():
    print('   teardown_function')

def teardown_module():
    print('teardown_module')

@pytest.fixture
def before():
    print('      before')
    yield None
    print('      after')

@pytest.fixture(params=[1,2])
def return_value(request):
    print('      return_value')
    π = 3.14*request.param
    return π

def test_this(before):
    print('            ', end='')

def test_that(return_value):
    print('            ', end='')
    print(return_value, end='')


# so the name of the fixture function works as a variable inside the test
# fixures have scopes: function module class session




