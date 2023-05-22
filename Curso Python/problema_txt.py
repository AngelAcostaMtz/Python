

nombres = ["angel","angelito","Mathias","Diego"]
apellidos = ["Acosta","Martinez","Acosta","Martinez"]

with open("nombres_y_apellidos.txt","w") as archivo:
    archivo.writelines("Los datos son:\n\n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]