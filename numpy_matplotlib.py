#numpy
import numpy as np
#Creating arrays: from lists and using built-in functions
#arrays from lists
distances = [10,15,17,26,20]
times = [0.3,0.47,.055,1.20,1.0]
distances = np.array(distances)
times = np.array(times)
#speed can be calculated as:
print(distances/times)
r1 = distances/times
print(np.round(r1,2))
product_quantities = [13,5,6,10,11]
prices = [200,650,100,480,554]
product_quantities = np.array(product_quantities)
prices = np.array(prices)
np.sum(product_quantities*prices)
A = np.array([1,2],[3,4])
np.zeros(10,dtype=int)
np.ones(shape=(3,5),dtype=float)
x = np.arange(start=0,stop=20,step=2)
y = np.linspace(0,1,20)

#matplotlib
import matplotlib.pyplot as plt
plt.plot([11,22,33,2,5])
plt.ylabel('some numbers');
plt.plot([1,2,3,4],[1,4,9,16]);
import numpy as np
def f(t):
  return np.exp(-t)*np.cos(s*np.pi*t)
t1 = np.arange(0,5,0.1)
t2 = np.arange(0,5,0.02)
plt.figure()
plt.subplot(2,1,1)
plt.plot(t1,f(t1),'bo')
plt.ylabel("Y label-1");
plt.subplot(2,1,2)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.ylabel("Y label-2");
