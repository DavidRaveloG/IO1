import math
import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(0,1,2)
#funcion
y1=0*x
y2=0*x
plt.plot(x,y2,label='Gomas')
plt.plot(x*0,x,label='Lapices')
plt.plot(x*0,x,label='Carboncillos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('max z=4x+6y')
plt.legend(loc=1)
plt.scatter(1,0)
plt.show()
