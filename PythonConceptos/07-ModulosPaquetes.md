<p align="center">
  <img src="../src/Learn-python.png">
</p>


# ***MÓDULOS Y PAQUETES EN PYTHON***

En Python, un **módulo** es un archivo que contiene definiciones y declaraciones de funciones, variables y clases que puedes utilizar en tus programas. Por ejemplo, el módulo `math` contiene funciones matemáticas como `sqrt()` y `sin()`, que puedes utilizar en tu código.

Para utilizar un módulo en tu programa, primero debes importarlo. Puedes hacerlo utilizando la palabra clave `import` seguida del nombre del módulo:

```
import math

raiz_cuadrada = math.sqrt(16)
print(raiz_cuadrada)
```

---

También puedes importar una función específica de un módulo utilizando la sintaxis `from <módulo> import <función>`:

```
from math import sqrt

raiz_cuadrada = sqrt(16)
print(raiz_cuadrada)
```

---

Un `paquete` es una colección de módulos que están organizados en una estructura de directorios. Los paquetes permiten organizar el código en módulos relacionados y evitar conflictos de nombres entre módulos. Por ejemplo, el paquete `numpy` contiene módulos relacionados con el cálculo numérico.

Para utilizar un módulo dentro de un paquete, primero debes importar el paquete y luego el módulo. Por ejemplo:

```
from math import sqrt

raiz_cuadrada = sqrt(16)
print(raiz_cuadrada)
```

---

También puedes importar una función específica de un módulo dentro de un paquete utilizando la sintaxis `from <paquete>.<módulo> import <función>`:

```
from numpy.random import randint

numero_aleatorio = randint(1, 10)
print(numero_aleatorio)
```

---

###  **CONCLUSIÓN**

En resumen, los módulos y paquetes en Python son una manera de organizar y reutilizar código. Los módulos son archivos que contienen definiciones y declaraciones de funciones, variables y clases, mientras que los paquetes son colecciones de módulos organizados en una estructura de directorios.

---

# ***Ahora que ya hemos adquirido los conceptos fundamentales de Python,[`¡EMPECEMOS A PONER EN PRÁCTICA LO APRENDIDO!`](url)***

<p align="center">
  <img src="../src/monkey.png">
</p>