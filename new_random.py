import tkinter
import random


root = tkinter.Tk()
root.title("Проект 365")
root.geometry("250x250")

# Приветственный текст
text = "Нажми на кнопку чтобы\n выбрать случайную тему :)"
label1 = tkinter.Label(text=text, justify=tkinter.CENTER)
label1.place(relx=0.1, rely=.1)

# производим выбор случайного объекта из файла
items = []
with open("item.txt") as file:
    for line in file:
        items.append(line.split(',')[0])


def create_widgets():
    random.shuffle(items)
    random_choice = random.choice(items)
    label1.configure(text=random_choice, justify=tkinter.CENTER)


# кнопка
button = tkinter.Button(root)
button.configure(text="Выбрать тему",  command=create_widgets)
button.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=tkinter.OUTSIDE)

root.mainloop()