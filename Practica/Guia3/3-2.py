import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider

def productoInterno(x,y):
    """Producto interno entre las seniales x e y"""
    # Verificar que tengan la misma longitud
    if(len(x) != len(y)):
        raise Exception('Las seniales no son del mismo tamanio')

    return np.sum(np.multiply(x,np.conjugate(y)))

def senoidal(t,fs,A,alpha):
    aux = 2*np.pi*fs
    return A*np.sin(aux*t+alpha)

# ====================== MAIN ======================
Tini = 0
Tfin = 5
fm = 50

# parametros sin 1
fsx = 1
Ax = 1
fasex = 0
# parametros sin 2 (van a variar)
fsy = 1
Ay = 1
fasey = 0

# generar seniales
t = np.linspace(Tini,Tfin,int(fm*(Tfin-Tini)),endpoint=False)
x = senoidal(t,fsx,Ax,fasex)
y = senoidal(t,fsy,Ay,fasey)

fig, ax = plt.subplots(1,1)
fig.set_figwidth(10)
fig.set_figheight(5)
fig.subplots_adjust(bottom=0.5)

# graficas iniciales
ax.grid()
ax.plot(t,x,label="x")
graphy, = ax.plot(t,y,label="y")
txt = ax.text(0,1, "$ <x,y> = %.4f $ " % productoInterno(x,y), fontsize=10, va='center',
        bbox=dict(boxstyle='square'))

# sliders
fs_ax = fig.add_axes([0.25,0.1,0.5,0.03])
A_ax = fig.add_axes([0.25,0.2,0.5,0.03])
fase_ax = fig.add_axes([0.25,0.3,0.5,0.03])

fs_slider = Slider(
    ax=fs_ax,
    label='fs_Y [Hz]',
    valmin=0.1,
    valmax=5,
    valinit=fsy,
    #valstep=0.05,  # al fijar esto a 0.05 se puede ver que el PI se anula de a intervalso de 0.1 de fs
)
A_slider = Slider(
    ax=A_ax,
    label='A_Y',
    valmin=0.1,
    valmax=5,
    valinit=Ay,
    valstep=0.1,
)
fase_slider = Slider(
    ax=fase_ax,
    label='fase_Y',
    valmin=0,
    valmax=5,
    valinit=fasey,
    valstep=0.1,
)

# Callback de actualizacion de grafica
def update(event):
    y = senoidal(t, fs_slider.val, A_slider.val, fase_slider.val)
    graphy.set_ydata(y)
    txt.set_text("$ <x,y> = %.4f $ " % productoInterno(x,y))
    fig.canvas.draw_idle()

# registrar callback
fs_slider.on_changed(update)
A_slider.on_changed(update)
fase_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    fs_slider.reset()
    A_slider.reset()
    fase_slider.reset()
button.on_clicked(reset)

plt.show()