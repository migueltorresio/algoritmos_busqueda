objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo: #Enumera todas las soluciones posibles
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo: #Evalúa las soluciones de acuerdo a las restricciones del problema
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raíz cuadrada exacta') 
