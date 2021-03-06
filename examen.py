import re
import numpy as np
import pandas as pd
from numpy import shares_memory
from numpy.lib.function_base import append
from pandas import tseries
import matplotlib.pyplot as plt
import seaborn as sns 
import decorator as dec





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
    sns.countplot(conversiones["id_user"])
    plt.xticks(rotation= 90 )
    plt.show()
    print("El numero de visitas que recibe es:", navegacion.shape[0], "visitas")
    return
limpieza()

def conversion():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegaciones = pd.read_csv("navegacion.csv", sep = ";")
    convertidos = 0
    users_navegacion = navegacion["id_user"]
    users_conversion = conversiones["id_user"]
    for user_nav in users_navegacion:
        for user_conv in users_conversion:
            if user_nav == user_conv:
                convertidos += 1
    numero = [convertidos/navegaciones.shape[0]*100, 100-convertidos/navegaciones.shape[0]*100]
    labels = ["Convertidos", "No convertidos"]
    plt.pie(numero, labels = labels, autopct = "%1.1f%%")
    plt.show()
    print("El porcentaje de visitas a convertidos es de ", convertidos/navegaciones.shape[0]*100, "%")
    print("El porcentaje de visitas que no son convertidos es de ", 100-convertidos/navegaciones.shape[0]*100, "%")


    return
conversion()


def tipo_conversion():
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
    navegaciones = pd.read_csv("navegacion.csv", sep = ";") 
    call = 0
    form = 0
    tipo = conversiones["lead_type"]
    for i in tipo:
        if i == "CALL":
            call += 1
        else:
            form += 1
    sns.countplot(conversiones['lead_type'])
    plt.xticks(rotation= 90 )
    plt.show()
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
    porcentaje= [len(recurrente)/len(number_of_users)*100, 100-len(recurrente)/len(number_of_users)*100]
    labels = ["Recurrentes", "No recurrentes"]
    plt.pie(porcentaje, labels = labels, autopct = "%1.1f%%")
    plt.show()
    print("El porcentaje de usuarios que son recurrentes es:", len(recurrente)/len(number_of_users)*100, "%")
    return
recurrentes()
def unir_conversiones():
    navegacion = pd.read_csv("navegacion.csv", sep = ";")
    conversiones = pd.read_csv("conversiones.csv", sep = ";")
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
unir_conversiones()

def coche_mas_visitado():
    navegacion = pd.read_csv("navegacion.csv", sep = ";")

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
    return
coche_mas_visitado()

def separar_partes():
    navegacion = pd.read_csv("navegacion.csv", sep = ";")
    navegacion["url_landing"] = navegacion["url_landing"].str.split("/")
    campa??a = []
    adg = []
    adv = []
    sl = []
    urls = navegacion["url_landing"]
    for url in urls:
        try:
            esp = str(url).split("camp=")
            bueno = esp[1].split("&")
            campa??a.append(bueno[0])
        except:
            campa??a.append(0)
    for url in urls:
        try:
            esp = str(url).split("adg=")
            bueno = esp[1].split("&")
            adg.append(bueno[0])
        except:
            adg.append(0)
    for url in urls:
        try:
            esp = str(url).split("adv=")
            bueno = esp[1].split("&")
            adv.append(bueno[0])
        except:
            adv.append(0)
    for url in urls:
        try:
            esp = str(url).split("sl=")
            bueno = esp[1].split("&")
            sl.append(bueno[0])
        except:
            sl.append(0)
    navegacion["id_camp"] = campa??a
    navegacion["id_adg"] = adg
    navegacion["id_adv"] = adv
    navegacion["id_sl"] = sl
    return
separar_partes()    

print(navegacion)
def guardar_fichero():
    navegacion.to_csv("navegacion_final.csv", sep = ";")
    return
guardar_fichero()




