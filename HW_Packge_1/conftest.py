import pytest


@pytest.fixture(scope='class', autouse=True)
def package_1_fixture():
    print('Class Start')
    yield
    print('Class End')

