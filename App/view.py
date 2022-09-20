"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate
from datetime import datetime

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController():
    control = controller.newController()
    return control

def printMenu():
    print("Bienvenid@")
    print("1- Elegir la el tipo de lista:'1' Arraylist, '2' Linkedlist")
    print("2- Cargar informacion de las plataformas")
    print("3- Listar las peliculas estrenadas en un periodo de tiempo")
    print("4- Listar programas de television agregados en un periodo de tiempo")
    print("5- Encontrar contenido donde participar un actor")
    print("6- Encontrar contenido producido en un pais")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el TOP de los generos con mas contenido")
    print("0- Salir")

catalog = None
"""
Menu principal
"""
