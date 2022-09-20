"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
import config as cf
from DISClib.ADT import list as lt
from datetime import datetime
from filecmp import cmp
from hashlib import new
from platform import platform
import config as cf
from DISClib.ADT import list as lt
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Modelos

def new_catalog():
    """
    Crea un nuevo catálogo.
    """
    catalog = {'amazon':None,'netflix':None, "hulu":None, 'disney':None,'actors':None, 'titles': None}
        
    catalog['titles'] = lt.newList()
    catalog['amazon'] = lt.newList()
    catalog['netflix'] = lt.newList()
    catalog['hulu'] = lt.newList()
    catalog['disney'] = lt.newList()
    return catalog

# Funciones para agregar informacion al catalogo

def addMovie(catalog, movie):
    lt.addLast(catalog['titles'], movie)

    act = movie['cast'].split(',')

    for actor in act:
        addMovieActor(catalog, actor.strip(), movie)
    return catalog

def addMovieActor(catalog, actorname, movie):
    actors = catalog['actors']
    posactor = lt.isPresent(actors, actorname)
    if posactor > 0:
        actor = lt.getElement(actors, posactor)
    else:
        return None
    lt.addLast(actor['movies'], movie)
    return catalog

def addinfo_amazon(catalog, video):
    lt.addLast(catalog['amazon'], video)

    return catalog

def addinfo_netflix(catalog, video):
    lt.addLast(catalog['netflix'], video)

    return catalog

def addinfo_hulu(catalog, video):
    lt.addLast(catalog['hulu'], video)

    return catalog

def addinfo_disney(catalog, video):
    lt.addLast(catalog['disney'], video)

    return catalog

def addMediaTitles(catalog, video, streaming):
    video['streaming'] = streaming
    lt.addLast(catalog['titles'], video)

    return catalog

# Funciones para creacion de datos

def changeListType(catalog, type:str):
    catalog['amazon'] = lt.newList(type)
    catalog['netflix'] = lt.newList(type)
    catalog['hulu'] = lt.newList(type)
    catalog['disney'] = lt.newList(type)
    catalog['titles'] = lt.newList(type)

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
