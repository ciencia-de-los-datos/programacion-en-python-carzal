"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#importar librerias

def load_data(name_file):
    with open(name_file, "r") as file:
        data = file.readlines()

    data = [line.replace("\n", "") for line in data]
    data = [line.split("\t") for line in data]
    return data

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    data = load_data("data.csv")

    val = 0
    for line in data:
        val += int(line[1])
    val
    return val

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registros = sorted(list(Counter([x[0] for x in datos]).items()))

    return registros

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    # letras = [l[0] for l in datos]
    # numeros = [n[1] for n in datos]
    # zipped = sorted(zip(letras,numeros))
    list(zipped)
    lista = []
    for clave, grupo in itertools.groupby(zipped,lambda x:x[0]):
        z = 0
        for cont in grupo:
            z += int(cont[1])
        pareja = (clave,z)
        lista.append(pareja)

    return lista


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    fechas = [f[2].split("-") for f in datos]
    meses = sorted(list(Counter([x[1] for x in fechas]).items()))
    return meses

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    list(zipped)
    lista2 = []
    for clave, grupo in itertools.groupby(zipped,lambda x:x[0]):
        listanums = []
        for cont in grupo:
            listanums.append(int(cont[1]))
        trio = (clave,max(listanums),min(listanums))
        lista2.append(trio)

    return lista2

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    temp = [l[4].split(",") for l in datos]
    temp
    dic =[]
    for i in temp:
        listunitaria = i
        for j in listunitaria:
            x = ()
            x = tuple(j.split(":"))
            dic.append(x)
    dic = sorted(dic)

    lista3 = []
    for clave, grupo in itertools.groupby(dic,lambda x:x[0]):
        listanums = []
        for cont in grupo:
            listanums.append(int(cont[1]))
        trio = (clave,min(listanums),max(listanums))
        lista3.append(trio)
    return lista3                                                                                                                                             

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    zipped = zip(numeros,letras)
    zipped = list(zipped)
    zipped.sort(key = lambda x:x[0])
    lista4 = []
    for clave, grupo in itertools.groupby(zipped,lambda x:x[0]):
        listaletras = []
        for cont in grupo:
            listaletras.append((cont[1]))
            union = (int(clave),listaletras)
        lista4.append(union)
    return lista4

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    zipped = sorted(zip(numeros,letras))
    zipped = list(zipped)
    lista5 =[]
    for clave, grupo in itertools.groupby(zipped,lambda x:x[0]):
        listaletras = []
        for cont in grupo:
            listaletras.append((cont[1]))
            sinrep = sorted(set(listaletras))
        union = (int(clave),list(sinrep))
        lista5.append(union)
    return lista5

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    temp = [l[4].split(",") for l in datos]
    temp
    dic =[]
    for i in temp:
        listunitaria = i
        for j in listunitaria:
            x = ()
            x = tuple(j.split(":"))
            dic.append(x)
    dic = sorted(dic)
    registros2 = dict(sorted(list(Counter([x[0] for x in dic]).items())))
    return registros2

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    col4 = [len(l[3].split(",")) for l in datos]
    col5 = [len(l[4].split(",")) for l in datos]
    resultado = list(zip(letras,col4,col5))
    return resultado

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """

    col4 = [l[3].split(",") for l in datos]
    zipped = list(zip(col4,numeros))
    dic =[]
    temporal = []
    for j in zipped:
        temporal = j[0]
        for i in temporal:
            x = list(zip(i,j[1]))
            dic.append(x)
    #dic = sorted(dic)
    
    dicconv = []
    for k in dic: 
        for par in k:
            b = par
            dicconv.append(b)
    dicconv = sorted(dicconv)

    lista6 = []
    for clave, grupo in itertools.groupby(sorted(dicconv),lambda x:x[0]):
        z = 0
        for cont in grupo:
            z += int(cont[1])
        pareja = (clave,z)
        lista6.append(pareja)
    dic6 = dict(lista6)
    return dic6

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    col4 = [itemgetter(4)(l) for l in datos]
    pareja = list(zip(letras,col4))
    patron = re.compile(r"\d+")
    dic = []
    for i in pareja:
        temporal = patron.findall(i[1])
        dic.append(temporal)

    dic2 = []
    for j in dic:
        suma = 0
        for k in j:
            suma += int(k)
        dic2.append(suma)
    
    newpareja = list(zip(letras,dic2))

    lista7 = []
    for clave, grupo in itertools.groupby(sorted(newpareja),lambda x:x[0]):
        z = 0
        for cont in grupo:
            z += int(cont[1])
        pareja = (clave,z)
        lista7.append(pareja)
        dic7 = dict(lista7)

    return dic7
pregunta_12()


