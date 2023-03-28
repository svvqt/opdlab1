from bs4 import BeautifulSoup
import requests
import transliterate 
def parser():
    url = 'https://auto.drom.ru/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    rus="А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я" # Русский алфавит, нужен для транслита
    price=[] # цена со странички
    pricefiltered=[] # отфильтрованная цена
    newcars=[] # Данные машин со странички
    newcarsfiltered=[] # отфильтрованные данные машин
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    newcars = soup.findAll('div',class_='css-13ocj84 e1icyw250') # записываем нужный класс
    price=soup.findAll('span',class_='css-46itwz e162wx9x0') # записываем нужный класс
    for data in newcars: # проходим циклом по содержимому контейнера
        if data.find('span') is not None: # находим тег "span"
            newcarsfiltered.append(data.text) # записываем в переменную содержание тега
    for data in price:
        if data.find('span') is not None:
            pricefiltered.append(data.text)
    for i in range(20):
        a=newcarsfiltered[i] # записываем в переменную данные
        bukva=str(a.split(",")[0]) # первая буква
        for j in range(33):
            if (rus.split(" ")[j] == bukva[0]): # если буква в русском алфавите == первой букве в названии
                newcarsfiltered[i]=transliterate.translit(a, reversed=True) # с помощью библиотеки русское название переводится на латиницу
        print(newcarsfiltered[i].split(",")[0]+', '+pricefiltered[i]) # выводим название+цену
    with open("spisok.txt", "w",encoding="utf-8") as file:
        for i in range(20):
            file.write(newcarsfiltered[i].split(",")[0]+', '+pricefiltered[i]) # записываем в файл название+цену
            file.write('\n')
