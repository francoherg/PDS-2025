# Convolución

La propiedad de superposición de los sistemas LTI (lineales e invariantes) permite represental la señal de entrada **en términos de un conjunto de señales básicas** y determinar la salida en términos de las respuestas a estas más básicas. Esto, sumado a la propieda de invarianza temporal, permite caracterizar un sistema en términos de su **respuesta al impulso**.
La forma de representar sistemas en términos de su respuesta al impulso se conoce como __integral de convolución__ en el caso continuo, o __sumatoria de convolución__ en tiempo discreto.

## Convolución Lineal

Para representar una señal de tiempo discreto $x[n]$ en términos de impulsos unitarios $\delta [n]$ (__Delta de Dirac__ para el caso continuo) se utiliza la suma de señales __impulso unitario__ desplazados escalados y desplazados en el tiempo.

$$ x[n] = ... + x[-2]\delta [n+2] + x[-1]\delta [n+1] + x[0]\delta [n] + x[1]\delta [n-1] + ... $$

O en forma compacta como

$$ \sum^{\infty}_{k=-\infty} x[k]\delta [n-k] $$

Esta es la **representación de una secuencia arbitraria como combinación lineal de secuencias de impulsos unitarios desplazados $\delta [n-k]$ con peso $x[k]$**.

Notese que, para un valor dado de $n$, sólo uno de los términos del lado derecho será diferente de cero.

Supongamos un sistema LTI con respuesta al impulso $h[n]$ y una entrada arbitraria x[n] dada por la ecuación anterior. Por invarianza temporal, $x[n]=\delta[n] \rightarrow h[n]=\delta[n-m] \rightarrow h[n-m]$ (si la entrada $\delta[n]$ da salida $h[n]$, $\delta[n-m]$ da salida $h[n-m]$). Además, por superposición, la salida puede expresarse como la combinación lineal de las respuestas a los impulsos escalados y desplazados. Es decir:

$$
\begin{align*}
    y[n] &= ... + x[-2]h[n+2] + x[-1]h[n+1] + x[0]h[n] + x[1]h[n-1] + x[2]h[n-2] + ...\\
    y[n] &= \sum^{+\infty}_{k=-\infty} x[k]h[n-k]
\end{align*}
$$

Esto es lo que se conoce como **sumatoria de convolución**, y el lado derecho de la ecucación se conoce como **convolución lineal** $x[n]$ y $h[n]$, o $y[n] = x[n] * h[n]$

### Representación Matricial

Desarrollando la sumatoria en cada instante podemos ver que se puede representar la convolución de forma matricial
$$
\begin{align*}
    y[0] &= x[0]h[0]\\
    y[1] &= x[0]h[1] + x[1]h[0]\\
    y[2] &= x[0]h[2] + x[1]h[1] + x[2]h[0]\\
    y[3] &= x[0]h[3] + x[1]h[2] + x[2]h[1] + x[3]h[0]\\
    &...\\
    y[N] &= x[0]h[N] + \sum^{N-1}_{i=0} x[N-i]h[i]\\
\end{align*}
$$
es equivalente a
$$
\begin{align*}
    \begin{bmatrix}
        y[0]\\y[1]\\y[2]\\y[3]
    \end{bmatrix}
    =
    \begin{bmatrix}
        h[0] &0 &0 &0\\
        h[1] &h[0] &0 &0\\
        h[2] &h[1] &h[0] &0\\
        h[3] &h[2] &h[1] &h[0]
    \end{bmatrix}
    \bullet
    \begin{bmatrix}
        x[0]\\x[1]\\x[2]\\x[3]
    \end{bmatrix}
\end{align*}
$$
Aunque solo se obtienen las primeras $N$ muestras correspondientes a la $x*h$. De todas formas esta forma es útil para la [deconvolución](#deconvolucion)

## Convolución Circular

La propiedad de equivalencia entre convolución en el tiempo y multiplicación en frecuencias (y viceversa) no se aplica para el caso de la convolución lineal en tiempo discreto. Para esto es necesario utilizar la **convolución circular**.
Esta convolución equivale a hacer periódicas las señales $x$ y $h$. Al contrario que la convolución lineal, mantiene la cantidad de muestras.

## Lineal a partir de circular

# Deconvolucion

Es la operación inversa de la convolución. Quiere decir que si tenemos la salida de un sistema correspondiente a una señal de entrada que no conocemos, podemos recuperarla mediante la deconvolución. Una forma de obtenerla es mediante la división término a término.
Pero si realizamos la convolución mediante su forma matricial $y=Hx$, podemos deconvolucionar mediante $H^{-1} y=x$. Ahora bien, en este caso estamos tratando de obtener la entrada (llamado caso de __control__), pero también puede ser que estemos intentando obtener la respuesta al impulso conociendo la entrada (llamado caso de __identificación__) $y=Xh \Rightarrow X^{-1}y=h$

## Problemas

Como la deconvolución corresponde al __problema inverso__ de la convolución, presenta algunos problemas. La presencia de una señal de ruido afectará más o menos a la deconvolución dependiendo de dónde aparezca (en la entrada, o luego de la convolución).

# Video

Correlación: muy relacionado a la convolución

Interpretación de la convolución:
- Plegado
- Desplazamiento
- Multiplicación
- Integración (suma)

Propiedad de suavizado de la convolución para filtrado de señales con ruido

Propiedades de la convolución
- Conmutativa
- Asociativa:
- Distributiva
- Conmutativa del producto con escalar
- Desplazamiento
- Derivabilidad
- Soporte de la convolución: una de las cosas que nos dice es la cantidad de muestras que va a tener la convolución de acuerdo a la cantidad de muestas de x y h
- Convolución y multiplicación

Lineal a partir de circular