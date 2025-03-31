# Sistemas

Un sistema se puede ver como **un proceso** que produce una transformación de señales, constituido por una entrada, una salida y una función de transferencia.

Se puede dividir en sistemas de tiempo discreto $x(t) \rightarrow y(t)$ y sistemas de tiempo continuo $x[t] \rightarrow y[t]$

## Interconexión de sistemas

Se puede interconectar sistemas para construir otro más complejos. Pueden conectar en serie, paralelo o como **retroalimentación**.

## Propiedades de los sistemas

Los sistemas presentan propiedades que sirven de criterio para clasificarlos, tanto en caso de tiempo discreto como tiempo continuo.

- Memoria
- Invertibilidad
- Causalidad
- Estabilidad
- Invariabilidad
- Linealidad

### Memoria

Un sistema tiene memoria si la salida depende de valores de **entrada anteriores**.

### Invertibles

Un sistema es invertible si distintas entradas producen distintas salidas. Esto es $\forall n \forall m (n \neq m \Rightarrow y[n] \neq y[m])$

### Causales o no-anticipativos

Un sistema es causal si su salida depende solo de los valores de **entrada actual y anteriores**. Otra forma de verlo es que no se necesitan conocer con anticipación valores futuros de entrada.

### Estables

Un sistema es estable si una entrada de magnitud acotada produce una salida también acotada (no diverge)

### Invariantes

Un sistema es invariante si una variación de la entrada produce la misma variación en la salida. También se puede decir que es invariante si los coeficientes de la ecuación que define la **dinamica del sistema** son constantes.

### Lineales

Un sistema es lineal si posee la propiedad de superposición. Esto es
$$ \forall t \left( y(x_1(t)) = y_1(t) \land y(x_2(t)) = y_2(t) \Rightarrow y \left( \alpha x_1(t) + \beta x_2(t) \right) = \alpha y_1(t) + \beta y_2(t) \right) $$

## Dinámica del sistema

La dinámica de los sistemas de tiempo continuo se representa mediante una ecuación diferencial, mientras que los de tiempo discreto se representan mediante una ecuación de diferencias.
En el caso de que ésta ecuación sea lineal de coeficientes constantes, se dice que el sistema es _lineal e invariante en el tiempo_ (LTI). Ejemplos de este tipo de sistemas son los circuitos pasivos RLC, sistemas mecánicos masa-resorte y cinética de reacciones químicas, en el caso de tiempo continuo; mientras que para sistemas de tiempo discreto tenemos la obtención de la respuesta que produce el tracto vocal a la excitación de las cuerdas vocales.

Para un orden N, estas ecuaciones lineales de coeficientes constantes están dadas por
$$\sum^N_{k=0} \alpha_k \frac{d^ky(t)}{dt^k} = \sum^M_{k=0}\beta_k\frac{d^kx(t)}{dt^k}$$
o, en su contraparte discreta, por
$$\sum^{N}_{k=0} a_k y[n-k] = \sum^{M}_{k=0} b_k x[n-k]$$

Vamos a hacer énfasis en las discretas. Esta última ecuación puede reescribirse
$$a_0y[n] + \sum^{N}_{k=1} a_k y[n-k] = \sum^{M}_{k=0} b_k x[n-k]\\
a_0y[n] = \sum^{M}_{k=0} b_k x[n-k] - \sum^{N}_{k=1} a_k y[n-k]\\
y[n] = \frac{1}{a_0} \left[ \sum^{M}_{k=0} b_k x[n-k] - \sum^{N}_{k=1} a_k y[n-k] \right]$$
Desta forma expresamos la salida en el instante _n_ en función de los **valores actual y anteriores de entrada** y de los **valores anteriores de salida**

### Sistemas FIR

En el caso de la ecuación no recursiva, estaremos hablando de sistemas de _respuesta finita al impulso_ (FIR, _Finite Impulse Response_)

$$y[n] = \frac{1}{a_0} \sum^{M}_{k=0} b_k x[n-k]$$

Estos sistemas también son llamados de _promedios móviles_ (MA, _Moving Average_), ya que realizan un promedio de la entrada en sucesivos instantes de tiempo.

### Sistemas IIR

Los sistemas representados por la primer ecuación recursiva que reescribimos

$$y[n] = \frac{1}{a_0} \left[ \sum^{M}_{k=0} b_k x[n-k] - \sum^{N}_{k=1} a_k y[n-k] \right]$$

son denominados de _respuesta infinita al impulso_ (IIR, _Infinite Impulse Response_) y se dividen en dos tipos

- **Sistemas Autogresivos** (AR): la salida está dada por los _valores anteriores de salida_ y únicamente el _valor actual de entrada_

$$y[n] = x[n] - \sum^{N}_{k=1} \frac{a_k}{a_0} y[n-k]$$

- **Sistemas ARMA**: la salida está dada por los valores anteriores de salida y entrada. Es decir, la ecuación recursiva que ya vimos en un inicio.
