import pytest


@pytest.mark.parametrize('val', [1, 2, 3])
@pytest.mark.param
def test_hw_2_test_1(val):
    assert val > 0


@pytest.mark.parametrize('elem1, elem2', [[1, 2], [3, 4]])
@pytest.mark.param
def test_hw_2_test_2(elem1, elem2):
    assert elem1 < elem2


@pytest.mark.parametrize('i', ["V", "P", "I", "S"], ids=['Vasya', 'Petya', 'Ivan', 'Sasim'])
@pytest.mark.param
def test_hw_2_test_3(i):
    assert 65 <= ord(i) <= 122
