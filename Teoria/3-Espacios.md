# Señales y Vectores

Considerando las señales como vectores de un espacio n-dimensional, podemos aprovechar muchas herramientas del álgebra lineal para entender su procesamiento

Los vectores son objetos matemáticos, definidos como colecciones o arreglos de datos que forman una entidad independiente. Podemos ver una señal en el espacio N-dimensional como un vector $[x_1,x_2,...,x_N]$, definido como una N/upla _ordenada_ de números:
$$ x=[x_n]; n\in N; x_n \in \Reals; x \in \Reals^N$$

## Normas

La norma provee una medida del **tamaño** de las señales. La norma de un vector/señal $x$ es un número real positivo que toma el valor 0 solo cuando $x = 0$.

Una norma muy utilizada es la **norma-p**, definida como:
$$
||x||_p = 
    \begin{cases}
        \left( \sum_{k=1}^{N} |x_k|^p \right)^{1/p}     &\quad 1 <= p < \infty \\
        sup|x|                                          &\quad\text{si } p = \infty \\
    \end{cases}
$$

### Casos particulares de norma p

La norma 1 o **accion** de la señal:
$$||x||_1 = \sum_{k=1}^{N}|x_k|$$

La norma 2 o **longitud** del vector:
$$||x||_2 = \sqrt{ \sum_{k=1}^{N}|x_k|^2 }$$

Existen varios parámetros relacionados a esta norma:
- **Energía**: es el cuadrado de la norma 2
$$E(x) = ||x||_2^2$$
- **Potencia** o **valor cuadrático medio**:
$$P(x) = lim_{N \rightarrow\infty} \frac{1}{N} E(x) = lim_{N \rightarrow\infty} \frac{1}{N} ||x||_2^2$$
- Raiz del valor cuadrático medio (**RMS**):
$$RMS(x) = \sqrt{P(x)}$$

La norma infinito o **amplitud** de la señal:
$$A(x) = ||x||_\infty = sup_{n \in [1,N]} |x_n|$$

La norma 0 es llamada una **cuasinorma**, ya que no cumple con la _desigualdad del triángulo_. Vendría a ser la cantidad de elementos del vector distintos de cero.

Existe otra medida de interes de las señales, como el **valor medio**
$$m(x) = lim_{N \rightarrow \infty} \frac{1}{N} \sum_{k=1}^{N} x_k$$
No confundir esto como la norma 1 de la señal, ya que en este caso no estamos sumando el valor absoluto

## Producto Interno

$$\langle x,y \rangle = x_1y_1^* + x_2y_2^* + ... + x_Ny_N^* = \sum_{k=1}^{N} x_ky_k^*$$
o
$$\langle x,y \rangle = ||x||_2 ||y||_2 cos\phi$$
donde $y^*$ representa el conjugado (en caso de tratarse de valores complejos).
Podemos ver que el producto interno de una señal/vector consigo mismo es igual a su norma 2 al cuadrado:
$$\langle x,x \rangle = \sum_{k=1}^{N}x_k^2 = ||x||_2^2$$

### Relación con la proyección de vectores

Definimos la proyección de $x$ sobre $y$ como
$$proy_yx = ||x||_2 cos \phi$$
Por lo que podemos verla como
$$proy_yx = \frac{\langle x,y \rangle}{||y||_2}$$
Ahora podemos ver que el producto interno nos da una idea del aporte de una señal sobre otra. En el caso particular de que la señal sobre la que proyectamos tenga norma 2 unitaria, **producto interno es directamente una medida del _parecido_ entre ambas señales**

# Espacios de señales

Un conjunto de señales $S$ son una colección de señales que cumplen una cierta propiedad o prueba. Una señal solo nos interesa en relación con otras señales del conjunto (si tiene mas energia, mas ceros, etc), por lo que se suele caracterizar de alguna forma la diferencia entre dos elementos de un conjunto, asignando a cada par un número real positivo (por ejemplo, la distancia geométrica). Para definir esta "distancia" se necesita un _funcional_ $d: \{x,y\} \rightarrow \Reals$.
Si este funcional cumple con las siguientes propiedades, entonces se le llama **métrica**
1. $d(x,y) = 0 \Leftrightarrow x=y$
2. $d(x,y) = d(y,x)$
2. $d(x,z) \leq d(x,y) + d(y,z)$
En ese caso además llamamos a $(S,d)$ **espacio métrico**. En el caso de que los elementos del conjunto sean señales, lo llamamos **espacio de señales**. Es importante notar que dos métricas distintas sobre el mismo conjunto de señales determinan espacios distintos.

## Distancia

La distancia es un concepto asociado a un espacio que nos permite darle un sentido geométrico a través de una _métrica_. Una métrica puede derivarse a partir de una norma, aunque pueden existir métricas que no deriven de una norma. Hay que tener en cuenta que la norma refiere a un solo elemento, mientras que la distancia se refiere a dos. Aún así, puede verse la norma como la _distancia del elemento al origen_.

Las **distancias de Minkowski** son distancias que se definen como la norma-p de la diferencia de dos vectores del espacio.
$$
d(x,y) = ||x-y||_p = L_p(x,y) = \left( \sum_{i=1}^{N} |x_i - y_i|^p \right)^{1/p}; \quad p>= 1
$$
- Distancia **Manhattan** ($p=1$):
$$ L_1(x,y) = \sum_{i=1}^{N}|x_i - y_i| $$
- Distancia **Euclidiana** ($p=2$):
$$ L_2(x,y) = \sqrt{\sum_{i=1}^{N} |x_i - y_i|^2} $$
- Distancia **máximo** ($p=\infty$):
$$ L_{\infty}(x,y) = max_{i=1}^{N} |x_i - y_i| $$

La **distancia en habla ruidosa** es una alternativa a la _relación señal-ruido (SNR)_, mejor ya que menor ruido no significa mayor _inteligibilidad_ de las palabras. 

## Espacios vectoriales

Una vez tenemos un conjunto de señales con una métrica asociada, para manipularlo necesitamos una estructura algebraica, proporcionada por un **espacio vectorial**.
Un espacio vectorial $S$ es un cuadruplete $(S,K,+,^.)$ (conjunto de vectores, campo de escalares, operación de adición y operación de producto por un escalar) y satisfacen **9 propiedades** (consultar libro), entre las que se encuentra el cierre en la adición, cierre en el producto por un escalar, etc.

En general el campo de escalares es $K = \Complex$, la adición se define como
$$x+y=[x_i + y_i]_{i\in[1,N]\subset \natnums}$$
y el producto por un escalar $\alpha \in K$ como
$$\alpha x = [\alpha x_i]_{i\in[1,N]\subset\natnums}$$

### Subespacios

Podemos demostrar que un subconjunto no vacío del conjunto de señales que constituye un espacio vectorial $V$ es también un espacio vectorial $V_0$, que denominamos **subespacio vectorial**.

### Espacio normado

Un espacio vectorial con una definición de norma constituye un **espacio normado** si _la norma es finita para todos sus elementos_. Por ejemplo, tomando la norma-p, podemos definir el espacio normado
$$\{x/||x||_p < +\infty\}$$

## Diferencia entre espacio metrico y espacio vectorial

La principal diferencia entre estos es que el espacio métrico los definimos teniendo un conjunto y "agregando" una métricas y esto nos proporciona una **estructura geométrica**. En el caso de el espacio vectorial, la **estrucutra algebraica** nos la proporciona el conjunto de manera intrínseca, no es algo que podemos obtener cambiando el campo de escalares, la adición o el producto por un escalar.

# Bases

## Conjuntos generadores

Dado un conjunto de $N$ vectores $X_0 = {x_i}$, con $N < \infty$, se define la **combinación lineal** de los vectores $x_i$ como
$$x = \sum_{i=1}^{N}\alpha_i x_i$$
donde $\alpha_i$ son escalares.

Se dice que un vector es **linealmente dependiente** del conjunto $X_0$ si y sólo si se puede escribir $x$ como combinación lineal de los vectores $x_i$. En caso contrario, el vector es **linealmente independiente** de los vectores $x_i$.

Al variar los coeficientes $\alpha_i$ se generan todas las combinaciones lineales posibles de los $x_i$ y el resultado es un conjunto $X$ de nuevos vectores $x_j$ que heredan muchas propiedades de los $x_i$ generadores. Si a su vez el nuevo conjunto $X$ constituye un espacio vectorial $X$, etnocnes se dice que el conjunto $X_0$ es un **conjunto generador** del espacio. También se puede decir que para todo vector $x \in X$ existe un conjunto de escalares $A = \{\alpha_i\}$ tales que $x$ se puede expresar como combinación lineal de los $x_i$.

Un **conjunto linealmente independiente** es un conjunto de vectores que cumplen con la condición
$$
\sum_{i=1}^{N}\alpha_i x_i = 0 \Leftrightarrow \forall i \in [1,N] \left( \alpha_i = 0 \right)
$$
También puede definirse como que ningún vector del conjunto puede expresarse como combinación lineal de los demás vectores del mismo conjunto.

El conjunto de vectores $X_0$ es una **base** del espacio vectorial $X$ si $X_0$ es _linealmente independiente_ y es un _conjunto generador_ de $X$. A partir de esto, la **dimension** $D$ de un espacio vectorial es el número de vectores de una base de dicho espacio, y puede demostrarse que cualquier conjunto de $N > D$ vectores del espacio será _linealmente dependiente_. Particularmente nos interesa saber que _todo conjunto de $N$ vectores linealmente independientes en $\Reals^N$ será una base para $\Reals^N$_

## Ortogonalidad y Ortonormalidad

Un conjunto de vectores $X_0$ es **ortogonal** si
$$
\begin{align*}
    \langle x_i,x_j \rangle &= 0 \quad \forall i\neq j \text{ y}\\
    \langle x_i,x_j \rangle &= k \quad \forall i = j
\end{align*}
$$
donde $k$ es una constante escalar distinta de cero. Si además $k=1$, entonces el conjunto es **ortonormal**.

Si un conjunto $X_0$ _ortonormal_ es base de un espacio $X$ y se quiere expresar un vector como combinación lineal de los elementos de $X_0$, entonces los coeficientes $\alpha_i$ se pueden obtener simplemente mediante el _producto interno_ entre el vector y cada uno de los elementos de la base. Es decir:
$$
\begin{align*}
    x &= \alpha_1x_1 + \alpha_2x_2 + ... + \alpha_Nx_N \\
      &= \langle x,x_1 \rangle x_1 + \langle x,x_2 \rangle x_2 + ... + \langle x,x_N \rangle x_N
\end{align*}
$$

Demostración:
$$
\begin{align*}
    x &= \alpha_1x_1 + \alpha_2x_2 + ... + \alpha_Nx_N \\
    \langle x,x_1 \rangle &= \alpha_1 \langle x_1,x_1 \rangle + \alpha_2 \langle x_2,x_1 \rangle + ... + \alpha_N \langle x_N,x_1 \rangle &\quad \text{(producto interno por }x_1\text{ de ambos lados)}\\
    \langle x,x_1 \rangle &= \alpha_1 (1) + \alpha_2 (0) + ... + \alpha_N (0) &\quad \text{(por ortonormalidad)}\\
    \langle x,x_1 \rangle &= \alpha_1 = \sum_{n=1}^{N}x_nx_n^*\\
\end{align*}
$$

Como vemos, en esta forma cada coeficiente es una medida del _parecido_ entre el vector y el elemento de la base. A su vez, como vimos antes al analizar el producto interno como proyección, conceptualmente el coeficinete es la _componente de la señal $x$ en elemento_ $x_i$.

# Aproximación de señales

Si queremos aproximar la señal $y \in \Reals^M$ mediante una combinación lineal del conjunto _ortonormal_ $X_0 = {x_1, x_2, ..., x_N}$, debemos encontrar los coeficientes $\alpha_k$ que minimicen el error entre la combinación lineal y la señal $y$. El criterio más intuitivo para medir el error es el cuadrado de la longitud del _vector diferencia_ entre la señal y la aproximación, que se conoce como **error cuadrático total**:
$$
\epsilon = ||e||_2^2 = ||y-\~{y}||_2^2 = \sum_{j=1}^{M} \left( y_j-\~{y_j} \right)^2 = \sum_{j=1}^{M} \left( y_j - \sum_{i=1}^{N}\alpha_ix_{ij} \right)^2
$$
Para encontrar el mínimo del error debemos resolver $\nabla_{\alpha}\epsilon = 0$
$$
\begin{align*}
    0 &= \frac{\partial \epsilon}{\partial \alpha_k}\\
    0 &= \frac{\partial \sum_{j=1}^{M}\left( y_j - \sum_{i=1}^{N} \alpha_ix_{ij} \right)}{\partial \alpha_k}\\
    0 &= 2 \sum_{j=1}^{M} \left( y_j - \sum_{i=1}^{N} \alpha_ix_{ij} \right) \frac{\partial \left( y_j - \sum_{i=1}^{N}\alpha_ix_{ij} \right)}{\partial \alpha_k} \quad\text{(regla de la cadena)}\\
    0 &= 2 \sum_{j=1}^{M} \left( y_j - \sum_{i=1}^{N} \alpha_ix_{ij} \right) \left( \frac{\partial y_j}{\partial \alpha_i} - \frac{\partial\sum_{i=1}^{N}\alpha_ix_{ij}}{\partial \alpha_k} \right)\\
    0 &= 2 \sum_{j=1}^{M} \left( y_j - \sum_{i=1}^{N} \alpha_ix_{ij} \right) \left(-x_{kj} \right); \quad \frac{\partial y_j}{\partial \alpha_i}=0; \quad \forall i\neq k \left( \frac{\partial \alpha_ix_{ij}}{\partial \alpha_k} = 0 \right)\\
    0 &= -2 \sum_{j=1}^{M} \left( y_j - \sum_{i=1}^{N}\alpha_ix_{ij} \right)x_{kj}\\
    0 &= -2 \sum_{j=1}^{M} \left( y_jx_{kj} - \sum_{i=1}^{N}\alpha_ix_{ij}x_{kj} \right)\\
    \frac{0}{-2} &= \sum_{j=1}^{M} y_jx_{kj} - \sum_{j=1}^{M} \sum_{i=1}^{N}\alpha_ix_{ij}x_{kj}\\
    \sum_{j=1}^{M} \sum_{i=1}^{N}\alpha_ix_{ij}x_{kj} &= \sum_{j=1}^{M} y_jx_{kj}\\
    \sum_{i=1}^{N} \alpha_i \sum_{j=1}^{M}x_{ij}x_{kj} &= \langle y,x_k \rangle\\
    \sum_{i=1}^{N} \alpha_i \langle x_i,x_k \rangle &= \langle y,x_k \rangle\\
    \alpha_k \langle x_k,x_k \rangle &= \langle y,x_k \rangle; \quad \forall i\neq k \left( \langle x_i, x_k \rangle = 0 \right)\\
    \alpha &= \frac{\langle y, x_k \rangle}{\langle x_k, x_k \rangle}
\end{align*}
$$
Si además el conjunto es ortonormal, vemos que $\alpha_i = \langle y,x_i \rangle$. Este resultado demuestra que el conjunto de coeficientes obtenido mediante proyecciones ortogonales minimiza el error total. Otra forma de verlo es que el coeficiente que aproxima a un vector es la proyección de dicho vector sobre el vector "aproximador" (?).

# Cambio de base

Para un espacio vectorial dado existen infinitas bases. Por lo general representamos una señal simplemente utilizando la base canónica $X_e = {e_1, e_2, ..., e_N}$