import numpy as np
import matplotlib.pyplot as plt

def ECT(y,yapprox):
    """
        Error cuadratico total entre y y su aproximacion.\\
        Se define como la norma 2 al cuadrado de la diferencia de las seniales, pero por optimizacion y para evitar error de redondeo lo hacemos directamente como la suma de los cuadrados de la diferencia
    """
    if(len(y) != len(yapprox)):
        raise Exception("las seniales no tienen el mismo tamanio")

    return np.sum(np.power(y-yapprox,[2]*len(y)))

def yreal(t):
    """funcion real y(t) donde t<0 => y(t)=-1, si no y(t)=1"""
    return np.where(np.less(t,[0]*len(t)),-1,1)

def yapproxvar(t,alpha,beta):
    """aproximacion de y con polinomios de Legendre con variacion alpha y beta de las constantes"""
    frac1 = (45.0/16.0) + alpha
    frac2 = (35.0/16.0) + beta
    return frac1*t - frac2*np.power(t,[3]*len(t))

# Parametros
Tini = -1
Tfin = 1
fm = 50

# y original
t = np.linspace(Tini,Tfin,int(fm*(Tfin-Tini)), endpoint=False)
y = yreal(t)

# Calculo de errores
alpha = [[0] for _ in range(121)]
beta = [[0] for _ in range(121)]
e = [[0] for _ in range(121)]
for i in range(121):
    # senial aproximante
    alpha[i] = (i%11-5)*0.1
    beta[i] = (int(i/10.0)-5)*0.1
    s = yapproxvar(t,alpha[i],beta[i])
    # error
    e[i] = ECT(y,s)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
fig.set_figheight(5)
fig.set_figwidth(15)

ax.scatter(alpha,beta,e)

ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('error')

plt.show()