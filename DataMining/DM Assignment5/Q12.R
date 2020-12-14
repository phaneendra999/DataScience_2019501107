setwd("E:\\2nd Year\\DataScience_2019501107\\Data Mining\\DM Assignment5")
exams2 <- read.csv("spring2008exams.csv")
str(exams2)
mean2 <- mean(exams$Midterm.2, na.rm = TRUE)
sd2 <- sd(exams$Midterm.2, na.rm = TRUE)
z_score2 <- (exams2$Midterm.2 - mean2)/sd2
sort(z_score2)