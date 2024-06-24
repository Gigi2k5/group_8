library(readr)
df <- read_csv("c:\Users\NOUKON Gilberto\projet_python\Group_x\Task_2\Hist.R:2:20")
head(df)
# Créer un histogramme de la feature 'bedrooms'
hist(df$bedrooms, main="Histogramme des chambres", xlab="Nombre de chambres", ylab="Fréquence", col="blue", border="black")