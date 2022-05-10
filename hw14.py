import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, np.pi*4, 720) #x
x2 = np.linspace(0, np.pi*4*2, 720) #2x
x3 = np.linspace(0, np.pi*4*0.5, 720) #x/2
x4 = np.linspace(0, np.pi*4, 720) - np.pi*2*(15/360) #x-15

#print(x1)
y1 = np.sin(x1)
y2 = np.cos(x1)
y3 = np.sin(x2)
y4 = np.sin(x3)
y5 = np.sin(x4) * 0.5

plt.title('sin & cos functions')

plt.plot(y1, label='y1')
plt.plot(y2, label='y2')
plt.plot(y3, label='y3')
plt.plot(y4, label='y4')
plt.plot(y5, label='y5')
plt.legend()

plt.xlabel('Degree')
plt.xticks(range(0,721,60))
plt.ylabel('Valuses')

plt.show()