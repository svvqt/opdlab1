from bs4 import BeautifulSoup
import requests
import transliterate
def parser():
    url = 'https://auto.drom.ru/'
    page = requests.get(url)
    print(page.status_code)
    rus="А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я"
    price=[]
    pricefiltered=[]
    newcars=[]
    newcarsfiltered=[]
    soup = BeautifulSoup(page.text, "html.parser")
    newcars = soup.findAll('div',class_='css-17lk78h e3f4v4l2')
    price=soup.findAll('span',class_='css-46itwz e162wx9x0')
    for data in newcars:
        if data.find('span') is not None:
            newcarsfiltered.append(data.text)
    for data in price:
        if data.find('span') is not None:
            pricefiltered.append(data.text)
    for i in range(20):
        a=newcarsfiltered[i]
        b=str(a.split()[0])
        bukva=b.split()[0]
        for j in range(33):
            if (rus.split(" ")[j] == bukva[0]):
                a=str(newcarsfiltered[i])
                newcarsfiltered[i]=transliterate.translit(a, reversed=True)
        print(newcarsfiltered[i]+', '+pricefiltered[i])
    with open("spisok.txt", "w",encoding="utf-8") as file:
        for i in range(20):
            file.write(newcarsfiltered[i]+', '+pricefiltered[i])
            file.write('\n')
