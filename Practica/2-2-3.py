import numpy as np
import matplotlib.pyplot as plt

a = 0.5

def impulso(n):
    return np.equal(n,[0]*len(n))

def convolucion(x,h):
    N = len(x)
    M = len(h)
    y = [0]*(N+M-1)
    for n in range(N):
        for k in range(M):
            y[n+k] += x[n]*h[k]
    return y

def hA(n):
    return 8*np.sin(n)

def hB(n):
    return np.power([a]*len(n), n)

# test
N = 10
n = [i for i in range(N)]
ha = hA(n)
hb = hB(n)
x = [1,-a] # entrada d[n]-ad[n-1]

fig, ax = plt.subplots(7,sharex=True)
ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[3].grid()
ax[4].grid()
ax[5].grid()
ax[6].grid()

ax[0].set_title('$h_A[n]$')
ax[0].stem(ha)
ax[1].set_title('$h_B[n]$')
ax[1].stem(hb)
ax[2].set_title('$x[n]$')
ax[2].stem(x)
ax[3].set_title('$x[n]*h_A[n]$')
ax[3].stem(convolucion(x,ha))
ax[4].set_title('$x[n]*h_B[n]$')
ax[4].stem(convolucion(x,hb))
ax[5].set_title('$(x[n]*h_A[n])*h_B[n]$')
ax[5].stem(convolucion(convolucion(x,ha),hb))
ax[6].set_title('$(x[n]*h_B[n])*h_A[n]$')
ax[6].stem(convolucion(convolucion(x,hb),ha))

plt.show()
