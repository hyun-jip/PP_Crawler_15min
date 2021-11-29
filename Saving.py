import csv

def save_to_file(PP_ID, DATA_LIST):
  file = open("DATA.csv",  encoding='utf-8-sig', mode="a", newline="")
  writer = csv.writer(file)
 #  writer.writerow(["ismart_id", "mr_ymd", "mr_hhmi", "pwr_qty"])
  for index in DATA_LIST:
    temp = list(index.values())
    writer.writerow(temp)
  if(DATA_LIST==[]):
      print("** CSV파일 추출불가 **")
  else:
      print(f"** 고객번호 {PP_ID} 추출완료 **")
  return