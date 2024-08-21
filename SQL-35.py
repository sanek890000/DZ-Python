import sqlite3
import hashlib
import os


conn = sqlite3.connect('online_store.db')
cursor = conn.cursor()


def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        stock INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        status TEXT NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(product_id) REFERENCES products(id))''')
    conn.commit()


def register_user(username, password, email):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                       (username, hashed_password, email))
        conn.commit()
        print("Регистрация прошла успешно.")
    except sqlite3.IntegrityError:
        print("Имя пользователя уже существует. Не удалось выполнить регистрацию.")


def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        print("Неверные учетные данные.")
        return None


def change_user_data(user_id, new_username, new_password, new_email):
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    cursor.execute('''UPDATE users SET username = ?, password = ?, email = ? WHERE id = ?''',
                   (new_username, hashed_password, new_email, user_id))
    conn.commit()
    print("Пользовательские данные успешно обновлены.")


def view_catalog():
    cursor.execute('SELECT id, name, price, stock FROM products')
    products = cursor.fetchall()
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")


def add_to_cart(user_id, product_id, quantity):
    cursor.execute('INSERT INTO orders (user_id, product_id, quantity, status) VALUES (?, ?, ?, ?)',
                   (user_id, product_id, quantity, 'in_cart'))
    conn.commit()
    print("Товар добавлен в корзину.")


def place_order(user_id):
    cursor.execute('UPDATE orders SET status = ? WHERE user_id = ? AND status = ?', ('ordered', user_id, 'in_cart'))
    conn.commit()
    print("Заказ успешно размещен.")


def cli():
    create_tables()

    while True:
        print("Интернет-магазин")
        print("1. Регистрация")
        print("2. Логин")
        print("3. Изменить пользовательские данные")
        print("4. Просмотр каталога")
        print("5. Добавить в корзину")
        print("6. Разместить заказ")
        print("7. Выход")
        choice = input("Выберите нужный вариант: ")

        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            email = input("Введите адрес электронной почты: ")
            register_user(username, password, email)

        elif choice == '2':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            user_id = login_user(username, password)
            if user_id:
                print(f"Добро пожаловать, {username}! Ваш идентификатор пользователя {user_id}")

        elif choice == '3':
            user_id = int(input("Введите идентификатор пользователя: "))
            new_username = input("Введите новое имя пользователя: ")
            new_password = input("Введите новый пароль:")
            new_email = input("Введите новый адрес электронной почты: ")
            change_user_data(user_id, new_username, new_password, new_email)

        elif choice == '4':
            view_catalog()

        elif choice == '5':
            user_id = int(input("Введите идентификатор пользователя: "))
            product_id = int(input("Введите идентификатор продукта: "))
            quantity = int(input("Введите количество: "))
            add_to_cart(user_id, product_id, quantity)

        elif choice == '6':
            user_id = int(input("Введите идентификатор пользователя: "))
            place_order(user_id)

        elif choice == '7':
            conn.close()
            print("До свидания!")
            break

        else:
            print("Недопустимый параметр. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    cli()
