import pytest
from calc import soma, sub, div, mult, comp, imp,cel, fare

def test_soma():
    assert soma(2,3) == 5

def test_sub():
    assert sub(3,2)==1

def teste_mult():
    assert mult(10,5)==50

def test_div():
    assert div(10,5)==2

def test_comp():
    assert comp (11,10)==11

def test_imp():
    assert imp(2)=="Par"

def test_cel():
    assert cel(32)==0

def teste_fare():
    assert fare(0)==32