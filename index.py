from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

dv = webdriver.Chrome('../chromedriver.exe')
dv.get("https://www.naver.com/")



########### elem #############
elem = dv.find_element_by_name("query")
elem.send_keys("맞춤법검사기")
elem.send_keys(Keys.RETURN)
time.sleep(1.3)
elem = dv.find_element_by_class_name("txt_gray")
elem.send_keys("내 이름은 전현준임니다")
elem = dv.find_element_by_class_name("btn_check")
elem.click()


########### BeautifulSoup ###########
soup = BeautifulSoup(dv.page_source, 'html.parser')
print(soup.select("p.result_text.stand.txt")[0].text)

fp = open("1.txt",'r', encoding= "utf-8")
text = fp.read()
print(text)


