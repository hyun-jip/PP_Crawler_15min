import csv

def read_form():
    FORM_LIST = []
    IDPW_LIST = []
    file = open("Form.csv", encoding='utf-8-sig', mode="r", newline="")
    reader = csv.reader(file)

    for line in reader:
        FORM_LIST.append(line)

    START_YEAR = int(FORM_LIST[0][1][0:4])
    START_MONTH = int(FORM_LIST[0][1][4:6])
    START_DAY = int(FORM_LIST[0][1][6:8])
    END_YEAR = int(FORM_LIST[1][1][0:4])
    END_MONTH = int(FORM_LIST[1][1][4:6])
    END_DAY = int(FORM_LIST[1][1][6:8])
 
    IDPW_LIST = FORM_LIST[3:]
    
    return START_YEAR, START_MONTH, START_DAY, END_YEAR, END_MONTH, END_DAY, IDPW_LIST

