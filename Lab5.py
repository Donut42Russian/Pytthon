import math


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('Это треугольник')
    else:
        print('Это не треугольник')


def distance(x1, y1, x2, y2):
    print(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def number_to_words(n):
    e = {1: 'один', 2: 'два', 3: 'три',
         4: 'четыре', 5: 'пять', 6: 'шесть',
         7: 'семь', 8: 'восемь', 9: 'девять'}
    d = {10: 'десять', 20: 'двадцать', 30: 'тридцать',
         40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
         70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
    ch = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
          14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
          17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    n1 = n % 10
    n2 = n - n1
    if n < 10:
        print(e.get(n))
    elif 10 < n < 20:
        print(ch.get(n))
    elif n >= 10 and n in d:
        print(d.get(n))
    else:
        print(d.get(n2) + ' ' + e.get(n1))


def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        print(res)
    else:
        print(1 / res)


def palindrome(string):
    reversed_string = ""
    s = string.replace(" ", "")
    s = s.lower()
    reversed_string = s[::-1]
    if s == reversed_string:
        print("Палиндром")
    else:
        print("Не палиндром")


def print_without_duplicates(current_message):
    global last_message
    if current_message != last_message:
        print(current_message)
    last_message = current_message


# def add_friends(name_of_person, list_of_friends):
# def are_friends(name_of_person1, name_of_person2):
# def print_friends(name_of_person):


def mirror(arr):
    arr += arr[::-1]


def from_string_to_list(string, container):
    container.extend(map(int, string.split()))


def transpose(matrix):
    res = []
    for j in range(len(matrix[0])):
        t = []
        for i in range(len(matrix)):
            t = t + [matrix[i][j]]
        res = res + [t]
    return res


def partial_sums(*args):
    sum = 0
    array = [0]
    for i in range(len(args)):
        sum += args[i]
        array.append(sum)
    return array


def power_13(a, n):
    if n == 1:
        return a
    else:
        return a * power_13(a, n - 1)


def recursive_len(some_list):
    if not some_list:
        return 0
    return 1 + recursive_len(some_list[:-1])


# 1
triangle(1, 1, 2)
# 2
distance(0, 0, 1, 1)
# 3
number_to_words(64)
# 4
power(2, -3)
# 5
palindrome("А роза упала на лапу Азора")
# 6
last_message = ""
print_without_duplicates("message")
print_without_duplicates("message")
print_without_duplicates("mssge")
# 7

# 8
arr = [1, 2, 3, 4, 7]
mirror(arr)
print(*arr)
# 9
a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)
# 10
matrix = [[1, 2, 15], [3, 4, 8]]
matrix = transpose(matrix)
for line in matrix:
    print(*line)
# 11

# 12
print(partial_sums(1, 0.5, 0.25, 0.125))
# 13
print(power_13(2, 5))
# 14
print(recursive_len([1, 2, 3, 4, 45]))
# 15