import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
df=pd.read_csv('Housing.csv')
df.head()
df['bedrooms'].plot(kind='hist')
"""
Commentaire sur l'histogramme 
Suite à l'analyse de l'histogramme, nous constatons qu'il y a un grand nombre d'appartement avec 3 lit environs 300 appartements,
plus que la moitié du jeu de données. aussi on constate q'il y a une centaine de maisons avec 2 ou 4 lits.après ces appartements
nous avons très peu d'appartements avec 5 lits et presque pas d'appartements avec 6 lits. la conclusion est que la majorité des
appartements dans cette zone ont en moyenne trois lit. 

"""