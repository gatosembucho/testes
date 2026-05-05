import pytest
from calc import soma, sub, div, mult

def test_soma():
    assert soma(2,3) == 5

def test_sub():
    assert sub(3,2)==1

def teste_mult():
    assert mult(10,5)==50

def test_div():
    assert div(10,5)==2