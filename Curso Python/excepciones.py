
def multiplica():
    while True:
        a = input("Dame el primer numero: ")
        b = input("Dame el segundo numero: ")

        try:
            resultado = int(a) * int(b)
        except ValueError as e:
            print("Error intenta de nuevo: ")
            print(f"Error: {e}")
        else:
            break
    return resultado


print(multiplica())
