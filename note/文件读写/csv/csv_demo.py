import csv

list1 = ["name", "age", "city"]
with open('demo.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(list1)

with open('demo.csv', 'r', encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
