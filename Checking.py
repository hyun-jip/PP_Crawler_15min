import csv

def checking_data():
    READ_DATA = []
    file = open("DATA.csv",  encoding='utf-8-sig', mode="r", newline="")
    reader = csv.reader(file)
    for row in reader:
        READ_DATA.append(row[0])
    READ_DATA = list(set(READ_DATA))
    return READ_DATA
