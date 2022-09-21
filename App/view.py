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
    print("1- Elegir el tipo de lista:'1' Array, '2' Linked")
    print("2- Cargar la informacion de las plataformas")
    print("3- Peliculas en un periodo de tiempo")
    print("4- Contenido donde este un autor")
    print("5- Contenido realizado en un pais")
    print("6- Contenido con un director especifico")
    print("7- Top x de los generos con mas contenido")
    print("0- Finalizar programa")

catalog = None

def printPlatformCount(amazon, disney, netflix, hulu):
    plataformas = [['Amazon',str(amazon)], ['Netflix',str(netflix)], ['Hulu',str(hulu)], ['Disney',str(disney)]]
    print(tabulate((plataformas), headers=[
          'Service_name', 'count'], tablefmt='fancy_grid'))
    print("\n")

def printSomeTitles(titles):
    
    
    if lt.size(titles) > 0:

        table = []
        def crear_lista(lista):
            list = []
            for movie in lt.iterator(lista):
                description = movie['description']
                nueva_descripcion = ''
                if len(description) > 50:
                    nueva_descripcion = description[:50] + '...'
                description = nueva_descripcion
                id = str(movie['show_id'])
                id = id.replace('s', '')


                list.append([id, movie['streaming'] , movie['type'] , movie['release_year'],
                movie['title'] , movie['director'] , movie['cast'] ,
                movie['country'] , movie['date_added'], movie['rating'],
                    movie['duration'],  movie['listed_in'], description])
            return list


        table.append(crear_lista(titles))
        columna = []
        for i in range(len(table)):
            for k in range(len(table[i])):
                columna.append(table[i][k])
        return columna

    else:
        print("No se encontraron peliculas")

def printSortResults(sort_list, delta_time):
    delta_time = float(delta_time)
    
    print(f'El tiempo que tarda en ordenar los datos de las 4 plataformas es: {delta_time} ms')
    print('\n')

def printTitlesByAutor(moviesByAutor, cont_movies, cont_tvshows):
    table = []
    if cont_movies > 1 or cont_tvshows > 1:
        lista = []
        for i in range(1,3):
            movie = lt.getElement(moviesByAutor, i)
            
            cast = movie['cast']
            description = movie['description']
            nueva_descripcion = ''
            if len(description) > 50:
                nueva_descripcion = description[:50] + '...'
                description = nueva_descripcion
            if len(cast) > 80:
                cast = cast[:80] + '...'
            lista.append([movie['type'], movie['title'], movie['release_year'], movie['director'],
                         movie['streaming'], movie['duration'],cast, movie['country'], movie['listed_in'], description])
        
        for k in range(lt.size(moviesByAutor), lt.size(moviesByAutor) - 3, -1):
            movie = lt.getElement(moviesByAutor, k)
            
            description = movie['description']
            nueva_descripcion = ''
            if len(description) > 50:
                nueva_descripcion = description[:50] + '...'
                description = nueva_descripcion
            if len(cast) > 80:
                cast = cast[:80] + '...'
            lista.append([movie['type'], movie['title'], movie['release_year'], movie['director'],
                         movie['streaming'], movie['duration'], cast, movie['country'], movie['listed_in'], description])

        table.append(lista)
        tipos = [['Movies',str(cont_movies)], ['Series',str(cont_tvshows)]]
        print(tabulate(tipos, headers=['type', 'count'], tablefmt='grid', stralign='left'))
        columna = []
        for i in range(len(table)):
            for k in range(len(table[i])):
                columna.append(table[i][k])
        print(tabulate(columna, headers=['type ','title','release_year','director','stream_service', 'duration', 'cast', 'country','listed_in', 'description'],
        tablefmt="grid", stralign='left', maxcolwidths=18, ))
        print("\n")
    else:
        print("El actor no se encuentra en ningun contenido")


def printTitlesByCountry(moviesByCountry, cont_movies, cont_tvshows):
    table=[]
    if lt.size(moviesByCountry) > 2:
        lista = []
        for i in range(1,4):
            movie = lt.getElement(moviesByCountry, i)
            
            cast = movie['cast']
            description = movie['description']
            nueva_descripcion = ''
            if len(description) > 50:
                nueva_descripcion = description[:50] + '...'
                description = nueva_descripcion
            if len(cast) > 80:
                cast = cast[:80] + '...'
            lista.append([movie['release_year'],movie['title'], movie['director'],
                         movie['streaming'], movie['duration'],movie["type"],cast, movie['country'], movie['listed_in'], description])
        
        for k in range(lt.size(moviesByCountry), lt.size(moviesByCountry) - 3, -1):
            movie = lt.getElement(moviesByCountry, k)
            
            description = movie['description']
            nueva_descripcion = ''
            if len(description) > 50:
                nueva_descripcion = description[:50] + '...'
                description = nueva_descripcion
            if len(cast) > 80:
                cast = cast[:80] + '...'
            lista.append([movie['release_year'],movie['title'], movie['director'],
                         movie['streaming'], movie['duration'],movie["type"],cast, movie['country'], movie['listed_in'], description])

        table.append(lista)
        tipos = [['Movies',str(cont_movies)], ['Series',str(cont_tvshows)]]
        print(tabulate(tipos, headers=['type', 'count'], tablefmt='grid', stralign='left'))
        columna = []
        for i in range(len(table)):
            for k in range(len(table[i])):
                columna.append(table[i][k])
        print(tabulate(columna, headers=['release_year ','title','director','stream_service', 'duration','type', 'cast', 'country','listed_in', 'description'],
        tablefmt="grid", stralign='left', maxcolwidths=18, ))
        print("\n")
    else:
        print("No se encontró contenido producido en este pais.")


def printMoviesByPeriodo(moviesByPeriodo, periodo):
    if lt.size(moviesByPeriodo) > 0:

        inicio, fin = periodo
        tabla=[]
        print('Las primeras y ultimas 3 peliculas ordenadas de la lista son: ')
        for i in range(1, 4):
            movie = lt.getElement(moviesByPeriodo, i)
            cast = movie['cast']
            if len(cast) > 80:
                cast = cast[:80] + '...'
            movies=[ str(movie['type']) ,  str(movie["release_year"]),str(movie["title"]) ,
                str(movie['duration']) , str(movie['streaming']) , str(movie["director"]) ,  cast]
            tabla.append(movies)


        for i in range(lt.size(moviesByPeriodo) , lt.size(moviesByPeriodo) - 3, -1):
            movie = lt.getElement(moviesByPeriodo, i)
            cast = movie['cast']
            if len(cast) > 80:
                cast = cast[:80] + '...'
            movies=[ str(movie['type']) ,  str(movie["release_year"]),str(movie["title"]) ,
                str(movie['duration']) , str(movie['streaming']) , str(movie["director"]) ,  cast]
            tabla.append(movies)
        print(tabulate((tabla),headers=['type','Release year','Title','Duration','Stream Service','Director','Cast'],tablefmt="grid", stralign='left',maxcolwidths=18,))
            
        
        print("Hay " + str(lt.size(moviesByPeriodo)) +
            " peliculas en este periodo de tiempo " + str(inicio) + " - " + str(fin))
    else:
        print("No se encontraron peliculas en ese periodo de tiempo")

def printMoviesByDirector(contentByDirector, director):
    moviesByDirector, cantidad_type, cantidad_plataforma, dic_generos, delta_time = contentByDirector
    if lt.size(moviesByDirector) > 0:
        cuenta_movie,cuenta_show = cantidad_type
        cuenta_netflix,cuenta_amazon,cuenta_hulu,cuenta_disney = cantidad_plataforma
        print('=========== Respuesta requerimiento 6 ===========')
        print(f'------------ {director} Tipo de contenido ------------')
        tipos = [['Movies',str(cuenta_movie)], ['Series',str(cuenta_show)]]
        print(tabulate(tipos, headers=['type', 'count'], tablefmt='grid', stralign='left'))
        print('\n')
        print(f'------------ {director} Contador Plataformas ------------')
        plataformas = [['Netflix',str(cuenta_netflix)], ['Amazon',str(cuenta_amazon)], ['Hulu',str(cuenta_hulu)], ['Disney',str(cuenta_disney)]]
        print(tabulate(plataformas, headers=['service_name', 'count'], tablefmt='grid', stralign='left'))
        print('\n')

        print(f'------------ {director} Contador de Listed in ------------')
        print(f'Hay solo {len(dic_generos)} generos diferentes')
        print('Los 3 primeros y 3 ultimos son: ')
        columna =[]
        if len(dic_generos) > 6:
            for i in range(1,3):
                columna.append([list(dic_generos.keys())[i], list(dic_generos.values())[i]])
            for i in range(len(dic_generos) - 3, len(dic_generos)):
                columna.append([list(dic_generos.keys())[i], list(dic_generos.values())[i]])
        else:
            for i in range(len(dic_generos)):
                columna.append([list(dic_generos.keys())[i], list(dic_generos.values())[i]])
            print(tabulate(columna, headers=['listed_in', 'count'], tablefmt='grid', stralign='left'))

        print('\n')

        print(f'------------ {director} Detalles de contenido ------------')
        print('Las primeras y ultimas 3 peliculas ordenadas de la lista son: ')
        tabla=[]
        if lt.size(moviesByDirector) > 6:
            lista = []
            for i in range(1, 4):
                movie = lt.getElement(moviesByDirector, i)
                description = movie['description']
                nueva_descripcion = ''
                if len(description) > 50:
                    nueva_descripcion = description[:50] + '...'
                    description = nueva_descripcion

                cast = movie['cast']
                if len(cast) > 80:
                    cast = cast[:80] + '...'
                lista.append([movie['title'], movie['release_year'], movie['director'],
                            movie['streaming'], movie['duration'], cast, movie['country'], movie['rating'],movie['listed_in'], description])
                lista.append(movies)

            for i in range(lt.size(moviesByDirector) , lt.size(moviesByDirector) - 3, -1):
                movie = lt.getElement(moviesByDirector, i)
                description = movie['description']
                nueva_descripcion = ''
                if len(description) > 50:
                    nueva_descripcion = description[:50] + '...'
                    description = nueva_descripcion

                cast = movie['cast']
                if len(cast) > 80:
                    cast = cast[:80] + '...'
                lista.append([movie['title'], movie['release_year'], movie['director'],
                              movie['streaming'], movie['duration'], cast, movie['country'], movie['rating'], movie['listed_in'], description])
                lista.append(movies)
            tabla.append(lista)
            columna = []
            for i in range(len(tabla)):
                for k in range(len(tabla[i])):
                    columna.append(tabla[i][k])
            print(tabulate(columna, headers=['title', 'release_year', 'director ', 'stream service',
                                           'duration', 'cast', 'country', 'rating', 'listed_in', 'description'], tablefmt="grid", stralign='left', maxcolwidths=18, ))

        else:
            lista = []
            
            movie = lt.getElement(moviesByDirector, 1)
            description = movie['description']
            nueva_descripcion = ''
            if len(description) > 50:
                nueva_descripcion = description[:50] + '...'
                description = nueva_descripcion
            cast = movie['cast']
            if len(cast) > 80:
                cast = cast[:80] + '...'
            lista.append([movie['title'], movie['release_year'], movie['director'],
                            movie['streaming'], movie['duration'], cast, movie['country'], movie['rating'], movie['listed_in'], description])
            lista.append(movies)
            tabla.append(lista)
            
            columna = []
            for i in range(len(tabla)):
                for k in range(len(tabla[i])):
                    columna.append(tabla[i][k])
            print(tabulate(columna, headers=['title', 'release_year', 'director ', 'stream service',
                                           'duration', 'cast', 'country', 'rating', 'listed_in','description'], tablefmt="grid", stralign='left', maxcolwidths=18, ))
        

    else:
        print("No se encontraron peliculas de ese director")

def printContentGenders(content, top):
    top_generos, top_platfomrs_por_gen, top_tipos_por_gen, delta_time = content

    print('=========== Respuesta requerimiento 7 ===========')
    print(f'------------ Top {top} generos ------------')
    columnas = []
    for k in top_generos:
        columnas.append([k, top_generos[k]])
    print(tabulate(columnas, headers=['Listed in', 'count'], tablefmt='grid', stralign='left'))

    tabla_2 = {}
    columna = []
    columna_1 = []
    columna_2 = []
    columna_3 = []
    columna_4 = []
    rank = 0
    for k in top_generos:
        rank += 1
        columna.append(rank)
        columna_1.append(k)
        columna_2.append(top_generos[k])

    for genero in top_tipos_por_gen:
        text = 'count' + '\n' + 'type' + '\n'
        for type in top_tipos_por_gen[genero]:
            text += type + ' '*4 + str(top_tipos_por_gen[genero][type]) + '\n'
        columna_3.append(text)
    
    for genero in top_platfomrs_por_gen:
        text = 'count' + '\n' + 'stream_service' + '\n'
        for platform in top_platfomrs_por_gen[genero]:
            text += platform + ' '*10 + str(top_platfomrs_por_gen[genero][platform]) + '\n'
        columna_4.append(text)


    tabla_2['rank'] = columna
    tabla_2['Listed in'] = columna_1
    tabla_2['count'] = columna_2
    tabla_2['type'] = columna_3
    tabla_2['stream_service'] = columna_4
    print(f'------------ Top {top} generos con sus tipos y plataformas ------------')
    print(tabulate(tabla_2, headers=['Rank','Listed in', 'count', 'type',
          'stream_service'], tablefmt='grid', stralign='left'))


def printShowsByPeriod(shows, periodo, contador):
    if lt.size(shows) > 0:

        print('=========== Respuesta requerimiento 8 ===========')
        print(f'------------ Shows por periodo ------------')
        shows_primeros = lt.subList(shows, 1, 3)
        shows_ultimos = lt.subList(shows, lt.size(shows) - 2, 3)
        inicio, fin = periodo
        tabla = []
        print('Las primeras y ultimas 3 peliculas ordenadas de la lista son: ')
        for show in lt.iterator(shows_primeros):
            cast = show['cast']
            if len(cast) > 80:
                cast = cast[:80] + '...'
            shows = [show['type'], show['date_added'], show['title'], show['duration'],show['release_year'],show['streaming'], show['director'], cast]
            tabla.append(shows)
        
        for show in lt.iterator(shows_ultimos):
            cast = show['cast']
            if len(cast) > 80:
                cast = cast[:80] + '...'
            shows = [show['type'], show['date_added'], show['title'], show['duration'],
                     show['release_year'], show['streaming'], show['director'], cast]
            tabla.append(shows)
        
        print(tabulate((tabla), headers=['type', 'date_added', 'Title', 'Duration',
              'Release_year', 'streaming', 'director', 'cast'], tablefmt="grid", stralign='left', maxcolwidths=18,))

        print("Hay " + str(contador) +" shows en este periodo de tiempo " + str(inicio) + " - " + str(fin))
    else:
        print("No se encontraron shows en ese periodo de tiempo")


control = newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs) == 1:
        opc = int(input('Ingrese el numero de la lista que desea usar: '))
        if opc== 1:
            print('Se cambio el tipo de lista a ARRAY_LIST')
            controller.changeListType(control, 'ARRAY_LIST')
        elif opc == 2:
            print('Se cambio el tipo de lista a LINKED_LIST')
            controller.changeListType(control, 'SINGLE_LINKED')
        else:
            print('Eleccion no disponible')

    elif int(inputs) == 2:
        print("Se estan cargando los archivos... Espere por favor...")
        amazon, disney, netflix, hulu, titles = controller.loadData(control)
        print('El total de titulos son: ' +  str(lt.size(titles)))
        printPlatformCount(amazon, disney, netflix, hulu)
        movies = controller.getSomeTitles(control)
        tabla = printSomeTitles(movies)
        print(tabulate(tabla, headers=['show_id', 'stream_service', 'type ', 'release_year',
                'title', 'director', 'cast', 'country', 'date_added', 'rating', 'duration', 'listed_in', 'description'], tablefmt="grid", stralign='left',maxcolwidths=18, ))
        print("\n")
    
    elif int(inputs) == 3:
        fecha_i = int(input("Ingrese el año de inicio de la busqueda: "))
        fecha_f = int(input("Ingrese el año de fin de la busqueda: "))
        movies_periodo, deltatime = controller.getMoviesByPeriodo(titles, fecha_i, fecha_f)
        periodo = fecha_i, fecha_f
        print("El tiempo en ms es: ", deltatime)
        printMoviesByPeriodo(movies_periodo, periodo)

    elif int(inputs) == 4:
        actor = input("Ingrese el autor: ")
        movies, tiempo, cont_movies , cont_tvshows = controller.getMoviesByActor(titles, actor)
        print('El tiempo en ms es: ', f"{tiempo:0.3f}")
        print('Movies del autor: '+actor)
        printTitlesByAutor(movies, cont_movies, cont_tvshows)
        print('\n')

    elif int(inputs) == 5:
        pais = input("Ingrese el pais: ")
        movies, tiempo, cont_movies, cont_tvshows = controller.getMoviesByCountry(titles,pais)
        print('TEL tiempo en ms es: ', f"{tiempo:0.3f}")
        print('Movies por pais: '+pais)
        printTitlesByCountry(movies, cont_movies,cont_tvshows)
        print('\n')

    elif int(inputs) == 6:
        director = input("Ingrese el nombre del director: ")
        contentByDirector = controller.getMoviesByDirector(titles, director)
        
        print('El tiempo en ms es: ', f"{contentByDirector[4]:0.3f}")
        print('Movies por director: '+director)
        printMoviesByDirector(contentByDirector, director)
        print('\n')

    elif int(inputs) == 7:
        top = int(input("Ingrese el Top que quiere identificar: "))
        while top <= 0 and 'quick' <=0:
            top = int(input("Ingrese un numero mayor a 0: "))
            
        contenido_por_generos = controller.top_generos(titles, top)
        print('El tiempo en ms es : ', f"{contenido_por_generos[3]:0.3f}")
        printContentGenders(contenido_por_generos, top)

    elif int(inputs[0]) == 0:
        print("Hasta la proxima... Bay.")
        sys.exit(0)

    else:
        continue
sys.exit(0)
sys.exit(0)
