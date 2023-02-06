import csv

def read_csv(filename, limit, offset):
    with open(filename) as file:
        l = []
        reader = csv.reader(file)
        dreader = csv.DictReader(file, next(reader))
        for i in range(offset):
            next(dreader)
        for i in range(limit):
            l.append(next(dreader))
        return l