import sqlite3

def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Студенты (
            Имя TEXT,
            Фамилия TEXT,
            Возраст INTEGER,
            Группа TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_student():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    group = input('Введите группу: ')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Студенты (Имя, Фамилия, Возраст, Группа)
        VALUES (?, ?, ?, ?)
    ''', (name, surname, age, group))
    conn.commit()
    conn.close()
    print('Студент добавлен.')

def edit_student():
    surname = input('Введите фамилию студента, которого хотите изменить: ')
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Студенты WHERE Фамилия = ?', (surname,))
    student = cursor.fetchone()

    if student:
        print(f'Текущие данные: Имя={student[0]}, Фамилия={student[1]}, Возраст={student[2]}, Группа={student[3]}')
        new_name = input('Введите новое имя (или нажмите Enter, чтобы оставить прежним): ') or student[0]
        new_surname = input('Введите новую фамилию (или нажмите Enter, чтобы оставить прежним): ') or student[1]
        new_age = input('Введите новый возраст (или нажмите Enter, чтобы оставить прежним): ')
        new_age = int(new_age) if new_age else student[2]
        new_group = input('Введите новую группу (или нажмите Enter, чтобы оставить прежним): ') or student[3]

        cursor.execute('''
            UPDATE Студенты
            SET Имя = ?, Фамилия = ?, Возраст = ?, Группа = ?
            WHERE Фамилия = ?
        ''', (new_name, new_surname, new_age, new_group, surname))
        conn.commit()
        print('Данные студента обновлены.')
    else:
        print('Студент не найден.')

    conn.close()

def delete_student():
    surname = input('Введите фамилию студента, которого хотите удалить: ')
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Студенты WHERE Фамилия = ?', (surname,))
    conn.commit()
    conn.close()
    print('Студент удален, если он существовал.')

def menu():
    while True:
        print('Выберите действие:')
        print('1. Добавить нового студента')
        print('2. Редактирование данных')
        print('3. Удаление')
        print('4. Выйти из программы')
        choice = int(input('Ваш выбор: '))

        if choice == 1:
            add_student()
        elif choice == 2:
            edit_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            break
        else:
            print('Некорректный выбор. Попробуйте снова.')

if __name__ == '__main__':
    create_table()
    menu()
