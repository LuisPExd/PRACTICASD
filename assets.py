import reads
num_gate = 2
in_gate = 0 #Inicialmente la puerta esta cerrada



def access():
    dni = input('Ingrese DNI: ') #Esto puede ser reemplazado por un sensor
    reserve = reads.dni_read(dni)
    if reserve == [0,0] and reads.search(dni) == False: #Esta funcion permite que el usuario reserve
        print("El DNI no es esta en la base de datos o no tiene 8 digitos")
        print("Ingrese un DNI que si esta en la bd")
        access()
    #Cuando esta en la bd pero no tiene reserva
    elif reserve == [0,0] and reads.search(dni) == True:
        _action = input('Ingresa s o n para definir si quieres reservar ahora: ')
        if _action == 's':
            access_val = reads.reservation_now()[1] #Esta funcion permite que el usuario reserve en ese momento porque su DNI si esta en la bd
            gate = reads.reservation_now()[0]
            return [access_val, gate]
        else:
            print("Ha decidido que no va a reservar")
            print("Iniciando el programa..")
            access()
    #Cuando si tiene reserva
    else: 
        access_val = reserve[0]
        gate = reserve[1]
        print("Si tiene reserva")
        print(f"Ha reservado la cancha {gate}")
        print(f"abriendo la cancha {gate}")
        access()
    return [access_val, gate]   #Puerta a abrir
        

def save():
    print("Guardando")
    return save

def send_arduino():
    import serial
    arduino = serial.Serial('/dev/ttyACMO', 9600)

    while True:
        comando = input("Introduce un comando: ")