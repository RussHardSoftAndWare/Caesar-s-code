u_input = int(input("Введите число смещения: "))
let_input = input("Введите слово: ")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
"v", "w", "x", "y", "z",]
word = []
word_after = ""
for z in let_input:
    word.append(z)
for z in word:
    if z == " ":
        word_after = word_after + " "
    else:
        x = letters.index(z) - u_input
        word_after = word_after + letters[x]
print(word_after)
