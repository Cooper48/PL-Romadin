#Запуск другого скрипта
from tkinter import * #Импорт модуля tkinter
import subprocess
import os
import datetime
import time
class button_test:
    def __init__(self):
        self.but = Button(root,
                          text = "вызов скрипта буттон_тест")#Кнопка
        self.but.bind("<Button-1>",self.button_test)#Связать
        self.but.grid(row = 0,
                            column = 0,
                            padx = 30,
                            pady = 10)#Расположить
    def button_test(self,event):
        subprocess.run('python button_test.py'.split())#Запустить субпроцесс кнопка

root = Tk() #Создание главного окна надпись tk
obj = button_test()#Что-то связанное с объектом
root.mainloop() #отобразить окно, данная строчка кода должна быть всегда в конце скрипта
#Конец