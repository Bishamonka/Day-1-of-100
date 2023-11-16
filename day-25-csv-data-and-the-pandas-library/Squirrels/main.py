import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

number_of_grey = int(len(data[data["Primary Fur Color"] == "Gray"]))
number_of_red = int(len(data[data["Primary Fur Color"] == "Cinnamon"]))
number_of_black = int(len(data[data["Primary Fur Color"] == "Black"]))

squirrel_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [number_of_grey, number_of_red, number_of_black]
}

df = pandas.DataFrame(squirrel_count)
df.to_csv("squirrel_count.csv")

print(df)
