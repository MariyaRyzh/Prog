from tkinter import*
root = Tk()
shapes = ['rectangle', 'oval', 'polygon']


def next_figure():
    if shapes[0]:
        canvas.create_rectangle(80, 80, 150, 150)
    elif shapes[1]:
        canvas.create_oval(80, 80, 150, 150)
    elif shapes[2]:
        canvas.create_polygon(80, 80, 150, 80, 60, 20)

        
canvas = Canvas(root, width=200, height=200)
canvas.pack()
root.title('Случайные фигуры')
root.geometry('500x500')
root.resizable(False, False)
butt = Button(root, text='Нажми', width=8, height=3, command=next_figure)
butt.pack()
root.mainloop()
