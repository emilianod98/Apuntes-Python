#Succesión de Fibonacci:
def fibonacci(numero):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(numero):
        if b > numero: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b, a+b
            
resultado = fibonacci(34)
print(resultado)