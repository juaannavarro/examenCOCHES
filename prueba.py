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

recurrente = {()}
number_of_users = {()}

for i in range(navegacion.shape[0]):
    number_of_users.add(navegacion._get_value(i, "id_user"))
    if navegacion._get_value(i, "user_recurrent") == True:
        recurrente.add(navegacion._get_value(i, "id_user"))
print("El porcentaje de usuarios recurrentes frente a los totales es de:", len(recurrente) / len(number_of_users) * 100, end="%\n")

#Unir a la tabla de navegacion si convierte o no.
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
#Ahora navegacio contiene todos los datos de si ese usuario convierte o no.

#Ver cual es el coche más visitado de la página.
cars = {
    
}

for i in range(navegacion.shape[0]):
    m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", str(navegacion._get_value(i, "url_landing")))
    if m != None:
        if m.groups()[0] in cars:
            cars[m.groups()[0]] += 1
        else:
            cars[m.groups()[0]] = 1
        
for car in cars.keys():
    print("El coche", car, "ha sido buscado", cars[car], "veces")

#Separar cada una de las partes para añair a la tabla
campaña = []
adg = []
adv = []
sl = []
urls = navegacion["url_landing"]
#Valor del id campaña
for url in urls:
    try:
        esp = str(url).split("camp=")
        bueno = esp[1].split("&")
        campaña.append(bueno[0])
    except:
        campaña.append(0)
#Valor del id del adgroup
for url in urls:
    try:
        esp = str(url).split("adg=")
        bueno = esp[1].split("&")
        adg.append(bueno[0])
    except:
        adg.append(0)
#valor del adv
for url in urls:
    try:
        esp = str(url).split("adv=")
        bueno = esp[1].split("&")
        adv.append(bueno[0])
    except:
        adv.append(0)
#valor del sl
for url in urls:
    try:
        esp = str(url).split("sl=")
        bueno = esp[1].split("&")
        sl.append(bueno[0])
    except:
        sl.append(0)
navegacion["id_camp"] = campaña
navegacion["id_adg"] = adg
navegacion["id_adv"] = adv
navegacion["id_sl"] = sl

print(navegacion)
#Esto es para guardar el fichero final, comentar si no se usa
navegacion.to_csv("navegacion_final.csv", index = False)