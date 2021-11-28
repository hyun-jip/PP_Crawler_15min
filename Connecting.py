from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def connect_webpage(driver, PP_ID, PP_PW):
  driver.get("https://pp.kepco.co.kr/")
  assert "한전 파워플래너" in driver.title
  
  input = driver.find_element_by_id("RSA_USER_ID")
  input.send_keys(PP_ID)
  input = driver.find_element_by_id("RSA_USER_PWD")
  input.send_keys(PP_PW)
  input.send_keys(Keys.RETURN)


    
  driver.get("https://pp.kepco.co.kr/rs/rs0101N.do?menu_id=O010201")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loadingwrap')))
  



#  e_num = ['1','2','3','4','5']

#  for e_i, e_v in enumerate(e_num):

#    driver.find_element_by_id("SELECT_DT").click()
#    driver.implicitly_wait(2)
#    Select(driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]")).select_by_value("2")

#    m = driver.find_elements_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr/td")
#    for i in m:
#     if i.text == e_v:
#      i.click()



 # while q<33:
 #   m = driver.find_elements_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr/td")

 #   driver.find_element_by_id("SELECT_DT").click()
 #   sleep(1)
 #   m[q].click()
 #   print(m[q].text)
 #   q = q+1
