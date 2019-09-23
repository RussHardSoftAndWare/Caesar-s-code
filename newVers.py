from tkinter import *
from tkinter import messagebox
import webbrowser

root = Tk()
root.title("Шифр Цезаря 3.0")

def YVK():
    webbrowser.open('https://vk.com/yakidze', new=2)

def DVK():
    webbrowser.open('https://vk.com/uknowall_o', new=2)

def about_programm():
    help2 = Tk()
    help2.title("О программе")
    Label(help2, text="Программа для расшифровки/зашифровки создана\nот нехер делать, но это не делает ее плохой и т.д.").grid(row=0, column=0, pady=5, padx=5, columnspan=2)
    Button(help2, text="ВК Якова", command=YVK).grid(row=1, column=0, pady=5, padx=5)
    Button(help2, text="ВК Даниила", command=DVK).grid(row=1, column=1, pady=5, padx=5)

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="В разработке")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе", command = about_programm)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

def cypher():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z",]
    lettersru = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
    "у", "ф", "х", "ц", "ч","ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    word = []
    word_after = ""
    readyText = textToW.get().lower()
    readyNumber = int(numberToW.get())
    for z in readyText:
        word.append(z)
    for z in word:
        if z == " ":
            word_after = word_after + " "
        else:
            if z in letters:
                x = letters.index(z) - readyNumber
                word_after = word_after + letters[x]
            elif z in lettersru:
                y = lettersru.index(z) - readyNumber
                word_after = word_after + lettersru[y]
    ##messagebox.showinfo("Вы зашифровали жопу", word_after)
    textFR.delete('1.0', END)
    textFR.insert(1.0, word_after)

def decypher():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z",]
    lettersru = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
    "у", "ф", "х", "ц", "ч","ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    word = []
    word_after = ""
    readyText = textToW.get().lower()
    readyNumber = int(numberToW.get())
    for z in readyText:
        word.append(z)
    for z in word:
        if z == " ":
            word_after = word_after + " "
        else:
            if z in letters:
                x = letters.index(z) + readyNumber
                if (x >= 26):
                    x = x - 26
                    word_after = word_after + letters[x]
                else:
                    word_after = word_after + letters[x]
            elif z in lettersru:
                y = lettersru.index(z) + readyNumber
                if (y >= 33):
                    y = y - 33
                    word_after = word_after + lettersru[y]
                else:
                    word_after = word_after + lettersru[y]
    ##messagebox.showinfo("Вы отшифровали жопу", word_after)
    textFR.delete('1.0', END)
    textFR.insert(1.0, word_after)

Label(text="Текст:").grid(row=0, column=0, sticky=W, pady=5, padx=5)
textToW = Entry()
textToW.grid(row=0, column=1, sticky=W+E, padx=5, columnspan=2)
Label(text="Смещение:").grid(row=1, column=0, sticky=W, pady=5, padx=5)
numberToW = Entry()
numberToW.grid(row=1, column=1, sticky=W+E, padx=5, columnspan=2)
Button(text="Зашифровать", command=cypher).grid(row=2, column=0, sticky=S+W, pady=5, padx=5)
Button(text="Расшифровать", command=decypher).grid(row=2, column=2, sticky=E+S, pady=5, padx=5)
result = Label(text="Результат:").grid(row=3, column=0, sticky=W, pady=5, padx=5)
textFR=Text(height=7, font='Arial 12',wrap=WORD)
textFR.grid(row=4, column=0, sticky=W, pady=5, padx=5, columnspan=3)

root.mainloop()
