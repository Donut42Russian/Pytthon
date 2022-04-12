class BigBell:
    f = 0

    def sound(self):
        if not self.f:
            print('ding')
            self.f = 1
        else:
            print('dong')
            self.f = 0


class Balance:
    def __init__(self):
        self.__right = 0
        self.__left = 0

    def add_right(self, number):
        self.__right += number

    def add_left(self, number):
        self.__left += number

    def result(self):
        if self.__right == self.__left:
            print("=")
        elif self.__right < self.__left:
            print("L")
        elif self.__right > self.__left:
            print("R")


class Selector:
    def __init__(self, massive):
        self.mass = massive

    def get_odd(self):
        for i in self.mass:
            if i % 2 == 1:
                print(i, end=" ")
        print("")

    def get_evens(self):
        for i in self.mass:
            if i % 2 == 0:
                print(i, end=" ")
        print("")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class ReversedList:
    def __init__(self, ls):
        self.a = list(reversed(ls))

    def __getitem__(self, k):
        return self.a[k]

    def __len__(self):
        return len(self.a)


class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, idx, value):
        self.data[idx] = value

    def __getitem__(self, idx):
        return self.data.get(idx, 0)


class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        y = 0
        for i in range(len(self.coefficients)):
            y += pow(x, i) * self.coefficients[i]
        return y

    def __add__(self, other):
        arr = []
        res = Polynomial(arr)
        if len(self.coefficients) < len(other.coefficients):
            for i in range(len(self.coefficients)):
                arr.append(self.coefficients[i] + other.coefficients[i])
            arr += other.coefficients[len(self.coefficients)::]
        else:
            for i in range(len(other.coefficients)):
                arr.append(self.coefficients[i] + other.coefficients[i])
            arr += self.coefficients[len(other.coefficients)::]
        res.coefficients = arr
        return res


class Queue:
    def __init__(self, *values):
        self.arr = list(values)

    def __str__(self):
        if self.arr:
            self.arr = list(map(str, self.arr))
            arr = ' -> '.join(self.arr)
            return f'[{arr}]'
        return '[]'

    def __add__(self, other):
        c = self.copy()
        c.extend(other)
        return c

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.arr == other.arr

    def __rshift__(self, n):
        if n > len(self.arr):
            return Queue()
        else:
            c = self.copy()
            for i in range(n):
                c.pop()
        return c

    def __next__(self):
        return self.next()

    def copy(self):
        return Queue(*self.arr)

    def next(self):
        self_copy = self.copy()
        self_copy.pop()
        return self_copy

    def append(self, *values):
        for i in list(values):
            self.arr.append(i)

    def pop(self):
        return self.arr.pop(0)

    def extend(self, other):
        for i in other.arr:
            self.append(i)


###
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)


####
class Summator:

    def transform(self, n):
        return n

    def sum(self, n):
        count = 0
        for i in range(n + 1):
            count += self.transform(int(i))
        return count


class SquareSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 3


class PowerSummator(Summator):

    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b

# Переписанные Сумматоры
"""
class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)
"""
# Проверочные примеры
"""
bell = BigBell()
bell.sound()
bell.sound()
bell.sound()

balance = Balance()
balance.add_right(10)
balance.result()
balance.add_left(30)
balance.result()
balance.add_right(20)
balance.result()

selector = Selector([1, 2, 3, 4, 5, 6, 7, 8, 9])
selector.get_evens()
selector.get_odd()

p1 = Point(1, 2)
p2 = Point(5, 6)
if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

rl = ReversedList([10, 20, 30])
print([rl[i] for i in range(len(rl))])

arr = SparseArray()
arr[1] = 10
arr[8] = 20
print([arr[i] for i in range(10)])

poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
q0 = Queue("x", "t", "y")
print(q0)

triangle = EquilateralTriangle(10)
print(triangle.perimeter())

n = 5
summator = CubeSummator()
print(summator.sum(n))
print(pow(n * (n + 1) / 2, 2))

n = 5
summator = PowerSummator(3)
print(summator.sum(n))
print(pow(n * (n + 1) / 2, 2))
"""
