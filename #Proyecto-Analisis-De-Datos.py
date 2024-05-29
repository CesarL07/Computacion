#Proyecto Final
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#CREACION DEL DATASET:
IMDB_DATA=pd.read_csv("D:/PYTHON/imdb_data.csv")
print("===========================================================")

#LIMPIEZA DE DATOS
#Eliminamos columnas innecesarias:
IMDB_DATA=IMDB_DATA.drop(["Poster", "Cast", "Description", "Review Title", "Review"], axis=1)

#Cambiemos los tipos de datos necesarios:
IMDB_DATA["Year"]=pd.to_numeric(IMDB_DATA["Year"])

#Eliminamos los valores nulos y duplicados:
IMDB_DATA=IMDB_DATA.dropna()
IMDB_DATA=IMDB_DATA.drop_duplicates()

#Verifiquemos informacion general de nuestro DF:
print(IMDB_DATA.shape)
print(IMDB_DATA.info())
print(IMDB_DATA.describe())

print("===========================================================")
#GRAFICAS DESCRIPTIVAS

#Produccion de peliculas por año:
M_PY=IMDB_DATA["Year"].value_counts()
graph1=M_PY.plot(kind="bar", xlabel="Año", ylabel="Número de peliculas")
plt.gca().invert_xaxis()
for container in graph1.containers:
    graph1.bar_label(container, rotation=90)
plt.title("Produccion de peliculas por año")
plt.show()

#Distribucion de peliculas por generos:
IMDB_DATA["Genre"]=IMDB_DATA["Genre"].dropna()
G_I=IMDB_DATA["Genre"].str.split(", ", expand=True).stack()
D_PG=G_I.value_counts()
graph2=D_PG.plot(kind="pie", autopct="%1.1f%%", startangle=90)
graph2.set_title("Distribucion de peliculas por generos")
graph2.set_ylabel("")
plt.show()

#Distribucion de calificaciones
graph3=sns.histplot(data=IMDB_DATA["Rating"], bins=25, kde=True, color="b")
graph3.set_title("Distribución de calificaciones")
graph3.set_xlabel("Calificaciones")
graph3.set_ylabel("Frecuencia")
plt.show()

#Numero de reviews por año
#Primero eliminamos las comillas que separan los digitos:
IMDB_DATA["Review Count"]=IMDB_DATA["Review Count"].str.replace(",", "").astype(int)
NR_PY=IMDB_DATA.groupby("Year")["Review Count"].sum()
graph4=NR_PY.plot(kind="bar", x="Año", ylabel="Numero de reviews")
graph4.set_title("Número de reviews por año")
plt.show()

#Peliculas con mayor calificacion (10)
T10_BRM=IMDB_DATA.sort_values(by="Rating", ascending=False).head(10)
graph5=plt.bar(T10_BRM["Title"], T10_BRM["Rating"])
plt.title("10 peliculas mejor calificadas segun IMDB")
plt.xlabel("Peliculas")
plt.ylabel("Calificación")
plt.xticks(rotation=90)
plt.show()

#Peliculas peor calificadas (10)
T10_WRM=IMDB_DATA.sort_values(by="Rating", ascending=True).head(10)
graph6=plt.bar(T10_WRM["Title"], T10_WRM["Rating"])
plt.title("10 peliculas peor calificadas segun IMDB")
plt.xlabel("Peliculas")
plt.ylabel("Calificación")
plt.xticks(rotation=90)
plt.show()

#Directores mejor calificados (10)
fig,axes=plt.subplots()
df_D=IMDB_DATA.groupby("Director")
df_DM=pd.DataFrame(df_D["Rating"].mean())
df_DM=df_DM.sort_values("Rating", ascending=False)
sns.barplot(x=df_DM.index[:10], y=df_DM.iloc[:10, 0].values, ax=axes)
plt.title("10 directores mejor calificados")
plt.xlabel("Directores")
plt.ylabel("Calificacion Promedio")
plt.xticks(rotation=90)
plt.show()

#Directores con peor calificacion (10):
fig,axes=plt.subplots()
df_D=IMDB_DATA.groupby("Director")
df_DM=pd.DataFrame(df_D["Rating"].mean())
df_DM=df_DM.sort_values("Rating", ascending=True)
sns.barplot(x=df_DM.index[:10], y=df_DM.iloc[:10, 0].values, ax=axes)
plt.title("10 directores peor calificados")
plt.xlabel("Directores")
plt.ylabel("Calificacion Promedio")
plt.xticks(rotation=90)
plt.show()

#Peliculas con mayor numero de reviews (10):
T10_MRM=IMDB_DATA.sort_values(by="Review Count", ascending=False).head(10)
sns.barplot(x=T10_MRM["Title"], y=T10_MRM["Review Count"])
plt.title("10 peliculas con mayor numero de reviews")
plt.xlabel("Pelicula")
plt.ylabel("Numero de reviews")
plt.xticks(rotation=90)
plt.show()

#Evolucion de calificaciones y metascores por año
AR_PY=IMDB_DATA.groupby("Year")["Rating"].mean()
AM_PY=IMDB_DATA.groupby("Year")["Metascore"].mean()/10

plt.plot(AR_PY, marker="o", color="blue", label="Rating")
plt.plot(AM_PY, marker="o", color="orange", label="Metascore")
plt.xlabel("Año")
plt.ylabel("Promedio")
plt.title("Promedio de Calificaciones y Metascores de Películas a lo Largo de los Años")
plt.legend()
plt.show()

print("===========================================================")

#GRAFICOS COMPARATIVOS:

#Grafica de dispersion (duracion y rating)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Duration (min)", y="Rating", data=IMDB_DATA)
plt.title("Relación entre Duración de la Película y Calificación")
plt.xlabel("Duración (min)")
plt.ylabel("Calificación")
plt.show()

#Grafica de caja (genero y rating)
IMDB_DATA["Genre"]=IMDB_DATA["Genre"].str.split(", ")
IMDB_DATA_EXPLODED=IMDB_DATA.explode("Genre")
plt.figure(figsize=(12, 8))
sns.boxplot(data=IMDB_DATA_EXPLODED, x="Genre", y="Rating")
plt.title("Distribución de Calificaciones por Género")
plt.xlabel("Género")
plt.ylabel("Calificación")
plt.xticks(rotation=90) 
plt.show()

#Grafico de correlacion
Numeric_Data=IMDB_DATA.select_dtypes(include=["float64", "int64"])
corr=Numeric_Data.corr(method="spearman")
print(corr)
graph7=sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
graph7.set_title("Matriz de correlacion de los valores numericos")
plt.show()

print("===========================================================")

#PREDICCION DE CALIFICACION CON Sckit-Learn

#Primero hacemos la limpieza de la columna "Votes" - Para eliminar las comillas que separan los digitos
#Lo hice de este modo por que de otra forma no me funcionaba (no se por que)
columna=["Votes"] 
for element in columna:
    IMDB_DATA[element]=IMDB_DATA[element].str.replace(",", "").astype(float)
x = IMDB_DATA[["Year", "Duration (min)", "Metascore", "Votes", "Review Count"]]
y = IMDB_DATA["Rating"]

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#Este es el modelo que vamos a utilizar
modelo=RandomForestRegressor()

#Aqui se entrena al modelo
modelo.fit(X_train, y_train)

#Aqui estan las metricas de la prediccion
y_pred=modelo.predict(X_test)
mse=mean_squared_error(y_test, y_pred)
rf_r2s=r2_score(y_test, y_pred)
print(f"Desviacion estandar: {mse}")
print(f"R2: {rf_r2s}")

print("===========================================================")

#Aqui probamos al modelo con una pelicula existente:
blade_runner_2049={
    "Year": [2017],  
    "Duration (min)": [164],  
    "Metascore": [81], 
    "Votes": [481566],  
    "Review Count": [5807]  
}
df_blade_runner=pd.DataFrame(blade_runner_2049)
rating_predicho = modelo.predict(df_blade_runner)
print(f"Rating predicho para BladeRunner 2049: {round(rating_predicho[0],2)}")
print(f"La calificacion verdadera es : {8.0}")
