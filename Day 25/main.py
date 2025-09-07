# # with open("weather_data.csv") as data_file:
# #     data=data_file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data.csv", mode='r') as data:
# #     reader = csv.reader(data)
# #     temperatures=[]
# #     for row in reader:
# #         if row[1]!="temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
# data= pandas.read_csv("weather_data.csv")
# # print(data)
# # print(type(data))
# # print(data["temp"])
# # Dataframe: whole table
# # series: one single list ex: temp in our current dataset
#
# data_dict=data.to_dict()
# print(data_dict)
#
# data_temp=data["temp"].to_list()
# print(data_temp)
# print(data["temp"].mean())   # caclulate avg
# print(data["temp"].max())
# print(data.temp.max())
#
# print(data.condition)
#
#
# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday=data[data.day=="Monday"]
# monday_temperature=monday.temp[0]
# monday_temp_f=monday_temperature*9/5+32
# print(monday_temp_f)
#
#
# # Create a dataframe from scratch
# data_dict={
#     "students":["Any","Janes","Angela"],
#     "scores":[76,56,65],
# }
#
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#

import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"] == "Black"])

data_dict={
    "Fur Color":["Gray", "Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count],
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_countt.csv")