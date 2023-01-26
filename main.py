#Самсонова Юлия Евгеньевна 20-ИЭ-2
#Вариант 16
#Имитация ежедневника мобильного телефона.
#По названию месяца формируется матрица с датами.
#Есть возможность записать «Напоминание» и по
#наведению мыши прочитать его.  

import calendar
from tkinter import *
from tkinter import ttk
from idlelib.tooltip import Hovertip

root = Tk()
root.geometry('165x350')

def Autor(): #Информация об авторе
    about = Tk()
    label = Label(about, text='Самсонова Юлия Евгеньевна 20-ИЭ-2\nВариант 16\nИмитация ежедневника мобильного телефона.\nПо названию месяца формируется матрица с датами.\nЕсть возможность записать «Напоминание» \nи понаведению мыши прочитать его.')
    label.grid()
    
mainmenu = Menu(root) #Главное меню
root.config(menu=mainmenu)
mainmenu.add_command(label='Об авторе',command=Autor)

def Close(event): #Закрыть главное окно
    root.destroy()

def Get(event): #Вывод календаря
    global frameCalendar, year, month, button_text
    year = int(comboYear.get()) #Получить значение года
    if comboMonth.get() == 'январь': #Получить значение месяца
        month = 1
    elif comboMonth.get() == 'февраль':
        month = 2
    elif comboMonth.get() == 'март':
        month = 3
    elif comboMonth.get() == 'апрель':
        month = 4
    elif comboMonth.get() == 'май':
        month = 5
    elif comboMonth.get() == 'июнь':
        month = 6
    elif comboMonth.get() == 'июль':
        month = 7
    elif comboMonth.get() == 'август':
        month = 8
    elif comboMonth.get() == 'сентябрь':
        month = 9
    elif comboMonth.get() == 'октябрь':
        month = 10
    elif comboMonth.get() == 'ноябрь':
        month = 11
    else:
        month = 12

    frameCalendar.destroy() #Frame для календаря
    frameCalendar = Frame(root, height=180, width=165)
    frameCalendar.grid(row=8, columnspan=7)
    frameCalendar.grid_propagate(0) #Frame не изменятется под размеры виджетов в нем

    days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС'] #Вывод строки с днями недели
    for i in range(7):
        label = Label(frameCalendar, text=days[i])
        label.grid(row=6, column=i)

    weekday, numDays = calendar.monthrange(year, month) #Метод monthrange для подсчета дней и недель в месяце
    week = 1
    for i in range(1, numDays + 1): #Вывод календаря
        button = Button(frameCalendar, text=str(i), command=lambda day=i: Note(day))
        button.grid(row=week+6, column=weekday)
        datas = str(year)+"-"+str(month)+"-"+str(i)
        memos = open('data.txt', 'r')
        for line in memos: #Просмотр каждой строки в файле
            if datas == line.strip(): #Проверка совпадения по дате
                Hovertip(button, next(memos), hover_delay=100) #Всплывающая подсказка

        weekday += 1
        if weekday > 6:
            week += 1
            weekday = 0

def Note(day): #Создание второго окна
    global entryNote, data
    data = str(year)+"-"+str(month)+"-"+str(day)
    notes = Toplevel(root)
    notes.title(str(day)+"-"+str(month)+"-"+str(year))
    labelNote = Label(notes, text='Введите напоминание')
    labelNote.grid(row=0)
    entryNote = Entry(notes, width=35) #Поле для ввода напоминания
    entryNote.grid(row=1)
    buttonNote = Button(notes, text='Сохранить', command=Save) #Кнопка для сохранения напоминания
    buttonNote.grid()

    def Close2(): #Закрытие дополнительного окна
        notes.destroy()

    buttonClose = Button(notes, text='Закрыть', command=Close2) #Кнопка для закрытия второго окна
    buttonClose.bind('<Button-1>', Get) #Обновление календаря после сохранения напоминания
    buttonClose.grid()

    
def Save(): #Сохранение напоминания в файле
    
    with open('data.txt', 'a') as f:
        print(data, file=f)
        print(entryNote.get(), file=f)

labelMonth = Label(root, text='Выберите месяц')
labelMonth.grid(row=0, columnspan=7)
comboMonth = ttk.Combobox(root, state='readonly', values=['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
          'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']) #Выбор месяца
comboMonth.current(0)
comboMonth.grid(row=1, columnspan=7)
labelYear = Label(root, text='Выберите год')
labelYear.grid(row=2, columnspan=7)
comboYear = ttk.Combobox(root, state='readonly', values=['2022', '2023', '2024', '2025']) #Выбор года
comboYear.current(0)
comboYear.grid(row=3, columnspan=7)

frameCalendar = Frame(root, height=180, width=165) #Frame для календаря
frameCalendar.grid(row=8, columnspan=7)
frameCalendar.grid_propagate(0)

btn_get = Button(root, text='Вывести календарь')
btn_close = Button(root, text='Закрыть')

lbl = Label(root)
lbl.grid(row=5)

btn_get.grid(row=4, columnspan=7)
btn_get.bind('<Button-1>', Get)

btn_close.grid(row=25, columnspan=7)
btn_close.bind('<Button-1>', Close)

root.mainloop()
