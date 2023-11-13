import assets 

def main():
    print("main")
    print("Iniciando")
    results = assets.access() #La funcion que enciende el sistema
    assets.save() #a funcion que guarda los datos
    assets.send_arduino()

if __name__ == '__main__':
    main()
    