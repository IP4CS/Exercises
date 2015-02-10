import numpy as np
import matplotlib.pyplot as plt

def dft(f_n):
    N = len(f_n)
    f_k = np.zeros((N), dtype=np.complex) 
    k= 0
    while k < N:
        n= 0
        while n < N:
            f_k[k] += f_n[n]*np.exp(-2.0*np.pi*1j*n*k/N)
            n += 1
        k += 1
    return np.array(np.real(f_k))

def f(x):
    return np.sin(2*np.pi*x/5)+np.sin(2*np.pi*x*0.7)

N=10
x = np.linspace(0, 10, 100 )

plt.figure(1)
plt.subplot(211)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.plot(x, f(x), 'bo-')

plt.subplot(212)
plt.xlim([0,1])
plt.ylabel('f(k)')
plt.xlabel('k/2$\pi$')
plt.plot(x, dft(f(x)), 'rs-')
plt.show()