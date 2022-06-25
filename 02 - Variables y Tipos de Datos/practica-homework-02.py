#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
from telnetlib import STATUS


var01 = 73
print (var01)

#2) Imprimir el tipo de dato de la constante 8.5

var02 = 8.5
type (var02)

#3) Imprimir el tipo de dato de la variable creada en el punto 1

print (type(var01))

## 4) Crear una variable que contenga tu nombre

nombre01 = ("Federico")


## 5) Crear una variable que contenga un número complejo

var03 = 73 + 73j

## 6) Mostrar el tipo de dato de la variable crada en el punto 5

type(var03)

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

var04 = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var05 = 'True'
var06 = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

type(var05)
type(var06)


print ('la variable var05 es del tipo', type(var05), 'y la variable var06 es del tipo', type(var06) )

# 10) Asignar a una variable, la suma de un número entero y otro decimal

var07 = 8 + 0.5

# 11) Realizar una operación de suma de números complejos


var08 = 22 + 99j
var09 = 88 + 1j
print (var08 + var09)
#modifico para probar subier a github
var_prueba = 9

# 12) Realizar una operación de suma de un número real y otro complejo

var10 = 5 +7j
var11 = 10
print(var10 +var11)


# 13) Realizar una operación de multiplicación

5*5

print(5*5)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

var12 = 27/4
print (var12)

# 16) De la división anterior solamente mostrar la parte entera

var13 = 27//4
print(var13)

# 17) De la división de 27 entre 4 mostrar solamente el resto

print(27%4)
# o también

var14 = 27%4
print(var14)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print(6*4+3)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas


var15 = "32F"
var16 = "32F7"
print (var15 + var16)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

var17 = '2'
var18 = 2
print (var17==var18)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print (var17==str(var18))

#o también:

print (int(var17)==var18)

print (float(var17)==float(var18))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

#por la coma, debería ser con punto: 3.8

a = float(3.8)
print (a)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

var19 = 3
var19-=2
print(var19)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

1 << 2

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#no se permite porque son de distintos tipos
2 + int('2')
str(2) + '2'
float(2)+ float('2')

# 26) Realizar una operación válida entre valores de tipo entero y string

var20 = 4
var21 = " años"
print(var20 * var21)

#es decir NO SE PUEDE SUMAR número entero con string, PERO sí se puede multiplicar un string


#----------------------------------

