# 1. Напишите регулярное выражение для разбора строк логов определенного формата.
# Например, для строки лога "2024-05-12 12:34:56 [INFO] Сообщение лога" нужно
# извлечь дату, время, уровень логирования и само сообщение.

import re

log_string = "2024-05-12 12:34:56 [info] сообщение лога"

pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)"

match = re.match(pattern, log_string)

if match:

    date = match.group(1)
    time = match.group(2)
    level = match.group(3)
    message = match.group(4)

    print("Дата:", date)
    print("Время:", time)
    print("Уровень логирования:", level)
    print("Сообщение:", message)
else:
    print("Строка лога не соответствует формату")

# 2. Напишите регулярное выражение, которое проверит, является ли строка допустимым паролем.
# Пароль считается допустимым, если он содержит как минимум 8 символов, включая
# хотя бы одну строчную букву, одну заглавную букву, одну цифру и один специальный символ.

import re


def check_password(password):
    if len(password) < 8:
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[\W_]", password):
        return False

    return True

print(check_password("StrongPassword123!"))
print(check_password("weakpass"))
print(check_password("Password123"))
print(check_password("12345678"))

# 3. Напишите регулярное выражение, которое извлечет данные из HTML-таблицы, включая теги
# <table>, <tr>, <td>, и содержимое ячеек. Например, из строки HTML-таблицы:

# Вариант -1

import re

html_table = """
<table>
  <tr>
    <td>Row 1, Column 1</td>
    <td>Row 1, Column 2</td>
  </tr>
  <tr>
    <td>Row 2, Column 1</td>
    <td>Row 2, Column 2</td>
  </tr>
</table>
"""

pattern = r'<tr>(.*?)<\/tr>'
result = re.findall(pattern, html_table, re.DOTALL)

for row in result:
    columns = re.findall(r'<td>(.*?)</td>', row)
    print(columns)

# Вариант-2

import re

html_table = ("<table><tr><td>Ячейка 1</td><td>Ячейка"
" 2</td></tr><tr><td>Ячейка 3</td><td>Ячейка 4</td></tr></table>")

pattern = re.compile(r'<table>.*?</table>', re.DOTALL)
row_pattern = re.compile(r'<tr>.*?</tr>', re.DOTALL)
cell_pattern = re.compile(r'<td>(.*?)</td>')

table_data = re.findall(pattern, html_table)
for row in re.findall(row_pattern, table_data[0]):
    cells = re.findall(cell_pattern, row)
    print(cells)

# 4. Напишите регулярное выражение, которое найдет все ссылки в тексте, включая ссылки
# на веб-сайты (http/https), электронные адреса и ссылки на файлы. Затем оберните его
# в функцию, которая возвращает данные в виде словаря:
# {"Ссылки": [...], "Почты": [...], "Файлы": [...]}

# Вариант-1

import re

def find_links(text):
    link_regex = r'(https?://[^\s]+)|([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})|(\b\w+\.pdf\b)'

    matches = re.findall(link_regex, text)

    links_dict = {"ссылки": [], "почты": [], "файлы": []}

    for match in matches:
        for link in match:
            if link:
                if link.startswith("http"):
                    links_dict["ссылки"].append(link)
                elif "@" in link:
                    links_dict["почты"].append(link)
                elif link.endswith(".pdf"):
                    links_dict["файлы"].append(link)

    return links_dict

text = "Visit our website at https://www.google.com or send an email to sokol89@mail.ru You can also download the file report.pdf."
result = find_links(text)
print(result)

# Вариант -2

import re

def find_links(text):
    regex = r'(https?://\S+|[\w\.-]+@[\w\.-]+|\S+\.pdf|\S+\.docx)'

    matches = re.findall(regex, text)

    data = {"ссылки": [], "почты": [], "файлы": []}

    for match in matches:
        if match.startswith("http"):
            data["ссылки"].append(match)
        elif "@" in match:
            data["почты"].append(match)
        elif match.endswith(".pdf") or match.endswith(".docx"):
            data["файлы"].append(match)

    return data

text = "Привет, вот ссылка на мой сайт: https://google.com, а это мой email: sokol89@mail.ru. Можешь скачать файлы: Python.pdf и resume.docx."
result = find_links(text)
print(result)