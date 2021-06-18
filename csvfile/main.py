# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

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
data_dict = {
    "students": ["Any", "Jurias", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
