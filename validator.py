### Validator
char_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*']    #лист с особыми символами
ulet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #лист с большими буквами
pwd = []                                                     #парольчик
ver1 = False
ver2 = False
def u_input():                                               #пароль юзера
    u_input = input("Введите пароль: ")
    for x in u_input:
        pwd.append(x)
def checker(ver1, ver2):
    if (len(pwd) >=5) and (len(pwd) <=10):
        for z in range(0, len(pwd)):
            if pwd[z] in char_list:
                ver1 = True
            if pwd[z] in ulet_list:
                ver2 = True
        if (ver1 == True) and (ver2 == True):
            print("ПАРОЛЬ ПРОСТА ИДЕАЛЕН,МУА")
        else:
            print("Пароль не подходит из-за отсутствия спец. символов")
    else:
        print("Пароль не подходит по кол-ву символов")
u_input()
checker(ver1, ver2)
