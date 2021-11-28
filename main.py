from Connecting import connect_webpage
from Crawling import crawl_data
from selenium import webdriver
from MakeDates import Make_Dates
from ReadForm import read_form
from Saving import save_to_file


PATH = 'C:/Users/10149072/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)
  
START_YEAR, START_MONTH, START_DAY, END_YEAR, END_MONTH, END_DAY, IDPW_LIST = read_form()
DATE_LIST = Make_Dates(START_YEAR, START_MONTH, START_DAY, END_YEAR, END_MONTH, END_DAY)

for account in IDPW_LIST:
    connect_webpage(driver, account[0], account[1])
    CRAWLING_DATA = crawl_data(driver, account[0], DATE_LIST)
    save_to_file(account[0], CRAWLING_DATA)
