import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import xlwt
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
i = datetime.datetime.now().date()
print (i)

enterMonth = (input("Enter Month: "))
enterDay = (input("Enter Day: "))
enterYear = (input("Enter Year: "))
#n = eval(input("Enter the number of days you want to get rates for: "))

if (enterMonth == "") and (enterDay == "") and (enterYear == ""):
    enterMonth = i.month
    enterDay = i.day
    enterYear = i.year

    date1 = datetime.date(int(i.year), int(i.month), int(i.day))
    

else:
    date1 = datetime.date(int(enterYear), int(enterMonth), int(enterDay))

print (date1)

day = date1.day
month = date1.month
year = date1.year

if (date1 < i):
    print ("Invalid Date. Please enter future date.")
else:
    

    browser = webdriver.Firefox()
    type(browser)

    wb = xlwt.Workbook()

    ws1 = wb.add_sheet('The Euro Hotel', cell_overwrite_ok = True)

    n = 0

    for date in range (0,3):
        

        ws1.row(n).write(1,(str(month) + "/" + str(day) + "/" + str(year)))
       
        browser.get('http://expedia.com/San-Francisco-Hotels-Pacific-Euro-Hotel.h797110.Hotel-Information')

        browser.implicitly_wait(3)    

        browser.find_element_by_id("inp-start-date-eds").send_keys(str(month)+"/"+str(day)+"/"+str(year))

        print ("Day:", day)

        day = day + 1

        if (month == 2) and (day == 30):
            day = 1
            month = month + 1

        if (month == 1) and (day == 32):
            day = 1
            month = month + 1

        if (month == 3) and (day == 32):
            day = 1
            month = month + 1

        if (month == 4) and (day == 31):
            day = 1
            month = month + 1

        if (month == 5) and (day == 32):
            day = 1
            month = month + 1

        if (month == 6) and (day == 31):
            day = 1
            month = month + 1

        if (month == 7) and (day == 32):
            day = 1
            month = month + 1

        if (month == 8) and (day == 32):
            day = 1
            month = month + 1

        if (month == 9) and (day == 31):
            day = 1
            month = month + 1

        if (month == 10) and (day == 32):
            day = 1
            month = month + 1

        if (month == 11) and (day == 31):
            day = 1
            month = month + 1

        if (month == 12) and (day == 32):
            day = 1
            month = 1
            year = year + 1

        
        
        browser.find_element_by_id("eds-submit-action").click()

        #rateAvail = browser.find_element_by_xpath(".//*[@id='hotel0']/a/div[2]/ul[1]/li[1]/ul/div/li[1]/span")
        try:
            rateAvail = (browser.find_element_by_xpath(".//*[@id='hotel0']/a/div[2]/ul[1]/li[1]/ul/div/li[1]/span"))
            print ("Sold Out")

            n = n + 1
            ws1.row(n).write(1, "Property is Sold Out")
            
            n = n + 1
        except NoSuchElementException:
                         
           
            locatersEn = [
                (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[1]/tr/td[4]/div[1]/span[2]"),
                (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[1]/tr/td[4]/div[2]/span[2]"),
                (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[1]/tr/td[4]/div[3]/span[2]")
                ]

            for by, value in locatersEn:
                try:
                    rateCheckEn = browser.find_element(by, value)
                    break
                except NoSuchElementException:
                    pass
            
            
            print ("Rate for Economy Room is", rateCheckEn.text)

            var = rateCheckEn.text

            n = n + 1
            
            ws1.row(n).write(1,"EN")
            ws1.row(n).write(2,var)

            
            locatersEb = [
                 (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[2]/tr[2]/td[4]/div[1]/span[2]"),
                 (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[2]/tr[2]/td[4]/div[2]/span[2]"),
                 (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[2]/tr[2]/td[4]/div[3]/span[2]"),
                 (By.XPATH, ".//*[@id='rooms-and-rates']/div[2]/table/tbody[2]/tr[2]/td[4]/span")
                ]

            for by, value in locatersEb:
                try:
                    rateCheckEb = browser.find_element(by, value)
                    break
                except NoSuchElementException:
                    pass
                
                    
            print ("Rate for Standard Room is", rateCheckEb.text)

            n = n + 1 

            ws1.row(n).write(1,"EB")
            ws1.row(n).write(2,rateCheckEb.text)

            

            n = n + 1
                
                
                    
                    

    wb.save('C:\\Users\\ish\Documents\\RateSheet.xls')
            

