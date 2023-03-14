from bs4 import BeautifulSoup
import requests
url = 'https://auto.drom.ru/'
page = requests.get(url)
print(page.status_code)
newcars=[]
newcarsfiltered=[]
soup = BeautifulSoup(page.text, "html.parser")
newcars = soup.findAll('div',class_='css-17lk78h e3f4v4l2')
for data in newcars:
    if data.find('span') is not None:
        newcarsfiltered.append(data.text)
for data in newcarsfiltered:
    print(data.split(',')[0])
with open("spisok.txt", "w") as file:
    for data in newcarsfiltered:
        file.write(data.split(',')[0])
        file.write('\n')
