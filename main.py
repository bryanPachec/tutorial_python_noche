# Tipos de datos
# Numeros Enteros

numero1: int = 70
numero2 = 45

print(numero1)
print(numero2)

#Numeros Reales

numero3: float = 2.13
numero4 = 5.56
print(numero3)
print(numero4)

# Booleanos

esColombiano: bool = True
esArgentino = False
print(esColombiano)
print(esArgentino)

# Caracter y Cadena de caracteres

mensaje = "Cadena con una comilla simple ', una comilla doble \" y una diagonal invertida \\"
print(mensaje)


# Operadores
# Arimeticos

numero5 = 78
numero6 = 46
suma = numero5 + numero6
resta = numero5 - numero6
multiplicacion = numero5 * numero6
division = numero5 / numero6
modulo = numero5 % numero6
print( " La suma es: " , suma)
print( " La resta es: " , resta)
print( " La multiplicacion es: " , multiplicacion)
print( " La division es: " , division)
print( " el modulo es: " , modulo)

#Asignacion

x = 5
y = 7
z = 3

#Logicos
# and (y)

p = 5
print(p > 5 and p < 9)


#or (o)

q = 9
print( p < 7 or q < 9)

#not

print(not(q > 2 and p < 7))

# Relacionales

edad1 = 23
edad2 = 18

print( edad1 == edad2) # igualdad
print( edad1 > edad2) # mayor que
print( edad1 < edad2) # menor que
print( edad1 >= edad2) # mayor igual que
print( edad1 <= edad2) # menor igual que
print( edad1 != edad2) # no igual