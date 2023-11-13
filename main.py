import assets 
#Integrantes: 
#Alex Joel Cruz Rivas
#Erick Manuel Huanca Chimoy
#Luis Fernando Martinez Barbadillo
#Claudia Alejandra Olazabal Montoya
#Willian Puma Gutierrez
#Aaron Humberto Quintana Ordoñez
#Jhon Alexander Rosell Chiclayo
def main():
    print("main")
    print("Iniciando")
    results = assets.access() #La funcion que enciende el sistema
    assets.save() #a funcion que guarda los datos
    assets.send_arduino()

if __name__ == '__main__':
    main()
    
