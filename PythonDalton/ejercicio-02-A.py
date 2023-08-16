# EJERCICIO 02-A:
print('-'*20)
print('EJERCICIOS 2 - A ¿Cúal es el nombre del profesor (+edad) y el asistente (-edad) de esta clase?')

# Creamos una funcion para solicitar los nombres y edades:
def quien_es_quien (cantidad_de_participantes):
    personas_integrantes = []
    for i in range(cantidad_de_participantes):
        nombre = input('Ingrese el nombre de los integrantes: ')
        edad = int(input('Ingrese la edad, del integrante ingresado anteriormente: '))
        print(f'El integrante ingresado fue {nombre} y su edad es: {edad}')
        persona = (nombre, edad)
        personas_integrantes.append(persona)
    personas_integrantes.sort(key=lambda x:x[1])
    asistente = personas_integrantes[0][0]
    profesor = personas_integrantes[-1][0]
    return asistente, profesor

print('-'*20)
asistente, profesor = quien_es_quien(5)
print(f'¡El Profesor de este curso se llama {profesor} y su asistente es {asistente}!')

