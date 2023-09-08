<p align="center">
  <img src="../src/Learn-python.png">
</p>


# ***ESTRUCTURAS DE DATOS***

En Python, hay tres tipos de estructuras de datos que se utilizan comúnmente: `LISTAS`, `TUPLAS` y `DICCIONARIOS`.

---

### **• LISTAS:**

Una lista es una colección ordenada y mutable de elementos, que se definen entre corchetes (`[]`). Puedes agregar, eliminar y modificar elementos en una lista, y también puedes acceder a ellos mediante su índice (un número que representa su posición en la lista, empezando por 0).

Por ejemplo, aquí hay una lista de números enteros:

```
numeros = [1, 2, 3, 4, 5]
```

Puedes acceder a los elementos de una lista mediante su índice:

```
print(numeros[0])  # Output: 1
print(numeros[3])  # Output: 4
```

También puedes modificar los elementos de una lista:

```
numeros[2] = 6
print(numeros)  # Output: [1, 2, 6, 4, 5]
```

---

### **• TUPLAS:**

Una tupla es similar a una lista, pero es inmutable, lo que significa que no se pueden agregar, eliminar o modificar elementos después de que se hayan creado. Las tuplas se definen entre paréntesis (`()`).

Por ejemplo, aquí hay una tupla de colores:

```
colores = ("rojo", "verde", "azul")
```

Puedes acceder a los elementos de una tupla mediante su índice:

```
print(colores[0])  # Output: "rojo"
print(colores[2])  # Output: "azul"
```

Pero no puedes modificar los elementos de una tupla:

```
colores[1] = "amarillo"  # Esto dará un error
```

---

### **• DICCIONARIOS:**

Un diccionario es una colección no ordenada de elementos, que se definen entre llaves (`{}`) como pares clave-valor. Cada clave debe ser única en el diccionario, y los valores pueden ser cualquier tipo de dato.

Por ejemplo, aquí hay un diccionario de información de una persona:

```
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

Puedes acceder a los valores de un diccionario mediante su clave:

```
print(persona["nombre"])  # Output: "Juan"
print(persona["edad"])  # Output: 30
```

También puedes agregar, modificar o eliminar elementos de un diccionario:

```
persona["profesion"] = "Ingeniero"
persona["edad"] = 31
del persona["ciudad"]
```

---

### **CONCLUSIÓN**

En resumen, las listas, tuplas y diccionarios son estructuras de datos muy útiles en Python, cada una con sus propias características y usos. Las listas son útiles cuando necesitas una colección ordenada y mutable de elementos, las tuplas son útiles cuando necesitas una colección inmutable y los diccionarios son útiles cuando necesitas una colección no ordenada de elementos con claves únicas.

---

### **PRÓXIMO CONCEPTO: [`ARCHIVOS Y ENTRADA/SALIDA`](https://github.com/emilianod98/PythonChallenges-LowLevel/blob/main/conceptos_basicos/06-ArchivosEntradaSalida.md)**


<p align="center">
  <img src="../src/coffie.png">
</p>