def coche():
    return "Hoy soy un coche"

def motocicleta():
    return "Hey, soy una moto"


tipo_vehiculo = input("¿Qué tipo de vehículo quieres ser? (coche/motocicleta): ")


if tipo_vehiculo.lower() == "coche":
    resultado = coche()
elif tipo_vehiculo.lower() == "motocicleta":
    resultado = motocicleta()
else:
    resultado = "Tipo de vehículo no reconocido"


print(resultado)
