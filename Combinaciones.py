# Programa de ombinaciones para hallar el max o min de una función 
def variables(x1,x2,x3):
    return (10000*x1)+(6000*x2)+(4000*x3)<=10000
    
def F_objetivo(x1,x2,x3): 
    return (11000*x1)+(9000*x2)+(1000*x3)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
# diferentes posibilidades evaluadas en la función 
if(variables(1,1,1)==True):
    a=F_objetivo(1,1,1)
    print(str(F_objetivo)(1,1,1)+' con x1=1,x2=1,x3=1')
if(variables(1,1,0)==True):
    b=F_objetivo(1,1,0)
    print(str(F_objetivo(1,1,0))+' con x1=1,x2=1,x3=0')
if(variables(1,0,1)==True):
    c=F_objetivo(1,0,1)
    print(str(F_objetivo(1,0,1))+' con x1=1,x2=0,x3=1')
if(variables(0,1,1)==True):
    d=F_objetivo(0,1,1)
    print(str(F_objetivo(0,1,1))+' con x1=0,x2=1,x3=1')
if(variables(1,0,0)==True):
    e=F_objetivo(1,0,0)
    print(str(F_objetivo(1,0,0))+' con x1=1,x2=0,x3=0')
if(variables(0,1,0)==True):
    f=F_objetivo(0,1,0)
    print(str(F_objetivo(0,1,0))+' con x1=0,x2=1,x3=0')
if(variables(0,0,1)==True):
    g=F_objetivo(0,0,1)
    print(str(F_objetivo(0,0,1))+' con x1=0,x2=0,x3=1')
if(variables(0,0,0)==True):
    h=F_objetivo(0,0,0)
    print(str(F_objetivo(0,0,0))+' con x1=0,x2=0,x3=0')    
#calcula el maximo de la función 

maximo=[a,b,c,d,e,f,g,h]   

print('El maximo es: '+str(max(maximo)))
