from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://www.amazon.co.uk/gp/bestsellers/books"
page = requests.get(url)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

for _ in range(500):
  driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)


html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all('div',{'id':'gridItemRoot'})

master_list = []
for item in items:
  data_dict = {}
  data_dict['Title'] = item.find('div',{'class':'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text
  data_dict['Writer'] = item.find('div',{'class':'a-size-small a-link-child'}).text
  print(data_dict['Title'])
  print(data_dict['Writer'])