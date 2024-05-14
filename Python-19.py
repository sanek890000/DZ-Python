# 1.  Напишите регулярное выражение, которое соответствует всем строкам, начинающимся с гласной
#  и заканчивающимся на согласную.

# вариант -1

import re

pattern = r'^[aeiouAEIOU].*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]$'

strings = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'python']

for string in strings:
    if re.match(pattern, string):
        print(f'{string} соответствует шаблону')
    else:
        print(f'{string} не соответствует шаблону')

# вариант-2
import re

pattern = r'^[aeiouAEIOU].*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]$'

test_string = "apple" "Hello Python"
result = re.match(pattern, test_string)

if result:
    print("Соответствует")
else:
    print("Не соответствует")

# 2. Напишите регулярное выражение, которое соответствует всем URL адресам.

import re

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # схема
    r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+'  # доменное имя
    r'[a-zA-Z]{2,}$'  # зона
)

url1 = "https://yandex.ru"
url2 = "http://google.com"
url3 = "ftp://test.org"

if url_regex.match(url1):
    print(f"{url1} is a valid URL")
else:
    print(f"{url1} is not a valid URL")

if url_regex.match(url2):
    print(f"{url2} is a valid URL")
else:
    print(f"{url2} is not a valid URL")

if url_regex.match(url3):
    print(f"{url3} is a valid URL")
else:
    print(f"{url3} is not a valid URL")

# 3. Напишите регулярное выражение, которое соответствует всем строкам, содержащим хотя бы одно слово, начинающееся
# с заглавной буквы

import re

pattern = r'\b[A-Z]\w+\b'


s1 = "This is a Sample String"
s2 = "Python is a versatile language"
s3 = "Regular Expressions are powerful"
s4 = "hello World"


print(re.findall(pattern, s1))
print(re.findall(pattern, s2))
print(re.findall(pattern, s3))
print(re.findall(pattern, s4))

# 4. Напишите регулярное выражение, которое соответствует всем строкам, содержащим повторяющуюся букву
# (например "book" или "letter")

import re

re.search(r'(\w).*\1', 'book') # соответствует
re.search(r'(\w).*\1', 'letter') # соответствует
re.search(r'(\w).*\1', 'python') # не соответствует

string = "This is a test string with repeat letter"

result = re.findall(r'(\w).*\1', string)


for match in result:
    print("Найдено совпадение:", match)

