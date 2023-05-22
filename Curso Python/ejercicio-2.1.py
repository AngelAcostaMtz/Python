"""System module."""


# creando funcion para un asistente y su profesor segun la edad
def obtener_companeros(cantidad_compaeros):

    compaeros = []  # se crea la lista de los compañeros
    # se crea el for para pedir la informacion de los compañeros
    for i in range(cantidad_compaeros):
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        compañero = (nombre, edad)
        compaeros.append(compañero)  # se agrega la informacion a la lista
    # se ordenan de mayor a menor segun la edad
    compaeros.sort(key=lambda x: x[1])
    # devolviendo una tupla con nombre y edad, despues accedemos al nombre para definir el asistente y el profesor
    asis = compañero[0][0]
    maestro = compaeros[-1][0]
    return asis, maestro  # retornamos la tupla


# desempaquetamos lo que retorna la funcion
asistente, profesor = obtener_companeros(5)

print(f"El nombre del asistente es: {asistente}")  # mostrando el resultado
print(f"El nombre del profesor es: {profesor}")
