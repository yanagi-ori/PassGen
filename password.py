from base64 import b64encode, b64decode
from easygui import choicebox, msgbox, multpasswordbox, multenterbox
from easygui.boxes.fillable_box import __fillablebox
from random import choice as random


def passwordbox(msg="Enter your password.", title=" ", default="",
                image=None, root=None):
    return __fillablebox(msg, title, default, mask="*",
                         image=image, root=root)


def menu():
    menu_title = 'Меню'
    menu_msg = 'Выберите'
    choices = ['1 - Сгенерировать случайный пароль',
               '2 - Записать существующий',
               '3 - Читать пароли',
               '4 - Очистить список паролей',
               '5 - Список изменений',
               '0 - Выход']
    choice = choicebox(menu_msg, menu_title, choices)
    return choice


def encoder(key, clear):
    enc = []
    for index, item in enumerate(clear):
        key_c = key[index % len(key)]
        enc_c = chr(ord(item) + ord(key_c) % 256)
        enc.append(enc_c)
    return b64encode("".join(enc).encode()).decode()


def decoder(key, enc):
    dec = []
    enc = b64decode(enc).decode()
    for index, item in enumerate(enc):
        key_c = key[index % len(key)]
        dec_c = chr((256 + ord(item) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


file_path = 'storage'
try:
    fp = open(file_path)
except FileNotFoundError:
    fp = open(file_path, 'w')

msg = "Введите ключ шифрования"
title = "Пароль"
pw = passwordbox(msg, title)
if pw == '':
    pw = 'empty'
work = True
box_button = 'Вернуться'
name_box = 'Введите название для пароля: '
while work:
    choice = menu()

    if choice == '0 - Выход':
        exit('Спасибо за использование программы')

    elif choice == '1 - Сгенерировать случайный пароль':
        storage = open('storage', 'r')
        read = storage.read()
        read = decoder(pw, read)
        msg = 'Введите данные для генерации случайного пароля'
        title = 'Генерация случайного пароля'
        fieldNames = ['Название пароля', 'Длина пароля']
        fieldValues = multenterbox(msg, title, fieldNames)
        password_name = fieldValues[0]
        chars = int(fieldValues[1])
        password = ''.join([random(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
                            for x in range(chars)])
        msgbox('Можете скопировать и использовать: ' + password, 'Пароль готов!', 'Далее')
        read = read + password_name + ': ' + password + '\n'
        storage.close()
        storage = open('storage', 'w')
        storage.write(encoder(pw, read))

    elif choice == '2 - Записать существующий':
        storage = open('storage', 'r')
        read = storage.read()
        read = decoder(pw, read)
        storage.close()
        storage = open('storage', 'w')
        msg = 'Введите логин и пароль'
        title = 'Запись существующего пароля'
        fieldNames = ['Название пароля', 'Пароль']
        fieldValues = multpasswordbox(msg, title, fieldNames)
        password_name = fieldValues[0]
        password = fieldValues[1]
        to_encode = read + password_name + ': ' + password + '\n'
        storage.write(encoder(pw, to_encode))

    elif choice == '3 - Читать пароли':
        storage = open('storage', 'r')
        read = storage.read()
        decoded = decoder(pw, read)
        msgbox(decoded, 'Ваши пароли', box_button)

    elif choice == '4 - Очистить список паролей':
        storage = open('storage', 'w')
        storage.write('')
        msgbox('Ваши записи стерты', 'Очистка паролей', box_button)

    elif choice == '5 - Список изменений':
        title = 'Список изменений PassGen'
        changelog = '4.1 - Чистка кода ' \
                    '4.0 - Графический интерфейс! Внедрен на 30-40% ' \
                    '3.2 - Многочисленные фиксы - Новые пункты в меню программы ' \
                    '3.1 - Добавлена функция очистки данных (-1 в меню) ' \
                    '3.0 - Введено шифрование - Временный отказ от чтения ' \
                    '2.1 - Пароль для входа в программу - Меню в отдельном файле ' \
                    '- Незначительно улучшен код программы' \
                    '2.0 - Меню программы - Сохранение паролей - Запись уже существующего пароля ' \
                    '- Чтение паролей из программы' \
                    '1.0 - Простой генератор случайного пароля'
        msgbox(changelog, title, box_button)
