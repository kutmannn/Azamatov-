num_1=int(input("первое число: "))
do=input('выбери действие(+,-,*,/): ')
num_2=int(input("вторая цифра: "))

if do == '+':
    print(num_1 + num_2)
elif do == "-" :
    print(num_1 - num_2)
elif do == "*" :
    print(num_1 * num_2)
elif do == "/" :
    print(num_1 / num_2)

