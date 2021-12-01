import csv

file = open("Form.csv", encoding='utf-8-sig', mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["start_date(YYYYMMDD)", "20211013"])
writer.writerow(["end_date(YYYYMMDD)", "20211014"])
writer.writerow([""])
writer.writerow(["1710023462", "power001"])
writer.writerow(["1710028582", "power001"])
writer.writerow(["1710008443", "power001"])
writer.writerow(["1016033131", "power001"])
writer.writerow(["1016085174", "power001"])
writer.writerow(["1016045271", "power001"])
writer.writerow(["1016072017", "power001"])
writer.writerow(["1016005661", "power001"])

file.close()