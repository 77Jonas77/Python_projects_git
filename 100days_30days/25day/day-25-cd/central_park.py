import pandas

# task1
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data)

print(data["Primary Fur Color"].value_counts())

# albo

print(len(data[data["Primary Fur Color"] == "Gray"]))
print(len(data[data["Primary Fur Color"] == "Cinnamon"]))
print(len(data[data["Primary Fur Color"] == "Black"]))

data_dict = data["Primary Fur Color"].value_counts().to_dict()

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
