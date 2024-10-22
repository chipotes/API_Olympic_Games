# # Nobook de desarollo API juegos olimpicos
# ---
# -Importando librerias

# %%
import pandas as pd
import numpy as np
from fastapi import FastAPI

# %% [markdown]
# ### Instanciando fastapi
# ---
# La instanciación es el proceso de leer o especificar información, como los valores y el tipo de almacenamiento de un campo de datos.

# %%
app = FastAPI() #carga la fastapi en una variable, la vamos a intanciar con la varia app

# %% [markdown]
# ### Cargar datos
# ---

# %%
df =pd.read_parquet("Data/Dataset.parquet")

# %% [markdown]
# ### Funciones
# ---

# %%
@app.get('/Medals') # es un decorador
def index(): 
    return{"API":"Online"} 
#esta funcion la muestra en el inicio de la pagina

# %% [markdown]
# ### Funcion medals
# ---
# 

# %%
@app.get('/Medals/')
def medals():
    medals=df['Medals'].value_counts()
    return {medals.index[0]:medals.values[0],
            medals.index[1]:medals.values[1],
            medals.index[2]:medals.values[2]}

# %% [markdown]
# ### Funcion medals_country
# ---
# 

# %%
@app.get('/Medal_country/{Pais}')
def medal_country(Pais:str):
    filtro = df[df['Team']==Pais]
    medallas = filtro['Medal'].value_counts()
    dic = {}
    for i in range(len(medallas)):
        dic[medallas.index[i]]= int(medallas.values[i])
    return dic

# %%
medal_country('Mexico')

# %% [markdown]
# ### funcion Medals_year [año]
# ---
# 

# %%
@app.get('/medal_year/{year}')
def medal_year(year:int):
    filtro = df[df['Year']==year]
    medallas = filtro['Medal'].value_counts()
    dic = {}
    for i in range(len(medallas)):
        dic[medallas.index[i]]= int(medallas.values[i])
    return dic


# %%
medal_year(2000)

# %% [markdown]
# ### Funcion athletes (Nombre)
# ---
# 

# %%
@app.get('/athletes/{nombre}')
def athletes (nombre:str):
    filtro = df[df['Name']==nombre]
    dic = {}
    if filtro.empty:
        return{'Error':'Revise los datos imgresados'}
    dic['Nombre']=nombre
    dic['Sexo']= filtro['Sex'].values[0]
    dic['Edad']= int(filtro['Age'].values[0])
    dic['Pais'] =list(filtro['Team'].value_counts().index) #value_counts muestra valores unicos y cuantas veces se repite un valor
    dic['juegos'] =list(filtro['Games'].value_counts().index)
    dic['Evento'] =list(filtro['Event'].value_counts().index)
    medallas = {}
    for i in range(len(filtro['Medal'].value_counts())):
        medallas[filtro['Medal'].value_counts().index[i]]=int (filtro['Medal'].value_counts().values[i])
    dic['Medallas']= medallas
    return dic

# %%
athletes('A Lamusi')


