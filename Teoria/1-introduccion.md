# Introducción

## Definición de señal

- Ejemplos
- Variable independiente (generalmente el tiempo)

## Clasificación

- Criterios: dimensional, energético, espectral, fenomenológico, morfológico.
- Clasificación Fenomenológica
  - Determinísticas: valores conocidos de antemano o predichos exactamente
    - Periódicas: cumple que $\forall{t} \in \Reals ( x(t+T)=x(t) )$ donde el minimo T se llama periodo
    - Aperiódicas: no periodica. [[1]](#consulta-1)
      - Singulares: tienen propiedades unicas, como la delta de Dirac, escalon, etc.
  - Aleatorias (estocasticas): existe una incerteza en los valores que puede tomar en los siguientes instantes.
    - Estacionarias: las propiedades estadisticas no varian en el tiempo
      - Ergodicas: las estadisticas a lo largo de una realizacion son iguales a las estadisticas a lo largo de todas las realizaciones.
      - No ergodicas:
    - No estacionarias:
      - Estacionarias por tramos
      - Especiales
  - Transitorias: agotan su energia en el periodo de observacion. La clasificacion depende mas de la escala desde la que se observa.
- Clasificación Morfológica
  - Discretas: variable independiente $ n \in \mathbb{Z} $ y $ y[n] = sin(nT) $
    - Digital: amplitud y variable independiente discretas
  - Continuas: variable independiente $ t \in \Reals $ y $ y(t) = sen(\omega T) $
    - Analógica: amplitud y variable independiente continuas.

## Sistemas de conversión analógica a digital (A/D) o Cuantización
[[2]](#consulta-2)

- Muestreo uniforme y no-uniforme
- Presición de la representación digital
- Aliasing

## Ruido

- Definicion (?): fenomeno o proceso que perturba la percepción o interpretación de la señal.
- Relación señal-ruido (S/R, SNR): medida de cuan contaminada está una señal. $ P_s: $ potencia de la señal, $ P_r: $ potencia del ruido. $$ \xi = \frac{P_s}{P_r} \ \xi \text{ dB} = 10 log \frac{P_s}{P_r}$$ recordemos que la potencia de una señal se puede calcular como $$\frac{1}{N} \sum^{N}_{n} |x[n]|^2$$
- Fuentes de ruido
  - Relacionadas con el sistema bajo estudio
    - Intrinsecas
    - Asociadas
  - Relacionadas con el sistema de procesamiento o medida
    - Externas: fuera del sistema, actuando en él por susceptibilidad
      - Generadas por artefactos eléctricos: motores electricos, bobinas, transformadores, rectificadores, etc
      - Tipo electromagnético: ondas electromagneticas de comunicación, radiocomunicación, TV, etc. [[3]](#consulta-3)
    - Internas: dentro del sistema, señales útiles que interfieren independientemente de las condiciones externas.
      - Impulsivas: generadas por la conmutación de corrientes.
      - Electrónicas: generado en cables y componentes por la propia naturaleza electrónica de los mecanismos de conducción. Constituido ppalmente por ruido térmico, tipo disparo y de aleteo o flicker.

## Teoria de la comunicación

- Composición:
  - Teoria de la señal: modulación y muestreo, análisis espectral, detección y estimación
  - Teoria de la información: teoría de la codificación. Codificación de la fuente, corrección y detección de errores, criptografía.
- Teoria de la señal
  - Objetivo: descripción matemática de las señales. Proporciona un modo de caracterizar la señal.
  - Expansión de Fourier: el caso más interesante de expansión en términos de funciones ortogonales. Su forma generalizada es la Transformada de Fourier.
- Teoría de la Información y Codificación (Offtopic)
  - Objeto: teoría probabilística de los mensajes, teniendo en cuenta sus propiedades sin importar el significado.
  - Herramientas: resulta util para la evaluación de sistemas de transferencia de información, sobretodo cuando la señal es afectada por ruido.
  - Codificación: busca
    - Densificar: compactar la señal, eliminando la redundancia
    - Confiabilidad: incrementar la confiabilidad de la señal, incrementando redundancia estructurada para la deteccion y correcion de errores a posteriori.
    - Privacidad: la criptografía trata de asegurar la privacidad de la comunicación.

## Procesamiento de Señales

- Definición: disciplina técnica que, por medio de métodos de la teoría de la información y la señal, se encarga de interpretar señales que acarrean información. Se ayuda de la electrónica, la computación y la física aplicada.
- Extracción de información útil
- Generación de señales
- Medición de una señal: estimación de una variabla características, vinculada a la señal con un determinado nivel de confianza.
- Filtrado
- Regeneración: recuperar la forma original de una señal luego de una distorsión.
- Extracción de señal de interes o detección
- Aislación de las componentes del sistema para entender mejor su naturaleza y/u origen.
- Identificación: clasificar la señal
- Síntesis: armado de una señal combinando señales elementales
- Codificación
- Modulación
- Traducción a frecuencias
- Analisis de señales

## Operaciones elementales con señales

- Operaciones unarias: involucran a una única señal
  - Operaciones de rango: modifican el rango de la señal. Los valores nuevos se determinan en función de los valores viejos, esto es $x_{nuevo} (t) = \rho (x_{viejo} (t))$
    - Amplificación
    - Rectificación: de onda completa o media onda
    - Cuantización
  - Operaciones de dominio: modifican la variable independiente. Se definen como $x_{nuevo} (t) = x_{viejo} (\tau ^{-1} (t))$
    - Expansion
    - Compresión
    - Reversión temporal (o inversión): una señal que es idéntica a su contraparte invertida es una _señal par_
    - Muestreo: pasa la variable independiente de un dominio continuo a uno discreto.
    - Interpolación: inversa al muestreo
- Operaciones binarias: se realizan punto a punto entre dos señales
  - Adición
  - Sustracción
  - Multiplicación
  - División

## Consultas

### Consulta 1

Una señal aperiódica es una señal que no es periódica. ¿Esto sería cualquier señal no determinista tambien? La pregunta viene porque está como subclasificación de las deterministicas.

### Consulta 2

"Conversión analógica a digital" (A/D) y "Cuantización" son lo mismo?

### Consulta 3
Por qué se hace una distinción entre estos dos tipos de fuentes externas de ruido? Eléctricas y electromagnéticas.