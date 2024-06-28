
# pandas est un package pour la manipulation et l'analyse des données
# Pour installer pandas, on a utilisé la commande:
# !pip install pandas
# Pour l'importer:
# import pandas as pd

# matplotlib est un package pour la création de graphiques et de visualisations de données
# Pour installer matplotlib, on a utilisé la commande:
# !pip install matplotlib
# Importation
# import matplotlib.pyplot as plt

# Cette ligne lit le fichier CSV 'Housing.csv' et stocke les données dans un DataFrame pandas appelé 'df'. 
# df = pd.read_csv('Housing.csv')

# Afficher les premières lignes du dataset pour un aperçu des données
# df.head()

# Création d'un histogramme pour la colonne 'bedrooms'
# df['bedrooms'].plot(kind='hist')
# Cette ligne crée un histogramme pour visualiser la distribution des valeurs dans la colonne 'bedrooms' du DataFrame.
# Affichage du graphique avec la ligne 
#plt.show()

# Création d'un graphique de dispersion pour les colonnes 'area' et 'price'
# plt.scatter(df['area'], df['price'])
# Cette ligne crée un graphique de dispersion avec 'area' sur l'axe des x et 'price' sur l'axe des y pour visualiser leur relation.

# Ajout d'un titre au graphique
# plt.title('Graphique de dispersion: Area vs Price')

# Cette ligne affiche le graphique créé par matplotib 
# plt.show()

