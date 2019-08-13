from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

username = ''
pwd = ''

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

browser.maximize_window()

login = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
login.click()

sleep(2)

u = browser.find_element_by_name('username')
u.click()
u.send_keys(username)

p = browser.find_element_by_name('password')
p.click()
p.send_keys(pwd)

login = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
login.click()

sleep(3)

tmp = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
tmp.click()
sleep(2)


pos = browser.find_elements_by_class_name('_9AhH0')
for i in pos:
    i.click()
    browser.execute_script("window.scrollTo(0, 1080)") 