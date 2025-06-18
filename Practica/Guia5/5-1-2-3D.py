import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.colors as colors

def evaluarH(Y,X,z):
    '''
    Dado los coeficientes del numerador y denominador de H(z) y unos angulos omega,
    devuelve los valores de frecuencia
    '''
    H = np.zeros(len(z), dtype=complex)
    for i in range(len(z)):
        num = [Y[j]*np.power(z[i],-j) for j in range(len(Y))] # a0 + a1*z^-1 + a2*z^-2 + ...
        den = [X[j]*np.power(z[i],-j) for j in range(len(X))] # b0 + b1*z^-1 + b2*z^-2 + ...
        H[i] = np.sum(num)/np.sum(den)
    return H

#Helper Functions
def calcR(angle, x=1, y=1):
  return np.sqrt((x*y)/(x*np.cos(angle)**2 + y*np.sin(angle)**2))
def stretch_mesh(r, theta):
  return [ r[i] * calcR(theta[i][0]) for i in range(len(r)) ]

#Polar Mesh Grid
r = np.linspace(0, 1, 100)
theta = np.linspace(0, 2*np.pi, 100)
r, theta = np.meshgrid(r, theta)
# Stretch Function
r= stretch_mesh(r, theta)
# Transform to Cartesian
sigma = r * np.cos(theta)
omega = r * np.sin(theta)
z = sigma + 1j*omega

Y = [1, -2, 2, -1]
X = [1, -1.7, 0.8, -0.1]

z = np.asarray(z, dtype=complex)
original_shape = z.shape
z_flat = z.flatten()
H_flat = np.zeros(z_flat.shape)

H_min = -1
H_max = -1
for i in range(len(z_flat)):
    num = sum(Y[j] * z_flat[i]**(-j) for j in range(len(Y)))
    den = sum(X[j] * z_flat[i]**(-j) for j in range(len(X)))
    H_flat[i] = min([10,np.abs(num / den)])
    H_min = H_flat[i] if H_min == -1 else min(H_min,H_flat[i])
    H_max = H_flat[i] if H_max == -1 else max(H_max,H_flat[i])

H = H_flat.reshape(original_shape)

# Graficar

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(sigma, omega, H,
                       cmap=cm.rainbow,
                       linewidth=0, antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.set(zlim=(0,10))
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('$\\sigma$')
ax.set_ylabel('$\\omega$')
ax.set_zlabel('$H(z)$')

plt.show()