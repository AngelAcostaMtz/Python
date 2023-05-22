import csv

with open("archivos\\csv.txt") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
            print (row)