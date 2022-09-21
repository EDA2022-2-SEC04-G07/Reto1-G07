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
from gettext import Catalog

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

# Carga de Datos
 
def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    
    amazon = load_amazon(catalog)
    disney = load_disney(catalog)
    netflix = load_netflix(catalog)
    hulu = load_hulu(catalog)
    titles = getAllTit(control)
    
    
    return amazon,disney, netflix, hulu, titles

# Carga individual por plataforma

def load_netflix(catalog, ):
    """
    Carga los archivos. Tomando sus direcciones y por cada uno, se crea en la lista de direcciones,
    al director y una referencia a la pelicula o serie. (Archivo Netflix)
    """
    dats = cf.data_dir + 'Streaming/netflix_titles-utf8-small.csv'
    inpfil = csv.DictReader(open(dats, encoding='utf-8'))
    for inf in inpfil:
        model.addinfo_netflix(catalog, inf)
        model.addMediaTitles(catalog, inf, 'netflix')
        
    return model.netSize(catalog)

def load_amazon(catalog):
    """
    Carga los archivos. Tomando sus direcciones y por cada uno, se crea en la lista de direcciones,
    al director y una referencia a la pelicula o serie. (Archivo Amazon)
    """
    dats= cf.data_dir + 'Streaming/amazon_prime_titles-utf8-small.csv'
    inpfil = csv.DictReader(open(dats, encoding='utf-8'))
    for inf in inpfil:
       model.addinfo_amazon(catalog, inf)
       model.addMediaTitles(catalog, inf, 'amazon')
       
    return model.amaSize(catalog)

def load_disney(catalog):
    """
    Carga los archivos. Tomando sus direcciones y por cada uno, se crea en la lista de direcciones,
    al director y una referencia a la pelicula o serie. (Archivo Disney)
    """
    dats = cf.data_dir + 'Streaming/disney_plus_titles-utf8-small.csv'
    inpfil = csv.DictReader(open(dats, encoding='utf-8'))
    for inf in inpfil:
        model.addinfo_disney(catalog, inf)
        model.addMediaTitles(catalog, inf, 'disney')
        
    return model.disSize(catalog)

def load_hulu(catalog):
    """
    Carga los archivos. Tomando sus direcciones y por cada uno, se crea en la lista de direcciones,
    al director y una referencia a la pelicula o serie. (Archivo Hulu)
    """

    dats = cf.data_dir + 'Streaming/hulu_titles-utf8-small.csv'
    inpfil = csv.DictReader(open(dats, encoding='utf-8'))
    for inf in inpfil:
        model.addinfo_hulu(catalog, inf)
        model.addMediaTitles(catalog, inf, 'hulu')
    
    return model.hulSize(catalog)

# Requerimientos

def movSize(catalog):
    return model.movSize(catalog)

def changeListType(catalog, type):
    model.changeListType(catalog, type)

def getMoviesByActor(movies, actor):
    return model.getMoviesByActor(movies, actor)

def getMoviesByDirector(movies, director):
    return model.getContentByDirector(movies, director)
    
def getMoviesByPeriodo(movies, year1, year2):
    return model.getMoviesByPeriodo(movies, year1, year2)

def getMoviesByCountry(movies, country):
    return model.getMoviesbyCountry(movies, country)

def top_generos(movies,top):
    return model.top_generos(movies,top)

# Funciones de ordenamiento

def getSomeTitles(control):
    movies = model.getTitulos(control['model'])
    return movies

def getAllTit(control):
    allTitles = model.getAllTit(control['model'])
    return allTitles
