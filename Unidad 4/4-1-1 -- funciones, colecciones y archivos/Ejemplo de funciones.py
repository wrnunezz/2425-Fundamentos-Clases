# funciones
# def suma(a,b):
#     resp = a+b
#     return resp
# # resultado
# resultado = suma(5,10)
# print(f"la suma es ",resultado)

# def saludar(nombre):
#     print(f" hola q tal ,{nombre} como estas")
#
# saludo = saludar("Ana")
#
# def saludar(nombre):
#     mensaje= f"Hola srs Estudiante {nombre}"
#     return mensaje
# ## llamr a la funcion
# saludo = saludar("Clara")
# print(saludo)

####### Función ######
# def saludar(nombre ="Juan"):
#     print(f"hola {nombre}")
#
# saludo=saludar()
# saludo =saludar("chicos")

######## funciones con varios argumentos ########
def sumageneral(*numeros):
    respuesta = sum(numeros)
    return respuesta
sumatotal= sumageneral(1,3,5,10,20,30,1,4,5,4,8,6,8)
print(sumatotal)
