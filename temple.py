from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep
df=pd.read_excel(r'E:\karthik\manoj\temple\Tripadvisor_Temples_Rev 29.xlsx',engine='openpyxl')
browser=webdriver.Chrome()
browser.get('https://www.google.com/maps')
excel=open(r'E:\karthik\manoj\temple\temple_30_05_part 2.xls','w',encoding='utf-8')
for i in df.index[2886:]:
    aa=df['Latitude'][i]
    bb=df['Longitude'][i]
    browser.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys(aa,",",bb)
    sleep(2)
    browser.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]').click()
    sleep(3)
    s=browser.page_source
    v=bs(s,'html.parser')
    a=v.find('div',{'class':'MngOvd fontBodyMedium zWArOe'}).find('span',{'class':'DkEaL'})
    ad=a.text
    print(i,ad)
    excel.write(repr(aa)+'\t'+repr(bb)+'\t'+repr(ad)+'\n')
    browser.find_element(By.CLASS_NAME,'yAuNSb').click()
    sleep(1)
    
excel.close()
