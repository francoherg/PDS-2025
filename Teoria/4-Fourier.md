# Números complejos

Un número complejo se puede expresar como
$$c = a + jb$$
Donde $j$ es la unidad imaginaria o $\sqrt{-1}$ (los matemáticas la llaman $i$, los ingenieros la llamamos $j$). Una forma de representar este número es como un vector $(a,b)$ en el plano $\Reals x \Complex$, por lo tanto puede expresarse en forma polar por medio de su magnitud $r$ (o longitud) y el ángulo $\theta$ con el eje de los reales
$$c  = r\left[cos(\theta) + j sin(\theta)\right]$$
Por el _teorema de Euler_, sabemos además que
$$cos(\theta) + j sin(\theta) = e^{j\theta}$$
Entonces
$$c = r \left[ cos(\theta) + j sin(\theta) \right] = e^{j\theta}$$

## Conjugado

Es importante saber que, para un número complejo
$$c = a + j b$$
su conjugado no es más que
$$c^* = a - j b$$
y en su forma de Euler esto es equivalente a
$$c^* = e^{-j\theta}$$
**Demo:**
$$
\begin{align*}
	e^{-j\theta} &= e^{j(-\theta)}\\
					  &= cos(- \theta) + j sin(- \theta)\\
					  &= cos(\theta) - j sin(\theta)\\
					  &= c^*
\end{align*}
$$

# Transformada de Fourier

Vimos que para aproximar una señal $x$ mediante la combinación lineal de $k$ señales $\phi_i$ debemos usar los coeficientes $\alpha_i$ que minimizan el error, los cuales se calculan como
$$\alpha_i = \frac{\langle x, \phi_i \rangle}{\langle \phi_i, \phi_i \rangle}$$
de esta forma tendremos la combinación lineal
$$x = \sum^{i} \alpha_i \phi_i$$

La **transformada discreta de Fourier** es exactamente esto, donde señales de la combinación lineal son
$$
\begin{align*}
	\phi_i &= e^{j \frac{2\pi k}{N} n}\\
			 &= e^{j \omega_k n}
\end{align*}
$$
Las cuales cumplen tres propiedades importante:
- son periódicas
- son ortogonales
- son completas

Entonces, en definitiva tenemos que
$$x = \sum^{N}_{k=1}\alpha_k \phi_k$$
donde cada coeficiente esta definido como
$$
\begin{align*}
	\alpha_k &= \frac{\langle x, \phi_k \rangle}{\langle \phi_k, \phi_k \rangle}\\
	&= \frac{1}{N} \sum^{N}_{n=1}x[n]\phi_k[n]\\
	&= \frac{1}{N} \sum^{N}_{n=1}x[n] e^{-j \frac{2\pi k n}{N}}\\
\end{align*}
$$
([acá](#Ortogonalidad) la demostración de por qué $1/N$)
Normalmente se suele definir sin $1/N$ en la transformación ya que si solo nos interesa el análisis de frecuencias no es necesario. En caso de querer reconstruir la señal, se agrega $1/N$, pero en caso contrario son $N$ divisiones que nos podemos ahorrar.

### Periodicidad

Para demostrar que son periódicas hay que demostrar que $x[n] = x[n+N]$
$$
\begin{align*}
	e^{j\omega_k n} &= e^{j \omega_k (n+N)}\\
	e^{j\omega_k n} &= e^{j \omega_k n} e^{j \omega_k N}\\
	e^{j\omega_k N} &= 1\\
	cos(\omega_k N) + j sin(\omega_k N) &= 1\\
	cos(\omega_k N) &= 1 \Leftrightarrow \omega_k N\text{ debe ser multiplo entero de } 2\pi\\
	\omega_k N &= 2\pi k\\
	\omega_k &= \frac{2\pi k}{N} \quad \text{con }k\in \mathbb{Z}
\end{align*}
$$

### Ortogonalidad

Para demostrar que
$$
\langle \phi_i, \phi_j \rangle = 
\begin{cases}
	0 &\quad \text{si } i \neq j\\
	K &\quad \text{si } i = j
\end{cases}
$$
podemos ver que
$$
\begin{align*}
	\langle \phi[k_1], \phi[k_2] \rangle &= \sum^{N-1}_{n=0}e^{j \frac{2\pi k_1}{N}n} e^{-j \frac{2\pi k_2}{N}n}\\
	&= \sum^{N-1}_{n=0} e^{j \frac{2\pi (k_1-k_2)}{N}n}
\end{align*}
$$
y en el caso de que $k_1 = k_2$ vemos que obtenemos N
$$
\sum^{N-1}_{0} 1 = N \quad \forall k_1 = k_2
$$
Por otro lado, en el caso que $k_1 \neq k_2$ entonces		**(esto no hace falta saberlo, solo tener en cuenta que cuando son distintos es 0)**
$$
\begin{align*}
	&= \sum^{N-1}_{n=0} e^{j \frac{2\pi (k_1-k_2)}{N}n}\\
	&= \sum^{N-1}_{n=0} e^{j \frac{2\pi (\Delta k)}{N}n}\\
	&= \sum^{N-1}_{n=0} \left( e^{j \frac{2\pi (\Delta k)}{N}} \right)^n
\end{align*}
$$
es decir, una serie geométrica donde $r$ será nuestro exponente
$$
\begin{align*}
	\sum^{N-1}_{n=0} r^n &= \frac{1-r^N}{1-r}\\
	&= \frac{1 - \left( e^{j \frac{2\pi \Delta k}{N}} \right)^N}{1-r}\\
	&= \frac{1 - e^{j 2\pi \Delta k} }{1-r}\\
	&= \frac{1 - e^{j 2\pi \Delta k} }{1-r} \quad \text{, } \Delta k \in \mathbb{Z} \Rightarrow e^{j2\pi \Delta k} = 1\\
	\sum^{N-1}_{n=0} r^n &= \frac{1-1}{1-r} = 0
\end{align*}
$$

## Coeficientes

Cada uno de los coeficientes $\alpha_k$ es un complejo, por lo que tiene una parte real y otra imaginaria. Pero aún más útil es verlos en su forma polar, es decir **magnitud** y **fase**. De esta forma obtenemos de los componentes el espectro de magnitudes de frecuencias ($|x|_{(f)}$) y la gráfica de fases.

## Transformadas de Fourier según sus dominios

Lo que vimos es la Transformada **Discreta** de Fourier
$$
\begin{align*}
	X[k] &= \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi k}{N}n} \quad \quad \text{espectro discreto}\\
	x[n] &= \frac{1}{N} \sum_{k=0}^{N-1} X[k]e^{j\frac{2\pi k}{N}n} \quad \text{tiempo discreto}
\end{align*}
$$
donde tanto el dominio del tiempo como el dominio de las frecuencias es discreto. Pero existen otras transformadas

La Transformada de Fourier **de tiempo discreto** tiene, como su nombre lo dice, tiempo discreto, pero un espectro de frecuencias continuo
$$
\begin{align*}
	X(f) &= \sum_{n=-\infty}^{\infty}x[n]e^{-j2\pi fn} \quad \quad \text{espectro continuo}\\
	x[n] &= \int_{-\frac{1}{2T}}^{\frac{1}{2T}}X(f)e^{j2\pi fn}df \quad \text{tiempo discreto}
\end{align*}
$$

La transformada **continua** de Fourier tiene tanto tiempo como espectro continuo
$$
\begin{align*}
	X(f) &= \int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt \quad \text{espectro continuo}\\
	x(t) &= \int_{-\infty}^{\infty}X(f)e^{j2\pi fn}df \quad \text{tiempo continuo}
\end{align*}
$$

## Transformada discreta y periodicidad

No hay que confundir la TDF con la TFTD, donde la diferencia más importante radica en que la TDF se aplica a señales discretas **periódicas** de duración infinita o extensiones periódicas de señales de duración finita. Además de esto, tanto el dominio como la imágen de la TDF son discretos, mientras que en la TFTD la imágen es continua.
Al aplicar la TDF, el producto interno conceptualmente mide el _grado de parecido_ de una señal con respecto a la otra, por lo que estamos haciendo es comparar la señal de interés con las N exponenciales complejas que forman la base de $\Reals^N$. Intetamos determinar qué tanto de dicha exponencial debe _usarse_ en la combinación lineal para sintetizar la señal original o qué tanto de la exponencial _hay_ en la señal original. Estamos descomponiendo la señal en una serie de N exponentes de diferentes frecuencias, por lo que podemos estudiar características frecuenciales de la señal o el sistema que la generó.

Si bien consideramos N muestras de las exponenciales complejas, estos valores se repiten en las N muestras siguientes, lo que implica que **al hacer una combinación lineal de ellas, el resultante será una función de período N**. Cuando trabajamos con señales discretas de longitud finita, usualmente se trata de valores muestreados de una señal continua, por lo que este resultado no es "correcto", ya que la señal fuera del intervalo de meustreo habrá tenido valores que desconocemos. Estamos _suponiendo_ que son iguales a los N elementos conocidos.

**Al muestrear una señal y aplicar la TDF a este muestreo, lo que estamos haciendo es periodicidarla.**

## Propiedades de la TDF

La siguiente notación se identificar el par formado por una señal $x[n]$ y su TDF $X[k]$
$$x[n] \xLeftrightarrow{\mathcal{F}} X[k]$$
Para $x[n] \xLeftrightarrow{\mathcal{F}} X[k]$ y $y[n] \xLeftrightarrow{\mathcal{F}} Y[k]$ se verifican las siguientes propiedades:

1. Linealidad:
$$x[n] + y[n] \xLeftrightarrow{\mathcal{F}} X[k] + Y[k]$$
2. Simetría:
$$\frac{1}{N} \mathcal{F}\{x[n]\}[k] \xLeftrightarrow{\mathcal{F}} \mathcal{F}^{-1}\{X[k]\} [-n]$$
3. Desplazamiento temporal (retardo):
$$x[n-i] \xLeftrightarrow{F} X[k]e^{-j\frac{2\pi ki}{N}}$$
4. Desplazamiento frecuencial (modulación):
$$x[n]e^{j\frac{2\pi in}{N}} \xLeftrightarrow{\mathcal{F}}X[k-i]$$
5. Convolución en el tiempo:
$$x[n] \circledast y[n] \xLeftrightarrow{\mathcal{F}}X[k]Y[k]$$
6. Convolución en frecuencia:
$$x[n]y[n] \xLeftrightarrow{\mathcal{F}}\frac{1}{N} X[k]\circledast T[k]$$
7. Teorema de corrrelación cruzada:
$$\sum_{i=0}^{N}x[i]y[n+1] \xLeftrightarrow{\mathcal{F}} X[k]Y[k]^*$$
8. Teorema de Parseval (conservación de la energía):
$$\sum_{n=0}^{N-1}x[n]^2 = \frac{1}{N}\sum_{k=0}^{N-1}|X[k]|^2$$

## TDF, alias y rizado

Desarrollado y demostrado [acá](https://github.com/Lucasa98/PDS-2025/blob/main/Teoria/4-Fourier.ipynb)

Teniendo una señal continua _muestreada_ de duración infinita, mientras que en el dominio frecuencial tenemos una señal continua y periódica. Lo que tenemos es la Transformada de Fourier de Tiempo Discreto.

Para acotar la señal en el tiempo, debemos multiplicar la señal muestreada por una ventana cuadrada $s(t)$, lo cual equivale a convolucionar la TCF de la ventana ($s(f)$) en el dominio frecuencial, que corresponde a una función _sinc_. El efecto de esta convolución es un rizado o _ripple_ en el dominio frecuencial.

Luego, para muestrear en el dominio frecuencial y obtener un espectro discreto, multiplicamos por un tren de impulsos $\Delta_2(f)$ separados por $1/T_2$, lo que, en el dominio temporal, se traduce como la convolución por un tren de impulsos separados por $T_2$. Como resultado obtenemos una señal periódica de período $T_1$. Si se elige un valor $T_2$ igual al ancho $T_1$ de la ventana temporal $s(t)$ aplicada, entonces al hacer la convolución no se solapan las imágenes de la señal en el tiempo.

Finalmente, tomamos N muestras en el dominio temporal y N en el frecuencial y así obtenemos la TDF de la señal. Una vez más, es importante saber que, al hacer esto, asumimos que tanto en el dominio frecuencial como temporal tenemos señales periódicas y trabajamos con su período completo.

# Ventanas

Acabamos de analizar la TDF como consecuencia proceso del muestreo y limitación en la duración de la señal. Para esto último utilzamos una ventana cuadrada en el dominio temporal, lo cual equivale a una convolución en el dominio de frecuencias con una función sinc, generando la aparición de un rizado en el espectro. Existen ventanas diferentes que evitan este efecto no deseado, de forma que su espectro frecuencial presente "lóbulos" laterales de menor amplitud.
Entre estas tenemos:
- Ventana de Hann:
$$\omega_h[n] = \frac{1}{2} - \frac{1}{2} cos\left(\frac{2\pi n}{N}\right)$$
- Ventana de Hamming:
$$\omega_R[n] = \frac{27}{50} - \frac{23}{50} cos\left(\frac{2\pi n}{N}\right)$$
- Ventana de Bartlett:
$$
\omega_R[n] =
\begin{cases}
    \frac{2n}{N}    &\quad 0<n\leq N/2\\
    2-\frac{2n}{N}  &\quad \frac{N}{2}<n\leq N
\end{cases}
$$
- Ventana de Blackman:
$$\omega_R[n] = \frac{21}{50} - \frac{1}{2} cos\left(\frac{2\pi n}{N}\right) + \frac{2}{25} cos\left(\frac{4\pi n}{N}\right)$$

Para ver gráficamente estas ventanas y su efecto en el dominio temporal y frecuencial, ver [este ejercicio](https://github.com/Lucasa98/PDS-2025/blob/9221d445f10b1ee42f12dffd26e23f1544e67a88/Practica/Guia4/4-4.ipynb)

Aunque la magnitud del lóbulo central de la ventana rectangular en el espectro de frecuencias es la de mayor magnitud entre estas ventanas, los lóbulos laterales decaen muy lentamente en magnitud. En cambio, la ventana de Blackman posee la menor de las amplitudes en sus lóbulos laterales, a la vez que su lóbulo central tiene un ancho de banda tres veces mayor al de la rectangular.
