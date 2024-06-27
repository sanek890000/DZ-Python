# 1. Реализуйте клиент — серверное приложение, позволяющее двум людям играть
# в игру крестики — нолики. Один из игроков инициирует игру, если второй игрок
# подтверждает, то игра начинается. Игру можно прекратить, тот кто прекратил игру
# считается проигравшим. После завершения игры, можно инициировать повторный матч.

# Сервер

import socket
import threading

def handle_client(client_socket, addr, clients):
    print(f"Player {addr} connected.")
    clients.append((client_socket, addr))
    if len(clients) == 2:
        start_game(clients)
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            if message.decode() == 'quit':
                print(f"Player {addr} has left the game.")
                break
            for c in clients:
                if c[0] != client_socket:
                    c[0].send(message)
        except:
            break
    client_socket.close()
    clients.remove((client_socket, addr))

def start_game(clients):
    clients[0][0].send(b'START:X')
    clients[1][0].send(b'START:O')

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server started. Waiting for connections...")
    clients = []
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, clients))
        client_handler.start()

if __name__ == "__main__":
    main()

# Клиент.

import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            break

def send_messages(sock):
    while True:
        message = input('>')
        sock.send(message.encode())
        if message == 'quit':
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client.close()

if __name__ == "__main__":
    main()

# пример использования.

# 1. Запустите два клиента (например, в двух разных терминалах):

# 2. Сервер ждет подключения двух клиентов и инициирует игру отправляя START:X и START:O.

# 3. Клиенты отправляют ходы и могут в любое время завершить игру командой quit.


# 2. Реализуйте клиент — серверное приложение,
# позволяющее передавать файлы. Один пользователь инициирует
# передачу файла, второй подтверждает.
# После подтверждения начинается отправка.
# Если отправка была удачной необходимо сообщить об этом отправителю.

# Сервер

import socket
import os

def handle_client(client_socket):
    file_info = client_socket.recv(1024).decode()
    file_name, file_size = file_info.split('|')
    file_size = int(file_size)

    print(f'Получение файла: {file_name} размером {file_size} байт')

    client_socket.send('ГОТОВ ПРИНИМАТЬ ФАЙЛ'.encode())

    with open(file_name, 'wb') as file:
        bytes_received = 0
        while bytes_received < file_size:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            file.write(chunk)
            bytes_received += len(chunk)

    print(f'Файл {file_name} успешно принят')

    client_socket.send('ФАЙЛ УСПЕШНО ПРИНЯТ'.encode())
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print('Сервер слушает на порту 9999...')

    while True:
        client_socket, addr = server.accept()
        print(f'Соединение от {addr}')
        handle_client(client_socket)

if __name__ == '__main__':
    main()

# Клиент.

import socket
import os

def send_file(file_path, server_ip, server_port):
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))


    client.send(f'{file_name}|{file_size}'.encode())

    response = client.recv(1024).decode()
    if response == 'ГОТОВ ПРИНИМАТЬ ФАЙЛ':
        print('Сервер готов принять файл. Начинаю передачу...')

        with open(file_path, 'rb') as file:
            chunk = file.read(1024)
            while chunk:
                client.send(chunk)
                chunk = file.read(1024)

        print('Файл успешно отправлен. Ожидаю подтверждение...')

        confirmation = client.recv(1024).decode()
        if confirmation == 'ФАЙЛ УСПЕШНО ПРИНЯТ':
            print('Сервер подтвердил успешное получение файла.')
        else:
            print('Ошибка при получении подтверждения от сервера.')
    else:
        print('Сервер отклонил передачу файла.')


    client.close()

if __name__ == '__main__':
    file_path = 'server.txt'
    server_ip = '127.0.0.1'
    server_port = 9999

    send_file(file_path, server_ip, server_port)
