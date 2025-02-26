# crear listas

# Autor: Donato Ramos Martínez

# Crear lista
frutas=["manzanas","pera","uva","sandía","melón"]
print(frutas)
# acceder a los elementos de la lista. Comienzas siempre en el índice 0
print(frutas[1]) # Nos da pera
# acceder al último elemento
print(frutas[-1])
# Coloca la primera letra en mayúscula
print(frutas[1].title())
print(frutas[1].lower())
print(frutas[1].upper())
# usar valores individuales de una lista
mensaje=f"Mi fruta favorita es {frutas[1].title()}."
print("mensaje")
# modificar elementos de la lista
frutas[0]="fresa"
print(frutas) # sustituye el elemento manzana por fresa
mensaje=f"Mi fruta favorita es {frutas[0].title()}."
print(mensaje)
# agregar un elemento al final de la lista
frutas.append("naranja")
print(frutas)
coches=[]
coches.append("audi")
coches.append("bmw")
coches.append("subaru")
coches.append("toyota")
coches.append("nissan")

print(coches)

# insertar un elemento a la lista en el índice 0 y lo sobrescribe
frutas.insert(0,"plátano")
print(frutas)
coches.insert(2,"ford")
print(coches)

# creamos una lista para practicar
equipos=[];
equipos.append("barcelona");
equipos.insert(0,"celta de vigo")
equipos.append("real madrid")
equipos.insert(1,"atlético de madrid")
print(equipos)
# eliminar un elemento de la lista
elemento=frutas.pop()
print(elemento)
print(frutas)
# eliminar por índice
primera_fruta=frutas.pop(0)
# supuestamente se recoge el valor de la fruta, pero ésta queda inutilizada y, cuanto se vuelva a recargar la lista desaparecerá
print(primera_fruta)
print(frutas)
print(coches)
coche_eliminado=coches.pop(2)
print(f"El coche eliminado es el {coche_eliminado}")
print(coches)
# Eliminar un método específico
frutas.remove("uva")
print(frutas)

print(f"las frutas más importantes\n\t{frutas[1].title()}\n\t{frutas[2].title()}")

# ordenar la lista
print(frutas)
frutas.sort()
print(frutas)
frutas.sort(reverse=True)
print(frutas)
# sorted() para ordenar una lista temporalmente
print("Lista original")
print(frutas)
print("Lista ordenada")
print(sorted(frutas))

# cantidad de elementos en una lista
print("La lista de frutas tiene "+str(len(frutas))+" elementos")