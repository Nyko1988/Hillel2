import pytest


@pytest.fixture(scope='function', autouse=True)
def package_1_fixture():
    print('Function Start')
    yield
    print('Function End')
