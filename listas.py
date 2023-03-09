# Listas

# Listas con enteros

listaEntero = [2,5,8,9]
print(listaEntero)

# Listas con Decimales

listaDecimal = [2.33,4.5,63.2]
print(listaDecimal)
# listas con Cadenas o String

listaString = ["Manzana","Pera","Uvas","Mango"]
print(listaString)


# Listas dentro de listas

lista1 = [1,2,4,5,["Perros", 15]]
print(lista1)

# ejemplo de uso de lista

alumnos = []
notas = []

for x in range(5):
    nombre = input("Ingrese el nombre del alumno ")
    nota = float(input("Ingrese la nota del alumno "))
    alumnos.append(nombre)
    notas.append(nota)

for x in range(5):
    print(alumnos[x]+" "+str(notas[x]))

