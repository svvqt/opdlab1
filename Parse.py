from bs4 import BeautifulSoup
import requests
import transliterate
def parser():
    url = 'https://auto.drom.ru/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    rus="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # Русский алфавит, нужен для транслита
    price=[] # цена со странички
    pricefiltered=[] # отфильтрованная цена
    newcars=[] # Данные машин со странички
    newcarsfiltered=[] # отфильтрованные данные машин
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    newcars = soup.findAll('a',class_='css-xb5nz8 e1huvdhj1') # записываем нужный класс
    price=soup.findAll('span',class_='css-46itwz e162wx9x0') # записываем нужный класс
    for i in range(20): # проходим циклом по содержимому контейнера
        if newcars[i].find('span') is not None: # находим тег "span"
            newcarsfiltered.append(newcars[i].text) # записываем в переменную содержание тега
        pricefiltered.append(price[i].text)
        a=newcarsfiltered[i] # записываем в переменную данные
        bukva=str(a.split(",")[0]) # первая буква
        for j in range(len(rus)):
            if (rus[j] == bukva[0]): # если буква в русском алфавите == первой букве в названии
                newcarsfiltered[i]=transliterate.translit(a, reversed=True) # с помощью библиотеки русское название переводится на латиницу
        print(newcarsfiltered[i].split(",")[0]+', '+pricefiltered[i]) # выводим название+цену
    return(newcarsfiltered,pricefiltered)

def writinginfile(newcarsfiltered,pricefiltered):
    with open("spisok.txt", "w",encoding="utf-8") as file:
        for i in range(20):
            file.write(newcarsfiltered[i].split(",")[0]+', '+pricefiltered[i]) # записываем в файл название+цену
            file.write('\n')
