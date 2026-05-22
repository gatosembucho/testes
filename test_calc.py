import pytest
from calc import soma, sub, div, mult, comp, imp,cel, fare, quadrado, retangulo, elipse, centimetros, metros

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

def test_quadrado():
    assert quadrado(5)==25

def test_retangulo():
    assert retangulo(3,2)==6

def test_elipse():
    assert elipse(3,2)==18.84

def test_metros():
    assert metros(1)==100
    
def test_cent():
    assert centimetros(100)==1
    