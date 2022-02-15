import numexpr as ne
import math

def first():
    movie = input()
    cinema = input()
    time = input()

    print(f"Билет на \"{movie}\" в \"{cinema}\" на {time} забронирован.")

def second():
    a = input()
    b = input()
    if a == b:
        if a == "да" or a == "нет":
            print("ВЕРНО")
        else:
            print("НЕВЕРНО")
    else:
        print("НЕВЕРНО")

def third():
    login = input()
    email = input()

    if "@" not in login and "@" in email:
        print("Верно")
    else:
        print("Неверно")

def fourth():
    print(input())

def fifth():
    a = input()
    print("Да" if not bool(a) else "Нет")

def sixth():
    a = input()
    max_num = 0
    min_num = 10
    i_max, i_min = 0, 0

    arr = list(map(int, a))

    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            i_max = i
        if arr[i] < min_num:
            min_num = arr[i]
            i_min = i

    arr.pop(i_max)
    arr.pop(i_min)

    if (min_num + max_num)/2 == arr[0]:
        print("Вы ввели красивое число")
    else:
        print("Жаль, вы ввели обычное число")

def seven():
    def calc(first_num, second_num, third_num, last_num, mult):
        res = 0
        if first_num <= second_num and first_num <= third_num and first_num <= last_num:
            res = first_num * mult
            first_num = 99
        elif second_num != 10 and second_num <= first_num and second_num <= third_num and second_num <= last_num:
            res = second_num * mult
            second_num = 99
        elif third_num != 10 and third_num <= first_num and third_num <= second_num and third_num <= last_num:
            res = third_num * mult
            third_num = 99
        elif last_num != 10 and last_num <= first_num and last_num <= second_num and last_num <= third_num:
            res = last_num * mult
            last_num = 99

        return res, first_num, second_num, third_num, last_num

    num = int(input("введите четырехзначное число: "))
    first_num = num // 1000
    second_num = (num // 100) % 10
    third_num = (num // 10) % 10
    last_num = num % 10

    first_num = first_num if first_num != 0 else 10
    second_num = second_num if second_num != 0 else 10
    third_num = third_num if third_num != 0 else 10
    last_num = last_num if last_num != 0 else 10

    number = 0
    print("введенное число: " + str(num))

    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 1000)
    number += res

    first_num = 0 if first_num == 10 else first_num
    second_num = 0 if second_num == 10 else second_num
    third_num = 0 if third_num == 10 else third_num
    last_num = 0 if last_num == 10 else last_num

    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 100)
    number += res
    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 10)
    number += res
    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 1)
    number += res

    print(number)

def eight():
    max = 0
    min = 999
    count = 0
    while True:
        l = input("введите рост космонавта: ")
        if l == "!":
            break

        l = int(l)
        count = count + 1 if l < 190 and l > 150 else count
        max = l if (l > max and l < 190 and l > 150) else max
        min = l if (l < min and l < 190 and l > 150) else min

    print(f"подходит: {count} претендента(ов), максимальный рост: {max}, минимальный {min}")

def nine():
    while True:
        first_pass = input("введите пароль: ")
        second_pass = input("введите пароль повторно: ")
        if len(first_pass) < 8:
            print("Короткий!")
        elif first_pass.find("123") != -1:
            print("Простой!")
        elif first_pass != second_pass:
            print("Различаются!")
        else:
            print("OK")
            break

def ten():
    operation = ""
    while operation != "x":
        x1 = int(input())
        operation = input()

        if operation == "+":
            print(int(x1) + int(input()))
        elif operation == "*":
            print(int(x1) * int(input()))
        elif operation == "-":
            print(int(x1) - int(input()))
        elif operation == "/":
            x2 = int(input())
            if x2 != 0:
                print(int(x1) / x2)
            else:
                print("Error")
            del x2
        elif operation == "%":
            x2 = int(input())
            if x2 != 0:
                print(int(x1) % x2)
            else:
                print("Error")
            del x2
        elif operation == "!":
            print(math.factorial(int(x1)))
        elif operation == "x":
            print(x1)

def eleven():
    l = int(input("введите высоту пирамиды: "))
    for i in range(1, l + 1):
        l -= 1
        print(l * " " + (i * 2 - 1) * "*" + l * " ")

def twenteen():
    l = int(input("введите число: "))
    run = True
    num = 0
    last_count = 0
    while run:
        for _ in range(last_count + 1):
            num += 1
            print(f"{num} ", end="")
            if num >= l:
                run = False
                break

        last_count += 1
        print()

def thirteen():
    size = input("введите стороны прямоугольника через пробел\n")
    symbol = input("введите символ для рисования: ")
    size = size.split(" ")
    x, y = int(size[0]), int(size[1])

    for i in range(y):
        if i == 0 or i == y - 1:
            print(symbol * x)
            continue

        print(symbol + " " * (x - 2) + symbol)

first()
second()
third()
fourth()
fifth()
sixth()
seven()
eight()
nine()
ten()
eleven()
twenteen()
thirteen()