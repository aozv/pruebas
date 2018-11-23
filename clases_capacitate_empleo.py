"""Este es un encabezado de inicio"""
# -*- coding: UTF-8 -*-
__author__ = 'Arturo'
# Programa de Prueba

print("esto es una prueba de escritura en Python")

# Estructuras de datos en Python
# ================================


# ------------------------------------------------------------------------------
# Listas:
# ------------------------------------------------------------------------------
# variable = [elemento_0, elemento_1, elemento_2, elemento_n ]
# donde elemento puede ser "texto", numero, variable u otra [lista]

robot1 = ["bipedo", 6, ["caminar", "correr", "saltar"]]
variable1 = robot1[1]
variable2 = robot1[2][1]
print()
print("************* LISTAS ****************************************************")
print("Este es el valor del elemento 1 de la lista:", variable1)
print("este es el valor del elemento 1 dentro de la lista 2:", variable2)

robot1[2][1] = "trotar"
print("este es el valor de la lista robot1 cambiada: ", robot1)

# ------------------------------------------------------------------------------
# Tuplas
# ------------------------------------------------------------------------------
# variable = (elemento_0, el emento_1, elemento_2, elemento_n )
# donde elemento puede ser "texto", numero, variable u otra (tupla) y
# no se pueden añadir o modificar sus elementos, mantiene el contenido estatico.

robot2 = ("bipedo", 6, ("caminar", "correr", "saltar"))
print()
print("************* TUPLAS  **************************************************")
print("Este es el valor de la tupla: ", robot2)
print("Este es el valor del elemento 1 dentro de la tupla robot2: ", robot2[2][1])

# ------------------------------------------------------------------------------
# Diccionarios
# ------------------------------------------------------------------------------
# variable = {clave_0 : elemento 0,
#             clave_1 : elemento 1,
#             clave_2 : elemento 2,
#             clave_n : elemento n
# }

# las claves pueden ser textos, numeros y tuplas
# los elemento pueden ser  textos, numeros, variables, tuplas y listas
# solo se pueden cambiar los valores de los elementos pero No las claves

robot3 = {"clave_1": "bipedo",
          2: 6,
          (1, 2): ["camina", "correr", "saltar"]
          }
variable3 = robot3["clave_1"]
variable4 = robot3[2]
variable5 = robot3[(1, 2)][2]
print()
print("************* DICCIONARIOS  *********************************************")
print(variable3)
print(variable4)
print(variable5)

# Instrucciones de decisión lógica
# ==================================
print()
print("************* DECISIONES LOGICAS  ***************************************")
# ------------------------------------------------------------------------------
# condicionales simples
# ------------------------------------------------------------------------------

libros = int(input("cuantos libros lees anupralmente?: "))
if libros >= 15:
    print("Eres un buen lector")
else:
    print("necesitas leer mas!")

y = input("Presione Enter para continuar.")

# ------------------------------------------------------------------------------
# condicionales anidados
# ------------------------------------------------------------------------------

pregunta = input("Trabajas desde casa?: (si/no)")
if pregunta == "si":
    print("Eres afortunado")

if pregunta == "no":
    print("Trabajas fuera de casa")
    tiempo = int(input("Cuantos minutos haces al trabajo?: "))
    if tiempo == 0:
        print("trabajas desde casa.")
    elif 0 < tiempo <= 20:
        print("Es poco tiempo")
    elif 21 <= tiempo <= 45:
        print("Es un tiempo razonable!!")
    else:
        print("Busca otras rutas!!!!")

y = input("Presione Enter para continuar.")

# Instrucciones de repeticion
# ==================================

# ------------------------------------------------------------------------------
# while
# ------------------------------------------------------------------------------

# tabla del 7
print("Tabla del 7 usando WHILE:")
i = 1
while i <= 10:
    tabla = 7 * i
    print("7 x ", i, " = ", tabla)
    i = i + 1

y = input("Presione Enter para continuar.")

# ------------------------------------------------------------------------------
# for
# ------------------------------------------------------------------------------

print("Tabla del 7 usando FOR:")
for j in range(1, 11, 1):
    print("7 x ", j, " = ", 7 * j)

y = input("Presione Enter para continuar.")

# ------------------------------------------------------------------------------
# for para leer listas o textos
# ------------------------------------------------------------------------------
k = 0
lector = {}
for letras in "prueba de lectura en textos":
    print(letras)
    lector[k] = letras
    k = k + 1

print("aqui se imprime un valor del diccionario dinamico: ", lector[5])
print()
print("la cantidad de letras leidas fueron: ", k)

y = input("Presione Enter para continuar.")


# ------------------------------------------------------------------------------
# FUNCIONES
# ------------------------------------------------------------------------------

# AREA DEL CUADRADO
def areaCuadrado():
    lado = int(input("introduzca el valor del lado del cuadrado: "))
    acuadrado = lado ** 2
    print("El area del Cuadrado es: ", acuadrado)


# AREA CIRCULO
def areaCirculo():
    radio = int(input("introduzca el valor del lado del radio: "))
    pi = 3.141516
    acirculo = pi * radio ** 2
    print("El area del Circulo es: ", acirculo)


i = True
while i == True:
    area = input("Elije una figura para calcular su area: \nCuadrado = 1 \nCirculo = 2\n")
    if area == "1":
        areaCuadrado()
    elif area == "2":
        areaCirculo()
    else:
        print("Ingrese una opcion valida")
        i = bool(input("\nQuiere calcular otra area?:\nSi = True \nNo = False\n"))


# Programacion orientada a Objetos
# =======================================

# Nota: el nombre de una clase empieza en mayusculas por convencion y la linea termina con ":"

class Persona:

    # se tiene que definir el metodo constructor de la clase si lo hubiere para los atributos (usar siempre self)
    def __init__(
            self):  # Se puede definir el constructor con parametros __init__(self,variable1, variable2,etc...) pero siempre usar self
        self.nombre = "Arturo"
        self.edad = 47
        # self.variable1 = variable1
        # self.variable1 = variable2
        print("se creo a: ", self.nombre, "de ", self.edad, " anios")

    # despues del consttructor se puede crear otros metodos siempre usando self para referenciar las variables
    def hablar_de(self,
                  palabras):  # Se puede colocar un valor prederterminado al parametro "palabras" (palabras="esto es un texto predeterminado")
        print(self.nombre, ": ", palabras)


# Aqui se crea el objeto Arturo instanciando la clase Persona
Arturo = Persona()

# aqui se hace el llamado a un metodo de la clase Persona del objeto Arturo
# Arturo.hablar_de() este llamado al metodo funciona si de tiene un valor predeterminado en la variable "palabras" del metodo "hablar_de"
Arturo.hablar_de("estoy hablando un poco en este metodo")

# ------------------------------------------------------------------------------
# Herencia
# ------------------------------------------------------------------------------
