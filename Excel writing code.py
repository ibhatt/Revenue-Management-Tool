import xlwt

from bs4 import BeautifulSoup

wb = xlwt.Workbook()

ws1 = wb.add_sheet('Sheet1')

n = 0

ws1.row(n).write(0,'Name')

n = n + 1

for i in range(0,3):    

    ws1.row(n).write(0,'Ish')

    n = n + 1

wb.save('C:\\Users\\ish\Documents\\Name.xls')
    
