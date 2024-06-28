library(readr)
df <- read_csv("Housing.csv")
head(df)
# Créer un scatter plot
plot(df$area, df$price, main="Scatter Plot de Area vs Price", xlab="Area", ylab="Price", pch=19, col="blue")
