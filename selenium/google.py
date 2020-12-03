from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element_by_name("q")
elem.clear()
keyword = "채원"
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

imageList = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)
  
    # 스크롤 다운 후 스크롤 높이 다시 가져옴 mye4qd
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:#결과 더보기 버튼 클릭
            driver.find_element_by_class_name("mye4qd").click()
        except:
             break        
    last_height = new_height

if not os.path.exists(keyword):
        os.makedirs(keyword)

path="C:/pythonEx/selenium/"+keyword+"/"
for i in range(10):
    imageList[i].click()
    time.sleep(2)
    #imgUrl = driver.find_element_by_class_name("n3VNCb").get_attribute("src") 
    imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src") 
    urllib.request.urlretrieve(imgUrl, path+"test"+str(i)+".jpg")




driver.close()