# Tupla -> tuple
# Inmutable

tupla1 = (3,4,5,6)
print(tupla1)
print(type(tupla1))

# Accediendo a los elementos de la tupla
print(tupla1[0])

# Tuplas con diferenctes tipos de datos
tupla2 = (True, 25, 'hola')
print(tupla2)

# Averiguar si el em\lemento se encuentra o no en una lista





# Métodos de la tupla
print(tupla1.index(3))
# en caso de no estar indexado, devuelve error
print('Tamaño de una tupla', len(tupla1))
print('Cuántos números 6 están en la tupla 1', tupla1.count(6))

# Descompresión
dimensiones = (500,600)
dimensionX, dimensionY = dimensiones
print(dimensionX)
print(dimensionY)