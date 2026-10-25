"""
Requisitos:
1. Crear dos variables para nombre, profesión y ciudad
2. Crear dos variables para la remuneración de enero y febrero (mayor a 1500)
3. Crear una variable con la suma de enero y febrero
4. Mostrar el mensaje en pantalla
"""
# 1. Datos de dos personas: nombre, profesión y ciudad
nombre_a = "Lucía"
nombre_b = "Miguel"
profesion_a = "contadora"
profesion_b = "médico"
ciudad_a = "Trujillo"
ciudad_b = "Cusco"

# 2. Remuneración de enero y febrero (mayores a 1500)
remunera_a_enero = 2150
remunera_a_febrero = 1980

remunera_b_enero = 3200
remunera_b_febrero = 3450

# 3. Ingreso acumulado de los dos meses
total_a = remunera_a_enero + remunera_a_febrero
total_b = remunera_b_enero + remunera_b_febrero

# 4. Mostrar los mensajes
print("Hola soy {}, soy {} y mi remuneración acumulada es de {}".format(nombre_a, profesion_a, total_a))
print("Hola soy {}, soy {} y mi remuneración acumulada es de {}".format(nombre_b, profesion_b, total_b))