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
 """

import config as cf
import model
import csv

csv.field_size_limit(2147483647)



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control



# Funciones para la carga de datos

#esta consiste en cargar un
# archivo de cada uno de los servicios de streaming
def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']

    titles, authors = loadAmazon(catalog)
    maman = loadDisneyplus(catalog)
    dewd = loadHulu(catalog)
    bruh = loadNetflix(catalog)
    
    sorttitles(catalog)
    return titles, maman, dewd, bruh


def loadAmazon(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    """
    Carga el listado de todas las  peliculas y programas disponibles en la 
    plataforma respectiva.  Por cada titulo hay detalles como: reparto(cast),
    directores(director), clasificaciones(rating), y anio de lanzamiento(release_year).
    """
    amazonfile = cf.data_dir + '/Streaming/amazon_prime_titles-utf8-small.csv'
    input_file = csv.DictReader(open(amazonfile, encoding='utf-8'))
    for title in input_file:
        model.addTitle(catalog, title)
    return model.titleSize(catalog)


def loadDisneyplus(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'Data/Streaming/.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        model.addTag(catalog, tag)
    return model.tagSize(catalog)


def loadHulu(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    titletagsfile = cf.data_dir + 'Data/title_tags-small.csv'
    input_file = csv.DictReader(open(titletagsfile, encoding='utf-8'))
    for titletag in input_file:
        model.addtitleTag(catalog, titletag)
    return model.titleTagSize(catalog)

def loadNetflix(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    titletagsfile = cf.data_dir + 'Data/title_tags-small.csv'
    input_file = csv.DictReader(open(titletagsfile, encoding='utf-8'))
    for titletag in input_file:
        model.addtitleTag(catalog, titletag)
    return model.titleTagSize(catalog)



# Funciones de ordenamiento
def sorttitles(catalog):
    """
    Ordena los libros por average_rating
    """
    model.sortTitles(catalog)

# Funciones de consulta sobre el catálogo
def gettitlesByAuthor(control, authorname):
    """
    Retrona los libros de un autor
    """
    author = model.gettitlesByAuthor(control['model'], authorname)
    return author


def getBesttitles(control, number):
    """
    Retorna los mejores libros
    """
    besttitles = model.getBesttitles(control['model'], number)
    return besttitles


def counttitlesByTag(control, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.counttitlesByTag(control['model'], tag)
