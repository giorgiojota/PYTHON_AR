# Curso Python AR
# Mi progreso en el curso de Python - Academia AR
# Fecha: 21 de junio de 2026

print("Hola, este es mi primer script del curso AR")
print("Aquí iré registrando mis avances")

""" # Lección 1: Variables y tipos de datos
nombre = "Giorgio"
edad = 40
print(f"Me llamo {nombre} y tengo {edad} años")

# Lección 2: Listas
lenguajes = ["Python", "JavaScript", "Bash"]
print(f"Estoy aprendiendo: {', '.join(lenguajes)}")

# Lección 3: Funciones
def saludar(nombre):
    return f"Hola, {nombre}!"   
print(saludar(nombre))
 """


#Clase 3 Fundamentos del lenguaje Python
#Clase 03 Fundamentos del Lenguaje

#Ejercicios Estructura repetitiva while
#Problemas propuestos

#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
#cuántos tienen notas mayores o iguales a 7 y cuántos menores.

""" contador_mayores = 0
contador_menores = 0
i = 0
while i < 10:
    nota = float(input("Ingrese la nota del alumno: "))
    if nota >= 7:
        contador_mayores += 1
    else:
        contador_menores += 1
    i += 1

print(f"Alumnos con notas mayores o iguales a 7: {contador_mayores}")
print(f"Alumnos con notas menores a 7: {contador_menores}")
 """
#Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)

""" termino = 0
while termino < 25:
    termino += 1
    print(11 * termino) """

""" for i in range(1, 26):
    termino = 11 * i
    print(termino) """

#•Se ingresan un conjunto de n alturas de personas por teclado. 
# Mostrar la altura promedio de las personas.

""" n = int(input("Ingrese la cantidad de personas: "))
suma_alturas = 0
for i in range(n):
    altura = float(input("Ingrese la altura de la persona: "))
    suma_alturas += altura  
promedio = suma_alturas / n
print(f"La altura promedio de las personas es: {promedio:.2f} metros")
 """

#•Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
""" for x in range(8, 501, 8):
    print(x) """

#•Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

""" lista1 = []
lista2 = [] 
for i in range(15):
    valor1 = float(input("Ingrese un valor para la lista 1: "))
    lista1.append(valor1)
    valor2 = float(input("Ingrese un valor para la lista 2: "))
    lista2.append(valor2)

suma1 = sum(lista1)
suma2 = sum(lista2)

if suma1 > suma2:
    print("Lista 1 mayor")
elif suma2 > suma1:
    print("Lista 2 mayor")
else:
    print("Listas iguales") """

#•Desarrollar un programa que permita cargar n números enteros 
# y luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional (este
#operador retorna el resto de la división de dos valores, por ejemplo 11%2
#retorna un 1):

""" n = int(input("Ingrese la cantidad de números enteros: "))
pares = 0
impares = 0

for _ in range(n):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Valores pares: {pares}")
print(f"Valores impares: {impares}") """

#Ejercicios Estructura repetitiva for
#Problemas propuestos resolver con FOR

#Confeccionar un programa que lea n pares de datos, 
# cada par de datos corresponde a la medida de la base y la altura de un triángulo. 
# El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

""" n = int(input("Ingrese la cantidad de triángulos: "))
contador_superficie_mayor_12 = 0
for i in range(n):
    base = float(input(f"Ingrese la medida de la base del triángulo {i+1}: "))
    altura = float(input(f"Ingrese la medida de la altura del triángulo {i+1}: "))
    superficie = (base * altura) / 2
    print(f"Triángulo {i+1}: Base = {base}, Altura = {altura}, Superficie = {superficie:.2f}")
    
    if superficie > 12:
        contador_superficie_mayor_12 += 1
print(f"Cantidad de triángulos con superficie mayor a 12: {contador_superficie_mayor_12}")
 """

#Desarrollar un programa que solicite la carga de 10 números 
# e imprima la suma de los últimos 5 valores ingresados.
""" 
numeros = []
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

suma_ultimos_5 = sum(numeros[5:])
print(f"La suma de los últimos 5 valores ingresados es: {suma_ultimos_5}") """

#•Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)

""" print("Tabla de multiplicar del 5:")
for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")

for i in range(5, 51, 5):
    print(i) """

#•Confeccionar un programa que permita ingresar un valor del 1 al 10 
# y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
#Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

""" valor = int(input("Ingrese un valor del 1 al 10: "))
if 1 <= valor <= 10:
    print(f"Tabla de multiplicar del {valor}:")
    for i in range(1, 13):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")
else:
    print("Valor ingresado no válido. Por favor, ingrese un número del 1 al 10.")   """ 

#Realizar un programa que lea los lados de n triángulos, e informar:
#De cada uno de ellos, 
#a)qué tipo de triángulo es
#equilátero (tres lados iguales)
#isósceles (dos lados iguales), o 
# escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.

""" n = int(input("Ingrese la cantidad de triángulos: "))
contador_equilatero = 0
contador_isosceles = 0      
contador_escaleno = 0

for i in range(n):
    lado1 = float(input(f"Ingrese el lado 1 del triángulo {i+1}: "))
    lado2 = float(input(f"Ingrese el lado 2 del triángulo {i+1}: "))
    lado3 = float(input(f"Ingrese el lado 3 del triángulo {i+1}: "))

    if lado1 == lado2 == lado3:
        print(f"Triángulo {i+1} es equilátero.")
        contador_equilatero += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(f"Triángulo {i+1} es isósceles.")
        contador_isosceles += 1
    else:
        print(f"Triángulo {i+1} es escaleno.")
        contador_escaleno += 1
print(f"Cantidad de triángulos equiláteros: {contador_equilatero}")
print(f"Cantidad de triángulos isósceles: {contador_isosceles}")
print(f"Cantidad de triángulos escalenos: {contador_escaleno}") """

#Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
#Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

""" cantidad_puntos = int(input("Ingrese la cantidad de puntos a procesar: "))
contador_cuadrante1 = 0
contador_cuadrante2 = 0
contador_cuadrante3 = 0
contador_cuadrante4 = 0
for i in range(cantidad_puntos):
    x = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
    y = float(input(f"Ingrese la coordenada y del punto {i+1}: "))

    if x > 0 and y > 0:
        contador_cuadrante1 += 1
    elif x < 0 and y > 0:
        contador_cuadrante2 += 1
    elif x < 0 and y < 0:
        contador_cuadrante3 += 1
    elif x > 0 and y < 0:
        contador_cuadrante4 += 1

print(f"Puntos en el primer cuadrante: {contador_cuadrante1}")
print(f"Puntos en el segundo cuadrante: {contador_cuadrante2}")
print(f"Puntos en el tercer cuadrante: {contador_cuadrante3}")
print(f"Puntos en el cuarto cuadrante: {contador_cuadrante4}") """


#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

contador_negativos = 0
contador_positivos = 0
contador_multiplos_15 = 0
acumulado_pares = 0 
for i in range(10):
    valor = int(input(f"Ingrese el valor entero {i+1}: "))
    if valor < 0:
        contador_negativos += 1
    elif valor > 0:
        contador_positivos += 1
    if valor % 15 == 0:
        contador_multiplos_15 += 1
    if valor % 2 == 0:
        acumulado_pares += valor

print(f"Cantidad de valores ingresados negativos: {contador_negativos}")
print(f"Cantidad de valores ingresados positivos: {contador_positivos}")
print(f"Cantidad de múltiplos de 15: {contador_multiplos_15}")
print(f"Valor acumulado de los números ingresados que son pares: {acumulado_pares}")   

#Se cuenta con la siguiente información:
#Las edades de 5 estudiantes del turno mañana.
#Las edades de 6 estudiantes del turno tarde.
#Las edades de 11 estudiantes del turno noche.
#Las edades de cada estudiante deben ingresarse por teclado.
#a) Obtener el promedio de las edades de cada turno (tres promedios)
#b) Imprimir dichos promedios (promedio de cada turno)#
#c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

""" promedio_manana = 0
promedio_tarde = 0
promedio_noche = 0
suma_manana = 0
suma_tarde = 0
suma_noche = 0
for i in range(5):
    edad = int(input(f"Ingrese la edad del estudiante {i+1} del turno mañana: "))
    suma_manana += edad
for i in range(6):
    edad = int(input(f"Ingrese la edad del estudiante {i+1} del turno tarde: "))
    suma_tarde += edad
for i in range(11):
    edad = int(input(f"Ingrese la edad del estudiante {i+1} del turno noche: "))
    suma_noche += edad
promedio_manana = suma_manana / 5
promedio_tarde = suma_tarde / 6 
promedio_noche = suma_noche / 11
print(f"Promedio de edades del turno mañana: {promedio_manana:.2f}")
print(f"Promedio de edades del turno tarde: {promedio_tarde:.2f}")
print(f"Promedio de edades del turno noche: {promedio_noche:.2f}")
if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("El turno mañana tiene el promedio de edades mayor.") 
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene el promedio de edades mayor.")
elif promedio_noche > promedio_manana and promedio_noche > promedio_tarde:
    print("El turno noche tiene el promedio de edades mayor.") """
