
# with open("archivos\\texto_de_angel.txt",encoding="UTF-8") as archivo:
#     print(archivo.read())

#se agregan permisos para escribir en el archivo con la letra w, que sobreescribe completamente el archivo, a di
#a diferencia de la a que escribe pero agregando lineas al archivo de txt

with open('archivos\\texto_de_angel.txt','a',encoding="UTF-8") as archivo:
    
    for i in range(5):
       archivo.write("prueba de escritura\n")
       
    # print(archivo.read())
