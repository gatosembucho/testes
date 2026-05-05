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