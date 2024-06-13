# 1. Создайте реализацию паттерна Command. Протестируйте работу созданного класса.

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            self.commands[slot].execute()
        else:
            print("No command set for this slot")

light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(0, light_on)
remote.set_command(1, light_off)

remote.press_button(0)
remote.press_button(1)
remote.press_button(2)

# 2. Есть класс, предоставляющий доступ к набору чисел. Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому набору необходимо вносить запись в лог-файл. При реализации используйте
# паттерн Proxy (для логгирования) и другие необходимые паттерны.

from abc import ABC, abstractmethod
import logging

class DataSetInterface(ABC):
    @abstractmethod
    def get_data(self):
        pass

class DataSet(DataSetInterface):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = []

    def update_data(self):
# Реализация обновления данных из файла
        self.data = [1, 2, 3, 4, 5]
        logging.info('Data has been updated from file: {}'.format(self.file_name))

    def get_data(self):
        return self.data

# Прокси-класс, который добавляет логгирование при доступе к данным
class DataSetProxy(DataSetInterface):
    def __init__(self, dataset):
        self.dataset = dataset

    def get_data(self):
        logging.info('Accessing dataset')
        return self.dataset.get_data()


if __name__ == "__main__":
    logging.basicConfig(filename='dataset.log', level=logging.INFO)

    dataset = DataSet("data.txt")
    proxy = DataSetProxy(dataset)

    proxy.get_data()
    dataset.update_data()
    proxy.get_data()

# 3. Создайте приложение для работы в библиотеке. Оно должно оперировать следующими сущностями: Книга, Библиотекарь, Читатель.
#  Приложение должно позволять вводить, удалять, изменять, сохранять в файл, загружать из файла, логгировать действия, искать информацию
#  (результаты поиска выводятся на экран или файл) о сущностях. При реализации используйте максимально возможное
# количество паттернов проектирования.

from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='library.log', level=logging.INFO)

class Entity(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def save_to_file(self, file_name):
        pass

    @abstractmethod
    def load_from_file(self, file_name):
        pass

class Book(Entity):
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def create(self):
        logging.info(f'Added new book: {self.title} by {self.author}')

    def delete(self):
        logging.info(f'Deleted book: {self.title}')

    def update(self, new_title, new_author, new_genre):
        self.title = new_title
        self.author = new_author
        self.genre = new_genre
        logging.info(f'Updated book information: {self.title} by {self.author}')

    def save_to_file(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f'{self.title}, {self.author}, {self.genre}\\n')
        logging.info(f'Saved book information to file: {self.title}')

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
            for line in data:
                info = line.strip().split(',')
                logging.info(f'Loaded book information from file: {info[0]}')
                print(f'Book: {info[0]}, Author: {info[1]}, Genre: {info[2]}')

class Librarian(Entity):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def create(self):
        logging.info(f'Added new librarian: {self.name}, {self.position}')

    def delete(self):
        logging.info(f'Deleted librarian: {self.name}')

    def update(self, new_name, new_position):
        self.name = new_name
        self.position = new_position
        logging.info(f'Updated librarian information: {self.name}, {self.position}')

    def save_to_file(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f'{self.name}, {self.position}\\n')
        logging.info(f'Saved librarian information to file: {self.name}')

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
            for line in data:
                info = line.strip().split(',')
                logging.info(f'Loaded librarian information from file: {info[0]}')
                print(f'Librarian: {info[0]}, Position: {info[1]}')

class Reader(Entity):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def create(self):
        logging.info(f'Added new reader: {self.name}, {self.age}')

    def delete(self):
        logging.info(f'Deleted reader: {self.name}')

    def update(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
        logging.info(f'Updated reader information: {self.name}, {self.age}')

    def save_to_file(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f'{self.name}, {self.age}\\n')
        logging.info(f'Saved reader information to file: {self.name}')

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
            for line in data:
                info = line.strip().split(',')
                logging.info(f'Loaded reader information from file: {info[0]}')
                print(f'Reader: {info[0]}, Age: {info[1]}')


book1 = Book("Harry Potter", "J.K. Rowling", "Fantasy")
book1.create()
book1.save_to_file("books.txt")

librarian1 = Librarian("Alice", "Head Librarian")
librarian1.create()
librarian1.save_to_file("librarians.txt")

reader1 = Reader("Bob", 25)
reader1.create()
reader1.save_to_file("readers.txt")

book2 = Book("1984", "George Orwell", "Dystopian")
book2.load_from_file("books.txt")

librarian2 = Librarian("Charlie", "Assistant Librarian")
librarian2.load_from_file("librarians.txt")

reader2 = Reader("Eve", 30)
reader2.load_from_file("readers.txt")