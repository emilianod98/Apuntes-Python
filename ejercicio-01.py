#Tiempo de los cursos
time_max = 7
time_min = 2.5
time_prome = 4
time_dalto = 1.5

#Diferencia de duración:
dif_min = 100 - time_dalto / time_min * 100
dif_max = round(100 - time_dalto / time_max * 100, 1)
dif_prome = 100 - time_dalto / time_prome * 100

#Mostrar los resultados:
print('-'*20)
print('EJERCICIOS 1 - A ¿Cuál es la diferencia de promedio de duración con otros cursos?')
print(f'La diferencia es un {dif_min}% menos que el curso más rápido.')
print(f'La diferencia es un {dif_max}% menos que el curso más lento.')
print(f'La diferencia es un {dif_prome}% menos que el curso promedio.')
print('-'*20)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Duracion de video sin editar.
crudo_prome = 5
crudo_dalto = 3.5

#Proncentajes de espacios vacios
vacio_prome = 100 - time_prome / crudo_prome * 100
vacio_dalto = round(100 - time_dalto / crudo_dalto * 100, 1)

#Mostrar los resultados.
print('EJERCICIOS 1 - B ¿Que porcentaje de material se reduce?')
print(f'El video contiene {vacio_prome}% de tiempo vacio.')
print(f'El video contiene {vacio_dalto}% de tiempo vacio.')
print('-'*20)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#¿Cuál sería la diferencia de ver 10 horas de otros cursos con el curso de Dalto?
print('EJERCICIOS 1 - C ¡10 hora de este curso!¿Equivalen a ver?')
print(f'Ver 10 horas del curso de Dalto equivalen a ver {round(time_prome / time_dalto * 10, 1)} horas de otros cursos.')
print(f'Ver 10 horas de otros cursos equivalen a ver {round(time_dalto / time_prome * 10, 1)} horas del curso de Dalto.')
print('-'*20)