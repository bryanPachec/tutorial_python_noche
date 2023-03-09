#  Como crear un diccionario

persona= {'nombre': 'Brayan', 'edad': 26, 'correo' : 'brayan.pacheco@unividafup.edu.co'}
print(persona)

# Como accceder a un diccionario

print(persona['nombre']) # 1 forma
print(persona.get('edad')) # 2 forma

# Como modificar un diccionario

persona['nombre'] = 'Armando'
print(persona)

# Imprime los key del diccionario
for x in persona:
    print(x)

# Impre los value del diccionario
for x in persona:
    print(persona[x])

# Imprime los key y value del diccionario
for x, y in persona.items():
    print(x, y)