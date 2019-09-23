u_input = int(input("Введите число смещения: "))
let_input = input("Введите слово: ")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
"v", "w", "x", "y", "z"]
lettersru = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
"у", "ф", "х", "ц", "ч","ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
word = []
word_after = ""
for z in let_input:
    word.append(z)
for z in word:
    if z == " ":
        word_after = word_after + " "
    else:
        if z in letters:
            x = letters.index(z) - u_input
            word_after = word_after + letters[x]
        elif z in lettersru:
            x = lettersru.index(z) - u_input
            word_after = word_after + lettersru[x]
print(word_after)
