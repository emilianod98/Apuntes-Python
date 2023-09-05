<p align="center">
  <img src="../src/Learn-python.png">
</p>


# ***OPERADORES***

Los operadores son símbolos o palabras reservadas que se utilizan para realizar operaciones en Python. Los operadores más comunes en Python son:

<br>

###  **• OPERADORES ARITMÉTICOS**

Los operadores aritméticos se utilizan para realizar operaciones matemáticas como la suma, la resta, la multiplicación y la división. Aquí están algunos ejemplos de operadores aritméticos en Python:

```
+  # Suma
-  # Resta
*  # Multiplicación
/  # División
%  # Módulo (obtiene el resto de una división)
** # Potencia (por ejemplo, 2**3 significa 2 elevado a la tercera potencia)
```

---

###  **• OPERADORES DE COMPARACIÓN**

Los operadores de comparación se utilizan para comparar dos valores y devolver un valor booleano (`True` o `False`). Algunos ejemplos de operadores de comparación son:

```
== # Igual a
!= # Diferente de
<  # Menor que
>  # Mayor que
<= # Menor o igual que
>= # Mayor o igual que
```

---

###  **• OPERADORES LÓGICOS**

Los operadores lógicos se utilizan para combinar expresiones booleanas y devolver un valor booleano. Aquí están algunos ejemplos de operadores lógicos en Python:

```
and  # Y
or   # O
not  # No
```

El operador `and` es un operador lógico binario que se utiliza para combinar dos expresiones booleanas y devuelve "True" (verdadero) solo si ambas expresiones son verdaderas. Si alguna de las expresiones es falsa, entonces el operador "and" devuelve "False" (falso). Por ejemplo, en la expresión "x > 5 and y < 10", si tanto x es mayor que 5 como y es menor que 10, entonces la expresión completa se evaluará como verdadera.

El operador `or` también es un operador lógico binario que se utiliza para combinar dos expresiones booleanas y devuelve "True" si al menos una de las expresiones es verdadera. Si ambas expresiones son falsas, entonces el operador "or" devuelve "False". Por ejemplo, en la expresión "x > 5 or y < 10", si x es mayor que 5 o y es menor que 10, entonces la expresión completa se evaluará como verdadera.

Por último, el operador `not` es un operador lógico unario que se utiliza para invertir el valor de una expresión booleana. Si la expresión es verdadera, entonces "not" la convierte en falsa, y si es falsa, entonces "not" la convierte en verdadera. Por ejemplo, en la expresión "not (x > 5)", si x es menor o igual a 5, entonces la expresión completa se evaluará como verdadera, porque "not" convierte la expresión "x > 5" en falsa.

---

Por ejemplo, podrías usar operadores aritméticos y de comparación juntos para hacer cálculos y comparaciones, como en el siguiente ejemplo:

```
a = 10
b = 5

# Suma de dos números
c = a + b

# Comparación de dos números
es_mayor = a > b

# Imprimir los resultados
print(c)  # Output: 15
print(es_mayor)  # Output: True
```

En este ejemplo, se asignan los valores 10 y 5 a las variables `a` y `b`, respectivamente. Luego, se usa el operador de suma (`+`) para sumar `a` y `b`, lo que resulta en el valor 15 que se asigna a la variable `c`. Luego, se usa el operador de comparación mayor que (`>`) para comparar `a` y `b`, lo que devuelve `True` ya que a es mayor que `b`. Por último, se imprimen los valores de `c` y `es_mayor` utilizando la función `print()`.

Es importante comprender cómo funcionan los operadores en Python, ya que te permiten realizar cálculos y comparaciones en tus programas. Con ellos, podrás crear programas más sofisticados y realizar operaciones más complejas. Ahora, si estás listo, podemos continuar con el siguiente concepto: 

### **[`ESTRUCTURAS DE CONTROL DE FLUJO:`](https://github.com/emilianod98/PythonChallenges-LowLevel/blob/main/conceptos_basicos/03-EstructurasdeControldeFlujo.md)**

<p align="center">
  <img src="../src/operadores.png">
</p>