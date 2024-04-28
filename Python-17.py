# 1. Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции: {end_time - start_time} секунд")
        return result
    return wrapper

@timer
def find_primes():
    primes = []
    for num in range(2, 1001):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes



print(find_primes())

# 2. Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

@calculate_time
def find_primes(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

primes_list = find_primes(0, 1000)
print(primes_list)

# 3. Реализуйте декоратор для обработки исключений,
# возникающих внутри функции, и вывода
# соответствующего сообщения об ошибке.

# Вариант - 1

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

divide(10, 2)
divide(10, 0)
divide('a', 2)

# Вариант -2.

import sys
from functools import wraps


def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в функции {func.__name__}: {e}")
            sys.exit(1)

    return wrapper


@exception_handler
def my_function():
    raise ValueError("Неверный аргумент")


my_function()

# 4. Создайте декоратор, который применяется к классу и
# изменяет его поведение или добавляет новые методы.

def add_method(method):
    def decorator(cls):
        setattr(cls, method.__name__, method)
        return cls

    return decorator

@add_method
def new_method(self):
    return "This is a new method added to the class"


@new_method
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


obj = MyClass("Alice")
print(obj.greet())
print(obj.new_method())