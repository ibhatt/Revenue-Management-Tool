import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
i = datetime.datetime.now()
#print (i)

day = i.day
month = i.month
year = i.year


browser = webdriver.Firefox()
type(browser)


for date in range (0,1):
   
    browser.get('http://expedia.com')

    browser.find_element_by_xpath("/html/body/section/div/div/div/section/div[1]/div/ul/li[2]/a/span[1]").click()

    typeName = browser.find_element_by_id("hotel-destination")
    typeName.send_keys("Redwood City, CA")

    browser.find_element_by_id("hotel-checkin").send_keys(str(month)+"/"+str(day)+"/"+str(year))
    browser.find_element_by_link_text("30").click()

    day = day+1
    browser.find_element_by_id("hotel-checkout").send_keys(str(month)+"/"+str(day)+"/"+str(year))
    

    browser.find_element_by_id("search-button").click()
    
    browser.find_element_by_id("inpHotelNameMirror").send_keys("Pacific Euro Hotel, Redwood City, CA")
