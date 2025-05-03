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

## Espacios vectoriales

Una vez tenemos un conjunto de señales con una métrica asociada, para manipularlo necesitamos una estructura algebraica, proporcionada por un **espacio vectorial**.
Un espacio vectorial $S$ es un cuadruplete $(S,K,+,^.)$ (conjunto de vectores, campo de escalares, operación de adición y operación de producto por un escalar) y satisfacen **9 propiedades** (consultar libro), entre las que se encuentra el cierre en la adición, cierre en el producto por un escalar, etc.

En general el campo de escalares es $K = \Complex$, la adición se define como
$$x+y=[x_i + y_i]_{i\in[1,N]\subset \natnums}$$
y el producto por un escalar $\alpha \in K$ como
$$\alpha x = [\alpha x_i]_{i\in[1,N]\subset\natnums}$$