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

from DISClib.ADT import list as lt
from datetime import datetime
from filecmp import cmp
from hashlib import new
from platform import platform
import config as cf
from DISClib.ADT import list as lt
import time
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Modelos

def newCatalog():
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

    for ac in act:
        addMovieActor(catalog, ac.strip(), movie)
    return catalog

def addMovieActor(catalog, actorname, movie):
    act = catalog['actors']
    posact = lt.isPresent(act, actorname)
    if posact > 0:
        actor = lt.getElement(act, posact)
    else:
        return None
    lt.addLast(actor['movies'], movie)
    return catalog

def addinfo_amazon(catalog, vid):
    lt.addLast(catalog['amazon'], vid)

    return catalog

def addinfo_netflix(catalog, vid):
    lt.addLast(catalog['netflix'], vid)

    return catalog

def addinfo_hulu(catalog, vid):
    lt.addLast(catalog['hulu'], vid)

    return catalog

def addinfo_disney(catalog, vid):
    lt.addLast(catalog['disney'], vid)

    return catalog

def addMediaTitles(catalog, vid, streaming):
    vid['streaming'] = streaming
    lt.addLast(catalog['titles'], vid)

    return catalog

# Funciones para creacion de datos

def changeListType(catalog, type:str):
    catalog['amazon'] = lt.newList(type)
    catalog['netflix'] = lt.newList(type)
    catalog['hulu'] = lt.newList(type)
    catalog['disney'] = lt.newList(type)
    catalog['titles'] = lt.newList(type)

#Consultas

def getTitulos(catalog):

    titulos = catalog['titles']
    someTit = lt.newList()
    for i in range(6):
        tit = lt.getElement(titulos, i)
        lt.addLast(someTit, tit)
    return someTit

def getAllTit(catalog):

    titles = catalog['titles']
    allTitles = lt.newList()
    for i in range(lt.size(titles)):
        title = lt.getElement(titles, i)
        lt.addLast(allTitles, title)
    return allTitles

# Obtener peliculas por actor
def getMoviesByActor(movies,actor):
    start = getTime()
    sort = ms.sort(movies, cmpMoviesByReleaseYear)
    moviesByActor = lt.newList()
    mov= 0
    ser = 0
    for i in range(lt.size(sort)):
        movie = lt.getElement(sort, i)
        if actor.lower() in movie['cast'].lower():
            lt.addLast(moviesByActor, movie)
            if movie['type'] == 'Movie':
                mov += 1
            else:
                ser += 1
    end_time = getTime()
    deltatime = deltaTime(start, end_time)
    return moviesByActor, deltatime, mov , ser

#Obtener peliculas por pais
   
#Obtener contenido por director especifico
def getContentByDirector(movies,director):
    start = getTime()
    movies = ms.sort(movies, cmpMoviesByReleaseYear)
    moviesByDirector=lt.newList()
    for i in range(lt.size(movies)):
        movie=lt.getElement(movies,i)
        if movie['director'].lower() == director.lower():
            lt.addLast(moviesByDirector,movie)

    cuenta_movie=0
    cuenta_show=0
    cuenta_amazon=0
    cuenta_netflix=0
    cuenta_hulu=0
    cuenta_disney=0
    dic_generos={}

    for i in range(lt.size(moviesByDirector)):
        movie=lt.getElement(moviesByDirector,i)

        
        if movie['type'] == "Movie":
            cuenta_movie+=1
        elif movie['type'] == "TV Show":
            cuenta_show+=1

        if movie['streaming'] == "amazon":
            cuenta_amazon+=1
        elif movie['streaming'] == "netflix":
            cuenta_netflix+=1
        elif movie['streaming'] == "hulu":
            cuenta_hulu+=1
        elif movie['streaming'] == "disney":
            cuenta_disney+=1
        
        genders = movie["listed_in"].split(",")
        for genero in genders:
            if not genero in dic_generos:
                dic_generos[genero] = 1
            elif genero in dic_generos:
                dic_generos[genero]+=1
        

    cantidad_plataforma=cuenta_netflix,cuenta_amazon,cuenta_hulu,cuenta_disney
    cantidad_type=cuenta_movie,cuenta_show

    end_time = getTime()
    delta_time = deltaTime(start, end_time)
    contentByDirector = moviesByDirector,cantidad_type, cantidad_plataforma, dic_generos, delta_time
    return contentByDirector

# Obtener peliculas en un periodo de tiempo
def getMoviesByPeriodo(movies, year1, year2):

    start = getTime()
    moviesByPeriodo = lt.newList()
    for i in range(lt.size(movies)):
        movie = lt.getElement(movies, i)
        if movie['type'] == 'Movie':
            if int(year1) <= int(movie['release_year']) <= int(year2):
                lt.addLast(moviesByPeriodo, movie)

    movies_sort = ms.sort(movies, cmpMoviesByReleaseYear)
    end_time = getTime()
    delta_time = deltaTime(start, end_time)
    return movies_sort, delta_time

# Determina los generos en un top
def top_generos(movies, top):
    start = getTime()
    movies_sort = ms.sort(movies, cmpMoviesByReleaseYear)
    dic_generos={}
    for i in range(lt.size(movies_sort)):
        movie = lt.getElement(movies_sort, i)
        genders = movie["listed_in"].split(",")
        for genero in genders:
            if not genero in dic_generos:
                dic_generos[genero] = 1
            elif genero in dic_generos:
                dic_generos[genero] += 1

    dic_generos = dict(sorted(dic_generos.items(), key=lambda item: item[1], reverse=True))
    top_generos = {}
    for i in range(top):
        top_generos[list(dic_generos.keys())[i]] = list(dic_generos.values())[i]

    cont_t = {}
    cont_p = {}
    for i in range(lt.size(movies_sort)):
        movie = lt.getElement(movies_sort, i)


        for genero in top_generos:
            if genero in movie['listed_in']:
                if not genero in cont_t:
                    cont_t[genero] = {'Movies': 0, 'TvShows': 0}
                    if movie['type'] == "Movie":
                        cont_t[genero]['Movies'] += 1
                    elif movie['type'] == "TV Show":
                        cont_t[genero]['TvShows'] += 1
                else:
                    if movie['type'] == "Movie":
                        cont_t[genero]['Movies'] += 1
                    elif movie['type'] == "TV Show":
                        cont_t[genero]['TvShows'] += 1
                if not genero in cont_p:
                    cont_p[genero] = {'amazon':0, 'netflix':0, 'hulu':0, 'disney':0}
                    if movie['streaming'] == "amazon":
                        cont_p[genero]['amazon'] += 1
                    elif movie['streaming'] == "netflix":
                        cont_p[genero]['netflix'] += 1
                    elif movie['streaming'] == "hulu":
                        cont_p[genero]['hulu'] += 1
                    elif movie['streaming'] == "disney":
                        cont_p[genero]['disney'] += 1
                else:
                    if movie['streaming'] == "amazon":
                        cont_p[genero]['amazon'] += 1
                    elif movie['streaming'] == "netflix":
                        cont_p[genero]['netflix'] += 1
                    elif movie['streaming'] == "hulu":
                        cont_p[genero]['hulu'] += 1
                    elif movie['streaming'] == "disney":
                        cont_p[genero]['disney'] += 1

    
    top_plat = {}
    top_tip = {}
    for i in range(top):
        top_tip[list(cont_t.keys())[i]] = list(cont_t.values())[i]
        top_plat[list(cont_p.keys())[i]] = list(cont_p.values())[i]
    end_time = getTime()
    delta_time = deltaTime(start, end_time)
    return top_generos, top_plat, top_tip, delta_time

def amaSize(catalog):
    return lt.size(catalog['amazon'])

def netSize(catalog):
    return lt.size(catalog['netflix'])

def hulSize(catalog):
    return lt.size(catalog['hulu'])

def disSize(catalog):
    return lt.size(catalog['disney'])

def movSize(catalog):
    return lt.size(catalog['titles'])

# Comparar elementos

def cmpMoviesByReleaseYear(movie1, movie2):
    if (int(movie1['release_year']) < int(movie2['release_year'])):
        return True
    elif (int (movie1['release_year']) == int (movie2['release_year'])):
        if (movie1['title'] < movie2['title']):
            return True
        elif (movie1['title'] == movie2['title']):
            if (movie1['duration'] < movie2['duration']):
                return True
            return False
    return False

#Funcion para pasar de texto a fecha


def mesANumero(fecha):
    m = {
        'January': 1,
        'Februari': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'Novermber': 11,
        'December': 12
        }

    fecha = fecha.replace(",", " ")
    fecha = fecha.split(" ")

    dia =  fecha[1]
    mes =  fecha[0]
    mes = m[mes]
    anio = fecha[2]

    if dia < '10':
        dia = int(dia[1])


    return (int(anio), mes, dia)

# Tiempo Muestras

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed



