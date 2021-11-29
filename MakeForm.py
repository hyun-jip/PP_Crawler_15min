import csv

file = open("Form.csv", encoding='utf-8-sig', mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["start_date(YYYYMMDD)", "20210901"])
writer.writerow(["end_date(YYYYMMDD)", "20210902"])
writer.writerow([""])
writer.writerow(["1710023462", "power001"])
writer.writerow(["1710012009", "power001"])

file.close()