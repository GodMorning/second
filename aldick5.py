number=int(input('Введите число от 1 до 9:'))
if number <=3:
    s=input('Строка ввода: ')
    n=int(input('Строка повторов: '))
    for element in range(n):
        print(s)
elif number>=4 and number <=6:
    m=int(input('Степень числа: '))
    print(number**m)
elif number>=7 and number<=9:
    for num in range(10):
        print(number+num)
        num=num+1
else:
    print('Ошибка ввода')
