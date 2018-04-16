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

def test_f():
    pass

def test_g():
    pass
