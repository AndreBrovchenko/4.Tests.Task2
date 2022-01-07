import requests
from ya_disk import YaUploader


def get_token():
    """ Функция считывает из файла токен для Я.Диска """
    with open('ya_token.txt', 'r', encoding='utf-8') as yandex_file:
        ya_token = yandex_file.read().strip()
        return ya_token


if __name__ == '__main__':
    # print(f'Запрашиваем токен от пользователя\n ----')
    # token_ya = input('Введите ТОКЕН для Я.Диск: ')
    token = get_token()
    # token = 's'
    creator = YaUploader(token)
    name_folder = 'test'
    # code_answer = creator.create_folder(name_folder)
    code_answer = creator.get_find_folders(name_folder)
    if code_answer == 200:
        print(f'папка {name_folder} существует')
    else:
        print(f'Что-то пошло не так. Код ответа: {code_answer}')
