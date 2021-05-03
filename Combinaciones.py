# Programa de ombinaciones para hallar el max o min de una función 
def variables(x1,x2,x3):
    return (10000*x1)+(6000*x2)+(4000*x3)<=10000
    
def F_objetivo(x1,x2,x3): 
    return (11000*x1)+(9000*x2)+(10000*x3)

if(variables(1,1,1)==True):
    print(str(F_objetivo)(1,1,1)+' con x1=1,x2=1,x3=1')
if(variables(1,1,0)==True):
    print(str(F_objetivo(1,1,0))+' con x1=1,x2=1,x3=0')
if(variables(1,0,1)==True):
    print(str(F_objetivo(1,0,1))+' con x1=1,x2=0,x3=1')
if(variables(0,1,1)==True):
    print(str(F_objetivo(0,1,1))+' con x1=0,x2=1,x3=1')
if(variables(1,0,0)==True):
    print(str(F_objetivo(1,0,0))+' con x1=1,x2=0,x3=0')
if(variables(0,1,0)==True):
    print(str(F_objetivo(0,1,0))+' con x1=0,x2=1,x3=0')
if(variables(0,0,1)==True):
    print(str(F_objetivo(0,0,1))+' con x1=0,x2=0,x3=1')
if(variables(0,0,0)==True):
    print(str(F_objetivo(0,0,0))+' con x1=0,x2=0,x3=0')    
