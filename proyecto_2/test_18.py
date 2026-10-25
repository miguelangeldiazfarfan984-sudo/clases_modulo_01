# Nombre y apellido completo: Miguel Angel Diaz Farfan
# Participación a Práctica 02 - Listas en Python

"""
Requisitos:
1. Crear dos listas vacías usuario_1 y usuario_2 y agregar nombre, apellido, edad
   y profesión con append() e insert()
2. Operaciones:
   1. Sumar las edades de ambos usuarios mediante sus índices
   2. Concatenar ambas listas con + en una nueva lista llamada usuarios
   3. Invertir la lista usuarios con reverse()
   4. Eliminar la edad del primer usuario y el apellido del segundo usuario
   5. Modificar la profesión del segundo usuario mediante su índice
   6. Usar count() para contar un valor
   7. Usar copy() para copiar la lista actualizada
   8. Mostrar la lista original concatenada y la lista final
"""

# ---------- 1. CREACIÓN DE LISTAS ----------
# Se crean dos listas vacías
usuario_1 = []
usuario_2 = []

# Usuario 1: se agregan datos con append() e insert()
usuario_1.append("Miguel")        # ['Miguel']
usuario_1.append(28)              # ['Miguel', 28]
usuario_1.insert(1, "Diaz")       # inserta el apellido en el índice 1
usuario_1.append("Ingeniero")     # ['Miguel', 'Diaz', 28, 'Ingeniero']

# Usuario 2: se agregan datos con append() e insert()
usuario_2.append("Ana")
usuario_2.append("Torres")
usuario_2.append("Contadora")
usuario_2.insert(2, 31)           # inserta la edad en el índice 2

print("Usuario 1: {}".format(usuario_1))
print("Usuario 2: {}".format(usuario_2))

# ---------- 2. OPERACIONES ----------

# 2.1 Suma de edades usando sus índices (la edad está en el índice 2)
suma_edades = usuario_1[2] + usuario_2[2]
print("Suma de edades: {} + {} = {}".format(usuario_1[2], usuario_2[2], suma_edades))

# 2.2 Concatenación de ambas listas con el operador +
usuarios = usuario_1 + usuario_2
usuarios_original = usuarios.copy()   # se guarda la lista original para mostrarla al final
print("Lista concatenada: {}".format(usuarios))

# 2.3 Invertir el orden de la lista con reverse()
usuarios.reverse()
print("Lista invertida: {}".format(usuarios))

# 2.4 Eliminar elementos
# La edad del primer usuario (28) quedó en el índice 5 tras invertir: se elimina con pop()
edad_eliminada = usuarios.pop(5)
print("Edad eliminada del primer usuario: {}".format(edad_eliminada))
# El apellido del segundo usuario se elimina por su valor con remove()
usuarios.remove("Torres")
print("Lista después de eliminar: {}".format(usuarios))

# 2.5 Actualizar la profesión del segundo usuario (está en el índice 0)
usuarios[0] = "Administradora"
print("Lista con profesión actualizada: {}".format(usuarios))

# 2.6 Contar cuántas veces aparece un valor con count()
veces = usuarios.count("Miguel")
print("El valor 'Miguel' aparece {} vez(es)".format(veces))

# 2.7 Copiar la lista actualizada con copy()
usuarios_copia = usuarios.copy()
print("Copia de la lista: {}".format(usuarios_copia))

# 2.8 Mostrar resultados finales
print("Lista original concatenada: {}".format(usuarios_original))
print("Lista final modificada: {}".format(usuarios))