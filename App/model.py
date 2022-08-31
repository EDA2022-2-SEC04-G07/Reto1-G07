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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'titles': None,
               'authors': None,
               'tags': None,
               'title_tags': None}

    catalog['titles'] = lt.newList('SINGLE_LINKED')
    catalog['authors'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareauthors)
    catalog['tags'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparetagnames)
    catalog['title_tags'] = lt.newList('SINGLE_LINKED')

    return catalog

# Funciones para agregar informacion al catalogo

def addTitle(catalog, title):
    # Se adiciona la pelicula a la lista.
    lt.addLast(catalog['model'], title)
    # Se obtienen las entradas de las peliculas.
    # aqui se adicionaria, al igual que los autores en los libros,
    # las columnas de los datos de las peliculas.
    authors = title['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addTitleAuthor(catalog, author.strip(), title)
    return catalog


def addTitleAuthor(catalog, authorname, title):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['titles'], title)
    return catalog


def addTag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)
    return catalog


def addTitleTag(catalog, titletag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTitleTag(titletag['tag_id'], titletag['goodreads_title_id'])
    lt.addLast(catalog['title_tags'], t)
    return catalog

# Funciones para creacion de datos

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "titles": None,  "average_rating": 0}
    author['name'] = name
    author['titles'] = lt.newList('ARRAY_LIST')
    return author


def newTag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newTitleTag(tag_id, title_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    titleTag = {'tag_id': tag_id, 'title_id': title_id}
    return titleTag

# Funciones de consulta

def getTitlesByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posauthor = lt.isPresent(catalog['authors'], authorname)
    if posauthor > 0:
        author = lt.getElement(catalog['authors'], posauthor)
        return author
    return None


def getBestTitles(catalog, number):
    """
    Retorna los mejores libros
    """
    titles = catalog['titles']
    bestTitles = lt.newList()
    for cont in range(1, number+1):
        title = lt.getElement(titles, cont)
        lt.addLast(bestTitles, title)
    return bestTitles


def countTitlesByTag(catalog, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    tags = catalog['tags']
    titlecount = 0
    pos = lt.isPresent(tags, tag)
    if pos > 0:
        tag_element = lt.getElement(tags, pos)
        if tag_element is not None:
            for title_tag in lt.iterator(catalog['title_tags']):
                if tag_element['tag_id'] == title_tag['tag_id']:
                    titlecount += 1
    return titlecount


def titleSize(catalog):
    return lt.size(catalog['titles'])


def authorSize(catalog):
    return lt.size(catalog['authors'])


def tagSize(catalog):
    return lt.size(catalog['tags'])


def titleTagSize(catalog):
    return lt.size(catalog['title_tags'])


# Funciones utilizadas para comparar elementos dentro de una lista
def compareauthors(authorname1, author):
    if authorname1.lower() == author['name'].lower():
        return 0
    elif authorname1.lower() > author['name'].lower():
        return 1
    return -1


def comparetagnames(name, tag):
    if (name == tag['name']):
        return 0
    elif (name > tag['name']):
        return 1
    return -1
# Funciones de ordenamiento
def sorttitles(catalog):
    sa.sort(catalog['titles'], comparetagnames)