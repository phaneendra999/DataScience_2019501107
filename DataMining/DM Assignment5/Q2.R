data <- read.csv("sonar_test.csv", header = FALSE)
x <- data[,1:2]
plot(x, pch=19, xlab = expression(x[1]), ylab = expression(x[2]))

fit <- kmeans(x, 2)
points(fit$centers, pch = 19, col = "blue", cex = 2)

