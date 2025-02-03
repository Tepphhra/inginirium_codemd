import tkinter as tk #подключаем библиотеку ткинтер, обращаемся к ней как tk

def movit(event): #создаем функцию, которая будет проверять какую конкретно клавишу нажали
    if event.keysym == 'Up': #если нажата стрелка вверх
        canvas.move(oval, 0, -20) #перемещаем объект оval на 0 по гооризонтали и на -20 (вверх на 20) по вертикали
    elif event.keysym == 'Down': #это и ниже - аналогично первой проверке
        canvas.move(oval, 0, 20)
    elif event.keysym == 'Left':
        canvas.move(oval, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 20, 0)

win = tk.Tk() #создаем окно, называем win
canvas = tk.Canvas(win, bg='#fa70e3', width=400, height=600) #создаем холст, определяем его в окно win, задаем цвет и размеры | csscolor.ru

oval = canvas.create_oval((150, 150), (250, 250), fill='#ffffff') #создаем объект - круг, передаем ему координаты верхней левой и нижней правой точек, выбираем цвет

canvas.pack() #обрабатываем холлст
win.bind("<KeyPress>", movit) #прикрепляем события типа нажатия клавиши к функции movit
win.mainloop() #запускаем окно
