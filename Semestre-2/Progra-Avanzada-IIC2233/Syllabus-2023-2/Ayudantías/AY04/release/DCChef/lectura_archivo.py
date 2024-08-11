from collections import defaultdict
from os import path


def cargar_pedidos(ruta_archivo):
	with open(ruta_archivo, "r", encoding="utf-8") as file:
		for line in file:
			id_mesa, *pedidos = line.strip().split(",")
			yield (id_mesa, pedidos)


def cargar_ingredientes(ruta_archivo):
	with open(ruta_archivo, "r", encoding="utf-8") as file:
		dict_ingredientes = dict()
		for line in file:
			nombre_pedido, *ingredientes = line.strip().split(",")
			ingredientes = [(ingrediente.split(";")[0], ingrediente.split(";")[1]) for
			                ingrediente in ingredientes]
			dict_ingredientes[nombre_pedido] = ingredientes
	return dict_ingredientes


def generar_bodega(dict_ingredientes):
	dict_bodega = defaultdict(int)
	for pedido in cargar_pedidos(path.join("data","pedidos.csv")):
		for item in pedido[1::][0]:
			for ingrediente in dict_ingredientes[item]:
				dict_bodega[ingrediente[0]] += int(ingrediente[1])
	return dict_bodega