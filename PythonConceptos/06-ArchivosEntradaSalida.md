<p align="center">
  <img src="../src/Learn-python.png">
</p>


# ***TRABAJANDO CON ARCHIVOS EN PYTHON***

En Python, puedes trabajar con archivos para leer y escribir información en ellos. La entrada/salida (en inglés, I/O) se refiere al proceso de comunicación entre un programa y un dispositivo externo, como una pantalla o un archivo.

<br>

###  **• ABRIR UN ARCHIVO**

Para abrir un archivo en Python, puedes usar la función `open()`, que toma dos argumentos: el nombre del archivo y el modo en que se abrirá el archivo. El modo puede ser `r` (lectura), `w` (escritura) o `a` (anexar), dependiendo de lo que quieras hacer con el archivo.

Por ejemplo, para abrir un archivo llamado `datos.txt` en modo de lectura, puedes hacer lo siguiente:

```
archivo = open("datos.txt", "r")
```

---

###  **• LEER EL CONTENIDO DE UN ARCHIVO**

Una vez que tienes el archivo abierto, puedes leer su contenido o escribir en él. Para leer el contenido de un archivo, puedes usar el método `read()` del objeto de archivo:

```
contenido = archivo.read()
print(contenido)
```

---

###  **• ESCRIBIR EN UN ARCHIVO**

Para escribir en un archivo, puedes usar el método `write()` del objeto de archivo:

```
archivo.write("Este es un nuevo contenido para el archivo.")
```

---

###  **• CERRAR UN ARCHIVO**

Recuerda cerrar el archivo una vez que hayas terminado de trabajar con él, para liberar los recursos del sistema:

```
archivo.close()
```

---

###  **• ENTRADA/SALIDA POR CONSOLA**

Además de trabajar con archivos, Python también tiene funciones para la entrada/salida en la consola. Por ejemplo, para pedir al usuario que ingrese un valor por consola, puedes usar la función `input()`:

```
nombre = input("Ingresa tu nombre: ")
print("Hola, " + nombre + "!")
```

También puedes imprimir información en la consola usando la función `print()`:

```
print("Hola, mundo!")
```

---

###  **CONCLUSIÓN**

En resumen, en Python puedes trabajar con archivos para leer y escribir información en ellos, y también puedes usar funciones para la entrada/salida en la consola.

---

### **PRÓXIMO CONCEPTO: [`MÓDULOS Y PAQUETES`](https://github.com/emilianod98/PythonChallenges-LowLevel/blob/main/conceptos_basicos/07-ModulosPaquetes.md)**


<p align="center">
  <img src="../src/hacker.png">
</p>

