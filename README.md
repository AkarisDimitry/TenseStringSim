# **Simulación de Cuerda con Pygame**

Este repositorio contiene un programa que simula el movimiento de una cuerda bajo diferentes fuerzas. Utiliza la librería Pygame para renderizar gráficamente la cuerda y permite al usuario interactuar con ella.

## **Descripción** :

La simulación representa una cuerda sometida a varias fuerzas:
1. Elasticidad de la cuerda.
2. Gravedad.
3. Fricción.

### **Física de la Simulación**:

- **Elasticidad**:
  La fuerza elástica en un segmento de la cuerda se basa en la Ley de Hooke:
  \[ $F_e = k \times (d - d_{eq})$ \]
  Donde:
  - \( $F_e$ \) es la fuerza elástica.
  - \( $k$ \) es la constante elástica de la cuerda.
  - \( $d$ \) es la longitud actual del segmento.
  - \( $d_{eq}$ \) es la longitud de equilibrio del segmento.

- **Gravedad**:
  La cuerda es afectada por la gravedad que actúa en la dirección vertical hacia abajo.
  \[ $F_g = m \times g$ \]
  Donde:
  - \( $F_g$ \) es la fuerza gravitacional.
  - \( $m$ \) es la masa del segmento.
  - \( $g$ \) es la aceleración debido a la gravedad.

- **Fricción**:
  La fuerza de fricción actúa en dirección opuesta al movimiento y es proporcional a la velocidad del segmento:
  \[ $F_f = -\mu \times V$ \]
  Donde:
  - \( $F_f$ \) es la fuerza de fricción.
  - \( $\mu$ \) es el coeficiente de fricción.
  - \( $V$ \) es la velocidad del segmento.

### **Integración de Verlet**:

Para simular el movimiento de la cuerda, se utiliza la técnica de integración de Verlet. Esta técnica es popular en simulaciones físicas por su estabilidad y precisión. El algoritmo Verlet básicamente usa las posiciones actuales y anteriores para estimar la siguiente posición.

## **Funciones Principales**:

- `integrate`: Esta función se encarga de calcular la posición y velocidad de cada punto en la cuerda en el siguiente paso de tiempo.
  
- `String`: Define la clase principal que representa la cuerda y contiene todos los parámetros y métodos necesarios para la simulación.

## **Cómo Usar**:

1. Asegúrate de tener instaladas las librerías `pygame`, `numpy` y `numba`.
2. Ejecuta el código para iniciar la simulación.
3. Interactúa con la cuerda utilizando el ratón.

## **Contribución**:

Si deseas contribuir al proyecto, no dudes en hacer un fork y enviar un pull request. Todas las contribuciones son bienvenidas.
