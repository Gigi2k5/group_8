library(readr)
df <- read_csv("c:\Users\NOUKON Gilberto\projet_python\Group_x\Task_2\Hist.R:2:20")
head(df)
# Créer un scatter plot
plot(df$area, df$price, main="Scatter Plot de Area vs Price", xlab="Area", ylab="Price", pch=19, col="blue")