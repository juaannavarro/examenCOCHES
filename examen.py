import re
import numpy as np
import pandas as pd
from numpy import shares_memory
from numpy.lib.function_base import append
from pandas import tseries


conversiones = pd.read_csv("conversiones.csv", sep = ";")
navegacion = pd.read_csv("navegacion.csv", sep = ";")
def limpieza():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegacion = pd.read_csv("navegacion.csv", sep = ";")
    index = []
    for i in range(conversiones.shape[0]):
        if conversiones._get_value(i, "id_user") == "None":
            index.append(i)
    conversiones = pd.DataFrame(conversiones.drop(conversiones.index[index]), columns = conversiones.columns)
    conversiones = conversiones.reset_index()
    print("El numero de visitas que recibe es:", navegacion.shape[0], "visitas")
    print("El numero de conversiones que recibe es:", conversiones.shape[0]*100, "conversiones", end= "%")
    print("")
    print("El numero de conversiones que no recibe es:", navegacion.shape[0] - conversiones.shape[0]*100, "conversiones", end= "%")
    print("")
    return
limpieza()

def tipo_conversion():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegaciones = pd.read_csv("navegacion.csv", sep = ";") 
    call = 0
    form = 0
    tipo = conversiones["lead_type"]
    for i in tipo:
        if i == "call":
            call += 1
        elif i == "form":
            form += 1
    print("El numero de conversiones de tipo call es:", call)
    print("El numero de conversiones de tipo form es:", form)
    return
tipo_conversion()

def recurrentes():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegaciones = pd.read_csv("navegacion.csv", sep = ";")
    recurrente = {()}
    number_of_users = {()}
    for i in range(navegaciones.shape[0]):
        number_of_users.add(navegacion._get_value(i, "id_user"))
        if navegaciones._get_value(i, "user_recurrent") == True:
            recurrente.add(navegaciones._get_value(i, "id_user"))
    print("El porcentaje de usuarios que son recurrentes es:", len(recurrente)/len(number_of_users)*100, "%")
    return
recurrentes()

def union_tabla():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegaciones = pd.read_csv("navegacion.csv", sep = ";")
    data = []
    only_user = navegacion["id_user"]
    for user in only_user:
        convierte = False
    for i in conversiones["id_user"]:
        if user == i:
            convierte = True
    
    if convierte:
        data.append(1)
    else:
        data.append(0)

    navegacion["convierte"] = data 
    return
union_tabla()  



def coches():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegaciones = pd.read_csv("navegacion.csv", sep = ";")
    cars={

    }

    for i in range(navegaciones.shape[0]):
        m= re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", str(navegacion._get_value(i, "url_landing")))
        if m != None:
            if m.groups()[0] in cars:
                cars[m.groups()[0]] += 1
            else:
                cars[m.groups()[0]] = 1
    for car in cars.keys():
        print("El coche " , car,"Ha sido buscado" , cars[car], "veces")
    return
coches()


