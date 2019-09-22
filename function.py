from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Шифр Цезаря 2.0")
root.geometry("300x400")

u_input = 0
let_input = ""

##u_input = int(input("Введите число смещения: "))
##let_input = input("Введите слово: ")
def cypher():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z",]
    word = []
    word_after = ""
    for z in let_entry.get().lower():
        word.append(z)
    for z in word:
        if z == " ":
            word_after = word_after + " "
        else:
            x = letters.index(z) - int(u_entry.get())
            word_after = word_after + letters[x]
    messagebox.showinfo("Вы зашифровали жопу", word_after)
##print(word_after)

u_entry = Entry(root)
u_entry.place(relx=.5, rely=.1, anchor="c")
let_entry = Entry(root)
let_entry.place(relx=.5, rely=.2, anchor="c")
ready_button = Button(text="Прошу шифр", command=cypher)
ready_button.place(relx=.5, rely=.9, anchor="c")

root.mainloop()
