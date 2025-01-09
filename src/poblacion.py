import csv
from collections import namedtuple
from matplotlib import pyplot as plt



Poblacion = namedtuple("Poblacion", "pais, abreviatura, año, censo")

def leer_archivo(ruta):
    poblacion = []
    with open(ruta, encoding= "utf-8") as f:
        lector = csv.reader(f)
        for pais, abreviatura, año, censo in lector:
            pais = str(pais)
            abreviatura = str(abreviatura).upper() #no se olvide poner los () que si no ☠️
            año = int(año)
            censo = int(censo)
            poblacion.append(Poblacion(pais, abreviatura, año, censo))
    return poblacion
    



datos = leer_archivo("data\population.csv") #esto me ayuda a meter los datos en cualquier funcion al llamarla

def paises_unicos(lista):
    paises = set()
    for datos in lista:
        paises.add(datos.pais)
    return sorted(paises)

#paises = paises_unicos(datos) #TEST😵‍💫
#print(paises)



def filtra_por_pais(lista, nombre_o_codigo):
    datos_pais = []
    for pais in lista:
        if (nombre_o_codigo == pais.pais) or (nombre_o_codigo == pais.abreviatura):
            datos_pais.append((pais.año, pais.censo)) # no es necesario el uso del zip, únicamente lo pones entre paréntesis y separados por coma
    return datos_pais

#print(f"Los datos de 'ESP' son: {filtra_por_pais(datos, "ESP")}") #TEST😵‍💫




def filtra_por_paises_y_anyo(poblaciones, anyo, paises): # cambié el nombre de lista a poblaciones
    res = []
    for pais in poblaciones:
        if (pais.pais in paises) and (pais.año == anyo):
            res.append((pais.pais, pais.censo))
    return res

#print(f"Los datos son: \n {filtra_por_paises_y_anyo(datos, 2000, ["Caribbean small states", "Spain"])}") #TEST😵‍💫



def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años = []
    lista_habitantes = []
    for pais in poblaciones:
        if (nombre_o_codigo == pais.pais) or (nombre_o_codigo == pais.abreviatura):
            lista_años.append(pais.año)
            lista_habitantes.append(pais.censo)

    if lista_años and lista_habitantes:
        plt.title(f"Evolución de la población de {nombre_o_codigo}")
        plt.plot(lista_años, lista_habitantes)
        plt.xlabel('Año')
        plt.ylabel('Número de Habitantes')
        plt.grid(True)
        plt.show()


#muestra_evolucion_poblacion(datos, "ESP") #TEST😵‍💫


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_paises = [] #para hacer graficas tenemos que crear listas de los datos que queremos mostrar en la gráfica
    lista_habitantes = []

    for pais in poblaciones:
        if (pais.pais in paises) and (pais.año == anyo):
            lista_paises.append(pais.pais)
            lista_habitantes.append(pais.censo)

    if lista_habitantes and lista_paises:
        lista_paises.sort() # lo ordenamos
        plt.title(f"Población de los países en {anyo}")
        plt.bar(lista_paises, lista_habitantes)
        plt.xlabel('Países')
        plt.ylabel('Número de Habitantes')
        plt.xticks(rotation=45, ha='right')  # pijada💵💱🤑
        plt.show()

muestra_comparativa_paises_anyo(datos, 2000, ["Spain", "France"]) #TEST😵‍💫