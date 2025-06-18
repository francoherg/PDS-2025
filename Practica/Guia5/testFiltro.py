import numpy as np
import matplotlib.pyplot as plt

def testFiltro(h, lab="h"):
    '''Grafica un filtro en tiempo, frecuencia y fase'''
    N = len(h)
    fmax = N//2
    f =  np.arange(-fmax,fmax,1)
    H = np.fft.fft(h)
    H = np.concatenate([H[fmax:], H[:fmax]])

    fig = plt.figure()
    fig.set_figheight(3)
    fig.set_figwidth(15)
    ax = [
        plt.subplot2grid([1,3],[0,0]),
        plt.subplot2grid([1,3],[0,1]),
        plt.subplot2grid([1,3],[0,2]),
    ]

    for axi in ax:
        axi.grid()

    ax[0].plot(h)
    ax[0].set_title(f"${lab}$")
    ax[1].plot(f,np.abs(H))
    ax[1].set_title(f"$\\mathcal{{F}}({lab})$")
    ax[2].plot(f,np.angle(H))
    ax[2].set_title(f"$\\Phi({lab})$")
    fig.tight_layout()