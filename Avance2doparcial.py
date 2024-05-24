#Valentina Dominguez
#Fabrizio Chera
#Arturo Machuca

#EN ESTE AVANCE DEFINIMOS LAS FORMAS EN LAS QUE VAMOS A GRAFICAR LOS RESULTADOS DE NUESTRO MODELO FINAL A LA VEZ ESTO NOS DA UNA HERRAMIENTA PARA COMPARAR LAS
# VARIABLES INDEPENDIENTES Y QUE IMPORTANCIA Y PESO TIENEN EN LAS FUTURAS PREDICCIONES, GRACIAS A ESTO TENDREMOS UNA IDEA DE LAS VARIABLES MAS IMPORTANTES PARA LA
# PREDICCION.
#LA BASE DE DATOS PROPORCIONADA EN EL AULA FUE MODIFICADA DE TAL FORMA QUE LA PRIMERA FILA DE LA PRIMERA COLUMNA LE PONEMOS EL NOMBRE DE "Fechas"

#Librerias necesarias

#pip install pandas
#pip install chart-studio
#pip install plotly

#Utilizaremos plotly porque vimos que es relativamente sencillo de utilizar y nos permite hacer graficos iterativos de buena calidad,y tambien que nos resulto facil
# de entender la documentacion de la libreria

import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go

#importamos la base de datos y agregamos la opcion de parse_dates = True para que pandas trate de identificar automaticamente las columnas que pueden ser fechas
# y luego utilizaremos index_col='Fechas' para que pandas utilice los valores de la columna 'Fechas' para etiquetar las filas osea se esa columna se convierte en los
# indices del dataset

data = pd.read_csv('NuevoTPIA_Actualizado.csv', parse_dates = True, index_col='Fechas')

# Mostramos en el terminal las primeras filas del dataset y ver el formato del mismo 

print(data.head())

#Creamos varios objetos go.Scatter para cada variable independiente del dataset que luego veremos para utilizar en un grafico iterativo utilizando plotly

temperatura = go.Scatter(x=data['T02M'].index, y=data['T02M'].values, name = 'Temperatura', line=dict(color='royalblue', width=0.7), yaxis='y')
humedad = go.Scatter(x=data['RH2M'].index, y=data['RH2M'].values, name = 'Humedad', line=dict(color='lightblue', width=0.7), yaxis='y')
presion = go.Scatter(x=data['PRSS'].index, y=data['PRSS'].values, name = 'Presion', line=dict(color='orange'), yaxis='y')
direccion_u = go.Scatter(x=data['U10M'].index, y=data['U10M'].values, name = 'U10M', line=dict(color='chocolate'), yaxis='y')
direccion_v = go.Scatter(x=data['V10M'].index, y=data['V10M'].values, name = 'V10M', line=dict(color='blueviolet'), yaxis='y')
demanda = go.Scatter(x=data['SIN Imputed'].index, y=data['SIN Imputed'].values, name = 'Demanda', line=dict(color='mediumvioletred', width=0.7), yaxis='y2')

#Creamos un objeto 'go.Layout' que define de cierta forma el diseno del grafico
#No falta aun muchos datos por ejemplo la unidad de medida de la demanda electrica suponemos que es MWh pero no sabemos

layout_temp = go.Layout(title='Temperatura y Demanda Electrica', xaxis=dict(title='Fecha'),
                   yaxis=dict(title='ºC', color='royalblue', overlaying='y2'),
                   yaxis2=dict(title='MWh?', color='purple', side='right'))

#Aqui combinamos los datos a graficar usando el diseno previamente definido

fig = go.Figure(data=[temperatura, humedad, demanda], layout=layout_temp)

#Mostramos el grafico iterativo 

fig.show()