import csv
import pandas

with open('weather_data.csv', 'r') as file_csv:
    csv_reader = csv.reader(file_csv)
    temp = []
    for row in csv_reader:
        if row[1].isnumeric():
            temp.append(int(row[1]))

    print(temp)

data = pandas.read_csv('weather_data.csv')
print(data)  # DataFrame
print()
print(data['temp'])  # Series

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

avrg = sum(temp_list) / len(temp_list)
print(avrg)

print(data['temp'].mean())
print(data['temp'].max())

print(data.temp)  # col
print(data[data.day == "Monday"])  # row

print(data[data.temp == data['temp'].max()])

monday = data[data.day == 'Monday']
print(monday.condition) # dla tego tu

print(data[data.day == 'Monday']['temp'])

# data = pandas.DataFrame(data_dict) -> data.to_csv("filename/path")
