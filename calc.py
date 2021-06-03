#импорт tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#окно калькулятора
root = Tk()
root.title('калькулятор')

#переменная
var = 1

def calc (key, a):
    global memory
    if key == '=':
        str1 = '-+0123456789.*/var'
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, 'ERROR: первый символ не чило!')
            messagebox.showerror('ERROR!', 'введен неверный знак!')

        if a == 'var+=1':
            global var
            var += 1
            calc_entry.delete(0, END)
            return 0
        if a == 'var=10':
            var = 10
            calc_entry.delete(0, END)
            return 0
        if a == 'var=50':
            var = 50
            calc_entry.delete(0, END)
            return 0
        if a == 'var+=10':
            var += 10
            calc_entry.delete(0, END)
            return 0
        if a == 'var+=50':
            var += 50
            calc_entry.delete(0, END)
            return 0

        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except:
            calc_entry.insert(END, 'ERROR!')
            messagebox.showerror('ERROR!', 'Введены нечеткие данные')


    elif key == 'C':
        calc_entry.delete(0, END)

    elif key == '-/+':
        if '=' in calc_entry.get():
            calc_entry.delete(0,END)

        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    elif key == 'help':
        roothelp = Tk()
        roothelp.title('help')

        Label(roothelp, text = 'var+=1 - прибавить к переменной 1\nvar=10 - присвоить переменной 10\nvar+=50 - прибавить к переменной 50\nvar=50 - присвоить переменной 50\nvar - узнать значение переменной').pack()

        roothelp.mainloop()
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


buttonlist = [
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '-/+', '=',
    '0', '.', 'C', '**', '(',
    ')', '//', '%', 'help','var'
]

r = 1
c = 0
calc_entry = Entry(root, width = 33)
for i in buttonlist:
    rel = ''
    cmd = lambda x = i: calc(x, calc_entry.get())
    ttk.Button(root, text = i , command = cmd).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1


calc_entry.grid(row = 0, column = 0, columnspan = 5)


root.mainloop()
