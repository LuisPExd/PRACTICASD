import data
import datetime as dt

bd = data.data
times = data.times

def search(dni):
    for i in range(len(bd)):
        if bd[i]['DNI'] == dni:
            print("Encontrado")
            return True
    else:
        return False
    

def val_dnitype(dni):
    #Puede ser 0 (cuando no esta en la base de datos) o 1 (el dni esta en la base de datos)
    if len(str(dni)) == 8:
        var_return = search(dni)
    else: 
        print("El DNI debe tener 8 digitos") #No esta en la base de datos
        var_return = False
    return var_return

def reserved_gate(dni):
    for i in range(len(bd)):
        if bd[i]['DNI'] == dni:
            gate = bd[i]['Gate']
    return gate

def have_permission(dni):
    for i in range(len(bd)):
        if bd[i]['DNI'] == dni:
            access = bd[i]['Reserva']
    return access

def day_():
    x = dt.date.today()
    x_str = f'{x.day}/{x.month}/{x.year}'
    return x_str

def time_():
    hour_ = dt.datetime.now()
    if int(hour_.hour)>12:
        str_hour = f'{hour_.hour-12}:00pm'
    elif int(hour_.hour)<12:
        str_hour = f'{hour_.hour-12}:00am'
    else:
        str_hour = f'{hour_.hour-12}:00m'
    return str_hour

def val_gate(day,time):
    #devuelve la primera puerta encontrada
    for day in times:
        if day['day'] == day_():
            for time in day['times']:
                if time['time'] == time:
                    for gate in time['gates']:
                        if gate['reserva'] == 0:
                            return gate['gate']
                        
def available_gate():
    _day = day_()
    _time = time_()
    return ['10/11/2023','9:00pm']


def dni_read(dni):
    print("Leyendo DNI")
    val_access = val_dnitype(dni) #Puede ser 0 (cuando no esta en la base de datos) o 1 (el dni esta en la base de datos)
    if val_access == True:
        gate = reserved_gate(dni)
        access = have_permission(dni) #Tiene acceso?
        return [access, gate]
    else:
        print("Usted no tiene acceso")
        return [0,0]
        

def reservation_now():
    ava_g = available_gate() #Habra alguna puesta disponible?
    #Si no hay puerta disponible => 0
    if ava_g == 0:
        print("No hay puerta disponible")
        return [0,0]
    else:
        print(f"Esta disponible la cancha de hoy {ava_g[0]} para las {ava_g[1]}")
        respuesta = input(f"¿Quiere reservar para ese horario? Escriba si o no: ")
        while respuesta != 'si' and respuesta != 'no':
            respuesta = input(f"Respuesta no valida. Escriba si o no: ")
        if respuesta == 'si':
            print("Ha reservado esa cancha")
            times[0]['times'][1]['gates'][0]['reserva'] = 1
            reserva = times[0]['times'][1]['gates'][0]['reserva']
            gate = times[0]['times'][1]['gates'][0]['gate']
            print(f"Abriendo puerta {gate}")
        else:
            print("Ok, no quiere reservar. Adios")
            gate = times[0]['times'][1]['gates'][0]['gate']
            reserva = 0
        return [gate, reserva]