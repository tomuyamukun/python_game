# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))


# average = round(sum(temp_list) / len(temp_list), 1)
# print(average)

# 普通にやる
# i = 0
# for temp in temp_list:
#     i += temp
# average_temp = round(i / len(temp_list))
# print(average_temp)

# pandas使用
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data['temp'].mean())
# print(data["temp"].max())

# Get Data in column
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

#  create DataFrame
# data_dict = {
#     "students": ["Any", "Jurias", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinammon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")
