from Connecting import connect_webpage
from Crawling import crawl_data
from selenium import webdriver
from MakeDates import Make_Dates
from ReadForm import read_form
from Saving import save_to_file
from Checking import checking_data


PATH = 'C:/Users/10149072/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)
  
START_YEAR, START_MONTH, START_DAY, END_YEAR, END_MONTH, END_DAY, IDPW_LIST = read_form()
DATE_LIST = Make_Dates(START_YEAR, START_MONTH, START_DAY, END_YEAR, END_MONTH, END_DAY)

RESTART = input("데이터를 이어서 수집하는 경우 인가요? (y/n): ")

if RESTART == "y":
  try:
    RESTART_DATA = checking_data()
    for row1 in RESTART_DATA:
      for index, value in enumerate(IDPW_LIST):
        if row1 == value[0]:
          del IDPW_LIST[index]

    for account in IDPW_LIST:
      login = connect_webpage(driver, account[0], account[1])
      if login:
        CRAWLING_DATA = crawl_data(driver, account[0], DATE_LIST)
        save_to_file(account[0], CRAWLING_DATA)

  except:
    print("입력 form이 변경됐습니다.")

else:
  for account in IDPW_LIST:
    login = connect_webpage(driver, account[0], account[1])
    if login:
      CRAWLING_DATA = crawl_data(driver, account[0], DATE_LIST)
      save_to_file(account[0], CRAWLING_DATA)
 