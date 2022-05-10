import re
import numpy
from numpy import shares_memory
from numpy.lib.function_base import append
import pandas as pd
from pandas import tseries

conversiones = pd.read_csv('conversiones.csv', sep=';')
navegaciones = pd.read_csv('navegacion.csv', sep=';')

def leer_Csv(conversiones, navegaciones):
    index = []
    for i in range(conversiones.shape[0]):
        if conversiones.get_value(i, 'id_user') == 'NONE':
            index.append(i)
    conversiones = pd.DataFrame(conversiones.drop(conversiones.index[index]), columns=conversiones.columns)
    conversiones = conversiones.reset_index()
print("El numero de visitas que recibe es:", navegaciones.shape[0], "visitas")
print("El numero de conversiones que recibe es:", conversiones.shape[0]*100, "conversiones", end = "%")
print()
print("El numero de conversiones que no recibe es:", navegaciones.shape[0] - conversiones.shape[0]*100, "conversiones", end = "%")
print()
#leer_Csv("conversiones", "navegacion")



