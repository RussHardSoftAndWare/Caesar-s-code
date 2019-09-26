u_inp1 = int(input("Введите первое число: "))
u_inp2 = int(input("Введите второе число: "))
u_inp3 = int(input("Введите число чисел: "))
list = []
list.append(u_inp1)
list.append(u_inp2)
for x in range(2, u_inp3):
    newnum = list[x-2] + list[x-1]
    list.append(newnum)
print(list)
