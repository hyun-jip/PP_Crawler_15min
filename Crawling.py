from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def crawl_data(driver, PP_ID, DATE_LIST):
     DATA_LIST = []
     for e_i, e_v in enumerate(DATE_LIST):
         wait = WebDriverWait(driver, 10)
         driver.find_element_by_id("SELECT_DT").click()
         driver.implicitly_wait(2)
         Select(driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]")).select_by_value(str(DATE_LIST[e_i][0]))
         Select(driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]")).select_by_value(str(DATE_LIST[e_i][1]-1))

         dates = driver.find_elements_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr/td")

         for date in dates:
             if date.text == str(e_v[2]):
                 date.click()

                 wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loadingwrap')))
                 ActionChains(driver).double_click(on_element=driver.find_element_by_xpath('//*[@id="txt"]/div[2]/div/p[2]/span[1]')).perform()
                 wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loadingwrap')))

                 table = driver.find_element_by_xpath("//*[@id='tableListChart']")
                 tbody = table.find_element_by_tag_name("tbody")
                 rows = tbody.find_elements_by_tag_name("tr")

                 print(f"고객번호 {PP_ID} / {DATE_LIST[e_i][0]}년 {DATE_LIST[e_i][1]}월 {DATE_LIST[e_i][2]}일 데이터 수집중...")

                 for index, value in enumerate(rows):
                     if(value.find_elements_by_tag_name("th")[0].text=="" or value.find_elements_by_tag_name("th")[0].text=="-"):
                         continue

                     if len(str(e_v[1])) == 1:
                         temp_month= "0" + str(e_v[1])
                     else:
                         temp_month = str(e_v[1])

                     if len(str(e_v[2])) == 1:
                         temp_day= "0" + str(e_v[2])
                     else:
                         temp_day = str(e_v[2])

                     DATE_FORMAT = str(e_v[0]) + temp_month + temp_day
                     TIME_SUM = (int(value.find_elements_by_tag_name("th")[0].text[0:2]) * 60) + int(value.find_elements_by_tag_name("th")[0].text[3:5]) - 15
                     TIME = str(divmod(TIME_SUM ,60)[0])
                     MINUTE = str(divmod(TIME_SUM ,60)[1])
                     if len(TIME) == 1:
                         TIME = "0" + TIME
                     if len(MINUTE) == 1:
                         MINUTE = "0" + MINUTE
                     TIME_FORMAT = TIME + MINUTE
                     DATA_LIST.append({"PP_ID": PP_ID, "DATE": DATE_FORMAT , "TIME": TIME_FORMAT, "USAGE": value.find_elements_by_tag_name("td")[0].text})

                 for index, value in enumerate(rows):
                     if(value.find_elements_by_tag_name("th")[1].text=="" or value.find_elements_by_tag_name("th")[1].text=="-"):
                         continue

                     if len(str(e_v[1])) == 1:
                         temp_month= "0" + str(e_v[1])
                     else:
                         temp_month = str(e_v[1])

                     if len(str(e_v[2])) == 1:
                         temp_date= "0" + str(e_v[2])
                     else:
                         temp_date = str(e_v[2])

                     DATE_FORMAT = str(e_v[0]) + temp_month + temp_date
                     TIME_SUM = (int(value.find_elements_by_tag_name("th")[1].text[0:2]) * 60) + int(value.find_elements_by_tag_name("th")[1].text[3:5]) - 15
                     TIME = str(divmod(TIME_SUM ,60)[0])
                     MINUTE = str(divmod(TIME_SUM ,60)[1])
                     if len(TIME) == 1:
                         TIME = "0" + TIME
                     if len(MINUTE) == 1:
                         MINUTE = "0" + MINUTE
                     TIME_FORMAT = TIME + MINUTE
                     DATA_LIST.append({"PP_ID": PP_ID, "DATE": DATE_FORMAT , "TIME": TIME_FORMAT, "USAGE": value.find_elements_by_tag_name("td")[7].text})

     ActionChains(driver).double_click(on_element=driver.find_element_by_xpath('//*[@id="gml"]/a[2]')).perform()
    
     return DATA_LIST
   