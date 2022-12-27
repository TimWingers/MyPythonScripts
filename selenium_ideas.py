from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://ya.ru")
element = driver.find_element(By.CLASS_NAME, "search3__input-wrapper")
# element.send_keys("search3__input-wrapper", Keys.ENTER)

element = driver.find_element(By.NAME, 'text')
element.click()
driver.close()



####################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://fb.ru/post/coaching/2022/11/27/370666")
element = element = driver.find_element(By.ID, 'yandex_rtb_R-A-70350-14')


######################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.thefactsite.com/do-cats-have-nine-lives/")
welcome = driver.find_element(By.CSS_SELECTOR, '.entry-content')
print(welcome.get_attribute("innerText"))