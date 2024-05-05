# 1. Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения)
# В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.

numbers = []

def add_number():
    num = int(input("Введите число: "))
    if num in numbers:
        print("Это число уже есть в списке")
    else:
        numbers.append(num)
        print("Число успешно добавлен")

def remove_number():
    num = int(input("Введите число для удаления: "))
    numbers[:] = [x for x in numbers if x != num]
    print("Все вхождения числа удалены")


def show_list():
    direction = input("Введите направление (начало/конец): ")
    if direction == "начало":
        print(numbers)
    elif direction == "конец":
        print(numbers[::-1])


def check_value():
    num = int(input("Введите число для проверки: "))
    if num in numbers:
        print("Значение есть в списке")
    else:
        print("Значение отсутствует в списке")


def replace_value():
    num = int(input("Введите число для замены: "))
    replace_num = int(input("Введите новое число: "))
    replace_all = input("Заменить все совпадения? (да/нет): ")
    if replace_all == "да":
        global numbers
    else:
        index = numbers.index(num)
        numbers[index] = replace_num
    print("Значение успешно заменено")


while True:
    print("Меню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_number()
    elif choice == "2":
        remove_number()
    elif choice == "3":
        show_list()
    elif choice == "4":
        check_value()
    elif choice == "5":
        replace_value()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

# 2. Реализуйте класс стека для работы со строками (стек строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.

class StringStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, string):
        if len(self.stack) < self.size:
            self.stack.append(string)
        else:
            print("Stack is full")

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("Stack is empty")

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Stack is empty")



stack = StringStack(3)
print("1. Поместите строку в стек")
print("2. Извлеките строку из стека")
print("3. Количество строк в стеке")
print("4. Проверьте, пуст ли стек")
print("5. Проверьте, заполнен ли стек")
print("6. Очистите стек")
print("7. Взгляните на верхнюю строку в стеке")

while True:
    choice = int(input("Введите свой выбор: "))
    if choice == 1:
        string = input("Введите строку, которую нужно поместить в стек: ")
        stack.push(string)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        print("Количество строк в стеке:", stack.count())
    elif choice == 4:
        print("Пуст ли стек?", stack.is_empty())
    elif choice == 5:
        print("Заполнен ли стек?", stack.is_full())
    elif choice == 6:
        stack.clear()
        print("Стек очищен")
    elif choice == 7:
        top_string = stack.peek()
        if top_string:
            print("Верхняя строка в стеке:", top_string)
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")

# 3. Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return False

    def clear(self):
        self.stack = []

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
         return None

stack = Stack()

while True:
    print("Menu:")
    print("1. Put rows on the stack")
    print("2. Extract a line from the stack")
    print("3. Count strings in stack")
    print("4. Check if stack is empty")
    print("5. Check if stack is full")
    print("6. Clear stack")
    print("7. Peek at top string in stack")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        string = input("Enter string to push: ")
        stack.push(string)
    elif choice == "2":
        popped_string = stack.pop()
        if popped_string:
            print("Popped string:", popped_string)
        else:
            print("Stack is empty")
    elif choice == "3":
        print("Number of strings in stack:", stack.count())
    elif choice == "4":
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == "5":
        if stack.is_full():
            print("Stack is full")
        else:
            print("Stack is not full")
    elif choice == "6":
        stack.clear()
        print("Stack cleared")
    elif choice == "7":
        top_string = stack.peek()
        if top_string:
            print("Top string in stack:", top_string)
        else:
            print("Stack is empty")
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")