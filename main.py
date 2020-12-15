from pandas import read_csv
read_csv("Squirrels.csv")["Primary Fur Color"].value_counts().to_csv("Fur.csv")
