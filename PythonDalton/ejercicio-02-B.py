# EJERCICIO 02-B:
print('-'*20)
print('EJERCICIOS 2 - B: Crear una función que me devuelva todos los números primos del 0 hasta el número ingresado!')

def verificar_si_es_primo(numero):
    for i in range(2,numero):
        if numero%i == 0: return False
    return True

def verificar_primos (numero):
    numeros_primos = []
    for i in range(3, numero+1):
        resultado = verificar_si_es_primo(i)
        if resultado == True: numeros_primos.append(i)
    return numeros_primos

comprobar_funcion = verificar_primos(99)
print(comprobar_funcion)