import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome(executable_path="F:\Selenium\web drivers\chromedriver")
form_url= "https://web.whatsapp.com/"

driver.get(form_url)

msg= input("Enter message to be sent- ")
count= int(input("Enter the count- "))

input("Press any key after scanning QR code- ")

contact= driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[15]/div/div/div[2]")
act= ActionChains(driver)   

act.move_to_element(contact).click(contact).perform()
input("Press 1 to confirm: ")
# message_box= driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
# act.move_to_element(message_box).click(message_box).perform()

while True:
    act.send_keys('1')
    act.send_keys(Keys.BACK_SPACE).perform()