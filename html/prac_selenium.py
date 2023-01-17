from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)


browser = webdriver.Chrome(options=chrome_options)

browser.get("http://naver.com")
browser.find_element(By.XPATH, '//*[@id="query"]').send_keys("코딩")
browser.find_element(By.XPATH, '//*[@id="query"]').send_keys(Keys.ENTER)

time.sleep(1)
