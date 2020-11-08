setwd("E:\\2nd Year\\DataScience_2019501107\\Final exam")
data = read.csv("NewAprioriData.csv", header = TRUE);

View(data)
data$TID <- NULL
library(arules)

write.csv(data, "Frequent-Itemsets.csv", quote = FALSE, row.names = TRUE)
transactions = read.transactions("Frequent-Itemsets.csv", sep=',', rm.duplicates = TRUE)
inspect(transactions)

frequent_itemsets <- apriori(transactions, parameter = list(sup = 0.03, conf = 0.5,target="frequent itemsets"))

inspect(sort(frequent_itemsets)[1:15])

itemFrequencyPlot(transactions, topN = 5, col = "blue")