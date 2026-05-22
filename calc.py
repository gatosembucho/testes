
def soma (a,i):
     return a+i 

def sub (a,i): 
    return a-i

def mult (a,i): 
    return a*i 

def div (a,i): 
    if i == 0: 
       raise ValueError("Não é possível dividir por 0!")
    return a/i 

def comp (a,i):
    if a>i:
        return a
    else:
        return i
    
def imp (a):
    if a%2==0:
        return ("Par")
    else:
        return ("Impar")    

def cel (a):
    return (a-32)/1.8

def fare (a):
    return (a*1.8)+32

##################################areas#################################

def quadrado(a):
    return a**2

def retangulo(a,i):
    return a*i

def elipse(a,i):
    return 3.14 * a * i

##################################conversao#################################
def centimetros(a):
    return a/100

def metros(a):
    return a*100

def litros(a):
    return a * 1000

def mililitros(a):
    return a / 1000

def dolar(a):
    return a*5

def real(a):
    return a/5
##################################slario liquido#################################
def salario(a,b):
    pagamento = a * b
    if pagamento>5000:
        pagamento=pagamento * 0.81
    else:
        pagamento= pagamento*0.89
    
    return pagamento
##################################login#################################
def autenticar(a,b):
    return a == "maluzinha" and b == "123"