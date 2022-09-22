from bs4 import BeautifulSoup
import requests
from csv import writer

i = 0
counter = 2
url = "https://www.pararius.com/apartments/amsterdam"
isHeader = True
if counter < 20:
  for i in range(18):
    page = requests.get(url)
    url = "https://www.pararius.com/apartments/amsterdam/page-"+str(counter)
    counter += 1
    soup = BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('section',class_='listing-search-item')

    with open('housing.csv', 'a', encoding='utf8', newline='') as f:
      thewriter = writer(f)
      if isHeader == True:
        header = ['Title','Location','Price','Area','Number of Rooms','Interior']
        thewriter.writerow(header)
        isHeader = False
      for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n','')
        location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n','')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n','')
        area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text
        number_of_rooms = list.find('li', class_="illustrated-features__item illustrated-features__item--number-of-rooms").text
        try:
          interior = list.find('li', class_="illustrated-features__item illustrated-features__item--interior").text
        except:
          continue

        info = [title,location,price,area,number_of_rooms,interior]
        thewriter.writerow(info)




