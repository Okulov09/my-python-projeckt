#импортируем библиотеки
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

#создаём окно
root = Tk()
root.title('погода')
root.geometry('400x200')
root['bg'] = 'lightblue'

#текста
Label(root, text = 'Прогноз погоды', font = 'Consolas 15 bold').pack(pady = 5)
Label(root, text = 'Введите город:', font = 'Consolas 11 bold').pack(pady = 5)

#поле ввода
city = Entry(root, width = 40)
city.pack()

#функция для погоды
def temp():
	a = str(city.get())
	search = f'Пагода в {a}'

	#url
	url = f'https://www.google.com/search?&q={search}'

	#подключаемся к сайту
	r = requests.get(url)
	s = BeautifulSoup(r.text, 'html.parser')

	#берём инфу
	update = s.find('div', class_ = 'BNeawe').text

	#создаём окно
	messagebox.showinfo('Погода', 'в городе ' + a + ' температура ' + update)

	#отчищаем
	city.delete(0, END)

#кнопка
Button(root, text = 'узнать погоду', command = temp).pack()

root.mainloop()