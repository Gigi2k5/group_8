library(readr)
df <- read_csv("Housing.csv")
head(df)
# Créer un histogramme de la feature 'bedrooms'
hist(df$bedrooms, main="Histogramme des chambres", xlab="Nombre de chambres", ylab="Fréquence", col="blue", border="black")
