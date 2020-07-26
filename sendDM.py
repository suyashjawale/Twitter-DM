from selenium import webdriver
import time
from secrets import id,password

def sendmessage(username,message):
    try:
        browser = webdriver.Chrome()
        browser.get('https://twitter.com/login')
        browser.find_element_by_name("session[username_or_email]").send_keys(id)
        browser.find_element_by_name("session[password]").send_keys(password)
        browser.find_element_by_xpath('//div[@role="button"]').click()
        time.sleep(5)
        browser.get(f"https://twitter.com/{username}")
        time.sleep(5)
        browser.find_element_by_xpath('//div[@aria-label="Message"]').click()
        time.sleep(2)
        browser.find_element_by_xpath("//div[@role='textbox']").send_keys(message)
        time.sleep(3)
        browser.find_element_by_xpath('//div[@aria-label="Send"]').click()
        time.sleep(12)
        browser.close()
        browser.quit()
    except Exception as e:
        print("Error occured : ",e)


#------------target username,Message 
sendmessage("iamRashmika","Hi Rashmika...<3")