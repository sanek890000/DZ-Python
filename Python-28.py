# 1. При старте приложения запускаются три потока. Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список  заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток среднеарифметическое значение в списке. Полученный список, сумма и
# среднеарифметическое выводятся на экран.

import threading
import random
import time


shared_list = []
list_filled_event = threading.Event()

def fill_list():
    global shared_list
    shared_list = [random.randint(1, 100) for _ in range(10)]
    print(f"Список заполнен: {shared_list}")
    list_filled_event.set()

def calculate_sum():
    list_filled_event.wait()
    list_sum = sum(shared_list)
    print(f"Сумма элементов списка: {list_sum}")

def calculate_average():
    list_filled_event.wait()
    list_average = sum(shared_list) / len(shared_list)
    print(f"Среднее арифметическое значение в списке: {list_average}")

# Создание потоков
fill_thread = threading.Thread(target=fill_list)
sum_thread = threading.Thread(target=calculate_sum)
average_thread = threading.Thread(target=calculate_average)

# Запуск потоков
fill_thread.start()
sum_thread.start()
average_thread.start()

fill_thread.join()
sum_thread.join()
average_thread.join()

print("Все потоки завершены.")

# 2. Пользователь с клавиатуры вводит путь к файлу. После чего запускаются три потока. Первый поток
# заполняет файл случайными числами. Два других потока ожидают заполнения. Когда файл заполнен оба потока
# стартуют. Первый поток находит все простые числа, второй поток факториал каждого числа в файле.
# Результаты поиска каждый поток должен записать в новый файл.
# На экран необходимо отобразить статистику выполненных операций.

import threading
import random
import time
import math
from pathlib import Path

def fill_file_with_random_numbers(file_path, num_numbers=100, max_value=1000):
    with open(file_path, 'w') as f:
        numbers = [random.randint(1, max_value) for _ in range(num_numbers)]
        f.write(' '.join(map(str, numbers)))
    return numbers

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(numbers, output_file_path):
    primes = [num for num in numbers if is_prime(num)]
    with open(output_file_path, 'w') as f:
        f.write(' '.join(map(str, primes)))

def calculate_factorials(numbers, output_file_path):
    factorials = [math.factorial(num) for num in numbers]
    with open(output_file_path, 'w') as f:
        f.write(' '.join(map(str, factorials)))

def main():
    input_path = input("Введите путь к файлу: ")
    input_path = Path(input_path)
    primes_output_path = input_path.with_suffix('.primes.txt')
    factorials_output_path = input_path.with_suffix('.factorials.txt')

    # Запуск первого потока для генерации случайных чисел
    numbers = None
    def generate_numbers():
        nonlocal numbers
        numbers = fill_file_with_random_numbers(input_path)

    generator_thread = threading.Thread(target=generate_numbers)

    # Запуск потоков для поиска простых чисел и вычисления факториалов
    primes_thread = threading.Thread(target=find_primes, args=(numbers, primes_output_path))
    factorials_thread = threading.Thread(target=calculate_factorials, args=(numbers, factorials_output_path))

    # Запуск потока генерации, ожидание его завершения и запуск следующих потоков
    generator_thread.start()
    generator_thread.join()
    primes_thread.start()
    factorials_thread.start()
    primes_thread.join()
    factorials_thread.join()

    print(f"Файл с простыми числами сохранен в: {primes_output_path}")
    print(f"Файл с факториалами сохранен в: {factorials_output_path}")

if __name__ == "__main__":
    main()

# 3. Пользователь с клавиатуры вводит путь к существующей директории
# и к новой директории. После чего запускается поток, который должен скопировать содержимое директории в новое место.
# Необходимо сохранить структуру директории. На экран необходимо отобразить
# статистику выполненных операций.

import os
import shutil
import threading

def copy_directory_contents(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(src):
        # Создаём корректные пути для файлов и директорий
        for directory in dirs:
            src_dir_path = os.path.join(root, directory)
            relative_path = os.path.relpath(src_dir_path, src)
            dest_dir_path = os.path.join(dest, relative_path)
            os.makedirs(dest_dir_path, exist_ok=True)
            total_dirs += 1

        for file in files:
            src_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(src_file_path, src)
            dest_file_path = os.path.join(dest, relative_path)
            shutil.copy2(src_file_path, dest_file_path)
            total_files += 1

    print(f'Копирование завершено: скопировано {total_files} файлов и {total_dirs} директорий.')

# Функция запускающая поток
def start_copy_process(src, dest):
    copy_thread = threading.Thread(target=copy_directory_contents, args=(src, dest))
    copy_thread.start()

if __name__ == "__main__":
    src_path = input("Введите путь к существующей директории: ")
    dest_path = input("Введите путь к новой директории: ")

    if not os.path.exists(src_path):
        print("Указанный путь не существует. Пожалуйста, введите действительный путь.")
    else:
        start_copy_process(src_path, dest_path)

# 4. Пользователь с клавиатуры вводит путь к существующей директории и слово для поиска. После чего запускаются
# два потока. Первый должен найти файлы, содержащие искомое слово и слить их содержимое в один файл.
# Второй поток ожидает завершения работы первого потока.
# После чего проводит вырезание всех запрещенных слов
# (список этих слов нужно считать из файла с запрещенными словами)
# из полученного файла. На экран необходимо отобразить статистику выполненных операций.

import os
import threading

def find_files_with_word(directory, word, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if word in content:
                            output.write(content + '\\n')
                            print(f"Слово '{word}' найдено в файле: {file_path}")
                except IOError as e:
                    print(f"Ошибка при чтении файла {file_path}: {e}")


def remove_forbidden_words(input_file, forbidden_words_file):
    try:
        with open(forbidden_words_file, 'r', encoding='utf-8') as f:
            forbidden_words = f.read().splitlines()

        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        for word in forbidden_words:
            content = content.replace(word, '')

        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Запрещенные слова удалены из файла: {input_file}")

    except IOError as e:
        print(f"Ошибка при обработке файла: {e}")


def main():
    directory = input("Введите путь к директории: ")
    search_word = input("Введите слово для поиска: ")
    forbidden_words_file = input("Введите путь к файлу с запрещенными словами: ")
    output_file = "output.txt"

    search_thread = threading.Thread(target=find_files_with_word, args=(directory, search_word, output_file))
    search_thread.start()
    search_thread.join()

    remove_thread = threading.Thread(target=remove_forbidden_words, args=(output_file, forbidden_words_file))
    remove_thread.start()
    remove_thread.join()

    print("Все операции завершены.")


if __name__ == "__main__":
    main()
