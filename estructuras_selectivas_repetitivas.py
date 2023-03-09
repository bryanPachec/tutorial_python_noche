# Estructuras selectivas y repetitivas

#Selectivas

#if

numero = int(input("Ingrese un número"))
if numero>5:
    print("El numero es mayor a 5 ")


#if else

numero1 = int(input("Ingrese el primer número "))
numero2 = int(input("Ingrese el segundo número "))

if numero1 > numero2:
    print("el numero mayor es: ",numero1)
else:
    print("el numero mayor es: ",numero2)


#elseif

nota1 = float(input("Ingrese la primer nota "))
nota2 = float(input("Ingrese la segunda nota "))
nota3 = float(input("Ingrese la tercer nota "))

promedio = (nota1+nota2+nota3)/3

if promedio >=4:
    print("Su promedio es alto")
else:
    if promedio >=3:
        print("Su promedio es medio")
    else:
        print("su promedio es bajo")


#Repetitivas
# While

empleados = int(input("Cuantos empleados tiene la empresa "))
x=1
menor= 0
mayor= 0
total= 0
while x<=empleados:
    sueldo = int(input("Ingrese el sueldo del empleado "))
    if sueldo <=500:
        menor= menor+1
    else:
        mayor= mayor+1
    total = total+ sueldo
    x = x+1

print("Los empleados con un suelo menor o igual a 500 son: " , menor)
print("Los empleados con un suelo mayor a 500 son: " , mayor)
print("La empresa paga a todos sus empleados un total de: " , total)


# For

empleados = int(input("Cuantos empleados tiene la empresa "))
menor= 0
mayor= 0
total= 0
for x in range(empleados):
    sueldo = int(input("Ingrese el sueldo del empleado"))
    if sueldo <= 500:
        menor = menor+1
    else:
        mayor = mayor+1
    total= total + sueldo
print("Los empleados con un suelo menor o igual a 500 son: " , menor)
print("Los empleados con un suelo mayor a 500 son: " , mayor)
print("La empresa paga a todos sus empleados un total de: " , total)
