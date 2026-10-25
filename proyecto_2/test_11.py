"""
Requisitos:
  1. Crear 4 variables, entre enteros, booleans, strings
  2. Condicionales: 2 casos true y 2 casos false
  3. En casos True, imprimir el valor de las otras variables
  4. En dos condicionales comparar variables (< o >)
"""
var_1 = 25
var_2 = 12
var_3 = "Lima"
var_4 = False

if var_1 > var_2:
    print("{} es mayor que {}".format(var_1, var_2))
    print(var_3)
    print(var_4)
if var_1 < var_2:
    print("{} es menor que {}".format(var_1, var_2))
if var_3:
    print("La ciudad es {}".format(var_3))
    print(var_1, var_2)
if var_4:
    print("Ingresó a la cuarta condicional")