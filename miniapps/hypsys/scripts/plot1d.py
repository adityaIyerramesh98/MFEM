import numpy as np
from matplotlib import pyplot as plt

# exact
x=np.linspace(0,1,1000)
y=(x>=0.4)*(x<=0.6)
plt.plot(x,y,'--k',lw=1)

# # Order 0
# data = np.genfromtxt("scatter0.dat")
# index = np.argsort(data[:,0])
# plt.plot(data[index,0],data[index,1],'-m',lw=2)

# Order 1
data = np.genfromtxt("scatter1.dat")
index = np.argsort(data[:,0])
plt.plot(data[index,0],data[index,1],'-k',lw=2)

# Order 3
data = np.genfromtxt("scatter2.dat")
index = np.argsort(data[:,0])
plt.plot(data[index,0],data[index,1],'-b',lw=2)

# Order 7
data = np.genfromtxt("scatter3.dat")
index = np.argsort(data[:,0])
plt.plot(data[index,0],data[index,1],'-c',lw=2)

# Order 15
data = np.genfromtxt("scatter4.dat")
index = np.argsort(data[:,0])
plt.plot(data[index,0],data[index,1],'-g',lw=2)

# Order 31
data = np.genfromtxt("scatter5.dat")
index = np.argsort(data[:,0])
plt.plot(data[index,0],data[index,1],'-r',lw=2)

plt.ylim([-0.01,1.01])
plt.axis('off')
plt.legend(['p=1','p=3','p=7','p=15','p=31'])
plt.savefig('img.png')
