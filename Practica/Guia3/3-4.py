import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider

def productoInterno(x,y):
    """Producto interno entre las seniales x e y"""
    # Verificar que tengan la misma longitud
    if(len(x) != len(y)):
        raise Exception('Las seniales no son del mismo tamanio')

    return np.sum(np.multiply(x,np.conjugate(y)))

def cuadrada(t, fs=1, fase=0):
    # precalcular modulos 2 * np.pi * fs * t + fase%(2pi)
    val = np.mod(2 * np.pi * fs * t + fase, 2 * np.pi)
    # retornar valores condicionados mod >= pi -> -1 
    return np.where(np.greater_equal(val, np.pi), -1, 1)

def senoidal(t,fs=1, fase=0):
    """Devuelve la senial senoidal de amplitud 1"""
    return np.sin(2*np.pi*t*fs + fase)

# Parametros
Tini = 0
Tfin = 5
fm = 100
coeficiente = [1 for _ in range(10)]
fase = [0 for _ in range(10)]

# Generar seniales
t = np.linspace(Tini,Tfin,int(fm*(Tfin-Tini)), endpoint=False)
y = [0] * len(t)
cuad = 3*cuadrada(t,5.5)                          # cuadrada
s = [[0] for _ in range(10)]

for i in range(10):
    s[i] = coeficiente[i]*senoidal(t,i+1,fase[i])
    y += s[i]

# ================= GRAFICAR =================
fig, ax = plt.subplots(3,1)
fig.set_figheight(10)
fig.set_figwidth(15)
fig.subplots_adjust(bottom=0.5)
ax[0].set_ylim(-10,10)
ax[1].set_ylim(0,1100)

ax[0].grid()
ax[1].axhline(0)
ax[2].axhline(0, color='black')
graphy, = ax[0].plot(t,y)
ax[0].plot(t,cuad)
bars = [0 for _ in range(10)]
cuadbars = [0 for _ in range(10)]               # cuadrada
for i in range(10):
    bars[i], = ax[1].bar(f"fs={i+1}Hz",productoInterno(y,s[i]))
    cuadbars[i], = ax[2].bar(f"fs={i+1}Hz",productoInterno(cuad,s[i]))          # cuadrada

# Sliders
coef_sliders_ax = [0 for _ in range(10)]
fase_sliders_ax = [0 for _ in range(10)]
coef_sliders = [0 for _ in range(10)]
fase_sliders = [0 for _ in range(10)]
for i in range(10):
    # Initialize axes and sliders here
    coef_sliders_ax[i] = fig.add_axes([0.15,0.45-i*0.025,0.1,0.03])
    coef_sliders[i] = Slider(
        ax=coef_sliders_ax[i],
        label=f"coef{i}",
        valmin=0,
        valmax=2,
        valinit=coeficiente[i],
        valstep=0.1
    )
    fase_sliders_ax[i] = fig.add_axes([0.35,0.45-i*0.025,0.1,0.03])
    fase_sliders[i] = Slider(
        ax=fase_sliders_ax[i],
        label=f"fase{i}",
        valmin=0,
        valmax=6,
        valinit=fase[i],
        valstep=0.05
    )

def update(event):
    # Recalcular y
    y = [0] * len(t)
    for i in range(10):
        # Recalcular la senoidal solo si cambia
        if(coef_sliders[i].val != coeficiente[i] or fase_sliders[i].val != fase[i]):
            coeficiente[i] = coef_sliders[i].val
            fase[i] = fase_sliders[i].val
            s[i] = coeficiente[i]*senoidal(t,i+1,fase[i])
        y += s[i]

    graphy.set_ydata(y)
    for i in range(10):
        bars[i].set_height(productoInterno(y,s[i]))
        cuadbars[i].set_height(productoInterno(cuad,s[i]))
        fig.canvas.draw_idle()

    ax[0].autoscale_view()
    ax[1].autoscale_view()
    ax[2].relim()
    ax[2].autoscale_view()

# Registrar callbacks
for i in range(10):
    coef_sliders[i].on_changed(update)
    fase_sliders[i].on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    for i in range(10):
        coef_sliders[i].reset()
        fase_sliders[i].reset()
button.on_clicked(reset)

plt.show()