#Le solicitamos al usuario que ingrese una frase (o varias)
frases = input('Rey/Reina escribime una frase o varias... ¡y te calculo el tiempo que tardarías en decirla!: ')

#Creamos una lista con todas las palabras escritas.
lista_palabras = frases.split(' ')

#Contamos todas las palabras utilizadas
cant_palabras = len(lista_palabras)

#En caso de que haya escrito algo que duré decirlo en más de un minuto le decimos que se zarpo!
if cant_palabras > 120:
    print('Rey/Reina te zarpaste!, tampoco me contes toda tu vida!')
    
#Le decimos el tiempo que tardaria en decir esa frase...
print(f'Rey/Reina dijiste {cant_palabras} palabras, lo cual tardarías {cant_palabras/2} segundos en decirlo!')