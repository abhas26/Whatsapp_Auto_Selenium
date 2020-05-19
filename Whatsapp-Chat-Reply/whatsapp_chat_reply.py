import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import urllib.request,urllib.parse,urllib.error

driver= webdriver.Chrome(executable_path="F:\Selenium\web drivers\chromedriver")
act= ActionChains(driver)

form_url= "https://web.whatsapp.com/"
driver.get(form_url)

# Wait for user to scan QR code.
input("Press any key after scanning QR code- ")

# INPUT necessary data.
contact_name= input("Enter the name of the conatct that you want to reply: ")

# INITIALIZING X_PATHS.
contact_Xpath= "//span[contains(@title,'" + contact_name + "')]"
dope_Xpath= "//span[contains(@title,'Dope')]"

# CLICKING ON DOPE CHAT AND WAITING FOR MESSAGE FROM CONTACT_NAME.
driver.find_element_by_xpath(dope_Xpath).click()

# ------------------------------------------------------------------------------------------------------------
time.sleep(2)

while True:
    # EXTRACTING SOURCE CODE AND CHECKING FOR NEW MESSAGE FROM CONTACT_NAME.
    source_code= driver.page_source
    soup= bs(source_code,'html.parser')

    contact_name_tag= soup.find("span", {"title" : contact_name})
    target_tag= contact_name_tag.find_parent("div", {"class" : "_3j7s9"})       # GETTING PARENT TAG.

    new_msg= target_tag.find("span", {"class" : "OUeyt"})                       # GETTING NOTIFICATION TAG IF PRESENT.

    # CHECKING IF NEW MESSAGE IF PRESENT.
    if new_msg:
        driver.find_element_by_xpath(contact_Xpath).click()
        time.sleep(1)

        input("Press to confirm WHO-")                                          # CONFIRMING CONTACT TO REPLY TO.
        time.sleep(1)

        text_field= driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        text_field.send_keys("Yo Dude!")
        time.sleep(1)
        act.send_keys(Keys.RETURN).perform()
        time.sleep(1)

        driver.find_element_by_xpath(dope_Xpath).click()                          # RETURNING TO DOPE CHAT SO AS TO WAIT FOR NOTIFICATION FROM CONTACT_NAME.
    
    time.sleep(3)                                                                   # REPEAT PROCESS AFTER SPECIFED TIME INTERVAL.

# ------------------------------------------------------------------------------------------------------------
