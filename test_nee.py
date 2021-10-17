#This is for testing pytest for learning

import pytest

@pytest.fixture()
def my_sum():
    return 3+3

def test_sum():
    assert 2+3 == 5

def test_sum2(my_sum):
    assert my_sum == 6

def test_sub():
    assert 3-1 == 2

def test_swapcase():
    assert "abc".swapcase() == "ABC"

def test_swapcase2():
    assert "ABC".swapcase() == "abc"

def test_multi():
    assert 4*2 == 8

def test_div():
    assert 4/2 == 2
