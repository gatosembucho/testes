import pytest
from calc import soma, sub, div, mult, comp, imp,cel, fare, quadrado, retangulo, elipse, centimetros, metros,litros,mililitros,real,dolar,salario,autenticar

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
    
def test_litros():
    assert litros(1)==1000
    
def test_mil():
    assert mililitros(1000)==1

def test_dolar():
    assert dolar(1)==5
    
def test_real():
    assert real(5)==1
    
def test_salario():
    assert (100, 5)== 5000
    
def teste_autenticar():
    assert ("ana", "julia")=="maluzinha","123"