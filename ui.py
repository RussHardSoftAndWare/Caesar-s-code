char = []
quit = True
while quit == True:
    inputChar = input("Символ: ")
    if inputChar == "q":
        quit = False
    char.append(inputChar)
print(char)
