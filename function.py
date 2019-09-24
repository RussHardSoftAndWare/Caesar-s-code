from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Шифр Цезаря 2.0")
root.geometry("300x400")

u_input = 0
let_input = ""

def cypher():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z",]
    lettersru = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
    "у", "ф", "х", "ц", "ч","ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    word = []
    word_after = ""
    for z in let_entry.get().lower():
        word.append(z)
    for z in word:
        if z == " ":
            word_after = word_after + " "
        else:
            if z in letters:
                x = letters.index(z) - u_input
                word_after = word_after + letters[x]
            elif z in lettersru:
                y = lettersru.index(z) - u_input
                word_after = word_after + lettersru[y]
    messagebox.showinfo("Вы зашифровали жопу", word_after)

u_entry = Entry(root)
u_entry.place(relx=.5, rely=.1, anchor="c")
let_entry = Entry(root)
let_entry.place(relx=.5, rely=.2, anchor="c")
ready_button = Button(text="Прошу шифр", command=cypher)
ready_button.place(relx=.5, rely=.9, anchor="c")

root.mainloop()
