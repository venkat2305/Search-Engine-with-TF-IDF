from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

website = "https://leetcode.com/problemset/all/"

def get_a_tags(url):
    time.sleep(10)  # important
    ans = []
    links = driver.find_elements(By.TAG_NAME, "a")
    for i in links:
        try:
            if "/problems/" in i.get_attribute("href"):
                # print(i.text)
                # print(i.get_attribute("href"))
                ans.append(i.get_attribute("href"))
        except:
            pass
    ans = list(set(ans))
    # print(ans)
    # print(len(ans))
    return ans

driver.get(website)
sol = []
i=0
while(i<55):
    sol += get_a_tags(driver.current_url)
    next_button = driver.find_element(By.XPATH , '//button[@aria-label="next"]')
    next_button.click()
    i+=1

sol = list(set(sol))
print(len(sol))

#creating a new file and adding all the links
with open("abc.txt" , 'a') as file:
    for j in sol:
        file.write(j+'\n')

driver.quit()