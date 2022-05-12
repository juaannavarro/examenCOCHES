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
    return
limpieza()