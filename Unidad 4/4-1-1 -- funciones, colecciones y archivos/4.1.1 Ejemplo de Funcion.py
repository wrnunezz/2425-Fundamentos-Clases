# funcion
# def suma (a,b):
#     return a+b
#
# # resultado
# resultado = suma(4,5)
# print("la suma es ", resultado )
################################################
# def saludar(nombre):
#     print(f" hola q tal , {nombre} como te va en clases")
#
# saludar("Vivi")
##############################################
# def saludar(nombre):
#     mensaje = f"Hola q tal ,{nombre} "
#     return mensaje
#
# ##llamr a la funcion
# saludo= saludar("Viviana")
# print(saludo)
################################################
# def saludar(nombre="Pedro"):
#     print(f" hola {nombre}")
#
# saludar()
# saludar("Juan")
################################################
# def sumageneral(*numeros):
#     return sum(numeros)
#
# sumatotal =sumageneral(1,5,6,80,50,20,5,2,6)
# print(sumatotal)
##############################################
def mostrar(**datos):
    for clave,valor in datos.items():
        print(f" {clave} {valor}")

mostrar(nombre="Juan",edad=20, telfono='09999999')