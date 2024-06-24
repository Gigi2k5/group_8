import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
df=pd.read_csv('Housing.csv')
df.head()
# Créer le graphique de dispersion
plt.scatter(df['area'], df['price'])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Graphique de dispersion: Area vs Price')
plt.show()
"""
Commentaire sur le nuage de point obtenu 
Ici le graphique nous montre que au fur et à mesure que la surface occupée
par l'appartement augmente, il y a aussi une agmentation du prix de cet appartement.
On peut conclure que les variables price et area sont corrélées positivement.
Pour plus d'informations on peut réliser une matrice de corrélation qui va démontrer cette forte corrélation entre ces deux features.
"""