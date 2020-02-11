import pytest
from exercises import *

@pytest.mark.skip()
def test_reverse():
    assert reverse('hello') =='olleh'
    assert reverse('hello world') == 'dlrow olleh'
    assert reverse('123456789') == '987654321'

@pytest.mark.skip()
def test_fib_rec():
    assert fib_rec(10) == 5
    assert fib_rec(1) == 1
    assert fib_rec(0) == 1
    assert fib_rec(20) == 6765

@pytest.mark.skip()
def test_fib_dyn():
    assert fib_dyn(10) == 5
    assert fib_dyn(1) == 1
    assert fib_dyn(0) == 1
    assert fib_dyn(20) == 6765

@pytest.mark.skip()
def test_fib_iter():
    assert fib_iter(10) == 5
    assert fib_iter(1) == 1
    assert fib_iter(0) == 1
    assert fib_iter(20) == 6765

@pytest.mark.skip()
def test_to_str():
    assert toStr(199, 10) == '199'
    assert toStr(30, 2) == '11110'
