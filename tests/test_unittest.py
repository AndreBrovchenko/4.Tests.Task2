import unittest

# from parameterized import parameterized
from ya_disk import YaUploader
# from main import get_token


class TestRestApi(unittest.TestCase):
    """ класс тестов """
    """ считываем из файла токен для Я.Диска """
    with open('ya_token.txt', 'r', encoding='utf-8') as yandex_file:
        token_ya = yandex_file.read().strip()

    def test_create_folder(self):
        # положительный тест. Создаем папку, ждем ответ 201 (ОК - папка создана)
        new_folder = 'test'
        creator = YaUploader(self.token_ya)
        code_answer = creator.create_folder(new_folder)
        self.assertEqual(201, code_answer, f'Ошибка осздания папки {new_folder} на Я.Диске')
        code_answer = creator.get_find_folders(new_folder)
        if code_answer == 200:
            print(f'Папка {new_folder} найдена в каталоге')
        else:
            print(f'Папка {new_folder} не найдена. Статуст ответа: {code_answer}')

    # @parameterized.expand([
    #     ['test', 201],
    #     ['test', 409]
    # ])
    # def test_create_folder_201_409(self, path_folder, result):
    #     # отрицательный тест. Создаем папку, но передает не валидный токен, ждем ответ 401 (Не авторизован.)
    #     # path_folder = 'test'
    #     creator = YaUploader(self.token_ya)
    #     code_answer = creator.create_folder(path_folder)
    #     self.assertEqual(result, code_answer, f'Ошибка осздания папки {path_folder} на Я.Диске')

    def test_create_folder_401(self):
        # отрицательный тест. Создаем папку, но передает не валидный токен, ждем ответ 401 (Не авторизован.)
        new_folder = 'test'
        creator = YaUploader('token')
        code_answer = creator.create_folder(new_folder)
        self.assertEqual(401, code_answer, f'Ошибка осздания папки {new_folder} на Я.Диске')

    def test_create_folder_409(self):
        # отрицательный тест. Создаем папку которая уже существует, ждем ответ 409 (Ресурс "{path}" уже существует.)
        new_folder = 'test'
        creator = YaUploader(self.token_ya)
        code_answer = creator.create_folder(new_folder)
        self.assertEqual(409, code_answer, f'Ошибка осздания папки {new_folder} на Я.Диске')

    def test_find_folder(self):
        # положительный тест. Проверяем существование папки, ждем ответ 200 (ОК - папка существует)
        new_folder = 'test'
        creator = YaUploader(self.token_ya)
        code_answer = creator.get_find_folders(new_folder)
        self.assertEqual(200, code_answer, f'Папка не найдена. Статуст ответа: {code_answer}')

    def test_find_folder_status_401(self):
        # отрицательный тест. Передаем не правильный токен и ждем ответ 401 (Не авторизован.)
        new_folder = 'test2'
        creator = YaUploader('token')
        code_answer = creator.get_find_folders(new_folder)
        self.assertEqual(401, code_answer)

    def test_find_folder_status_404(self):
        # отрицательный тест. Папки нет, ждем ответ 404 (Не удалось найти запрошенный ресурс.)
        new_folder = 'test2'
        creator = YaUploader(self.token_ya)
        code_answer = creator.get_find_folders(new_folder)
        self.assertEqual(404, code_answer)


if __name__ == '__main__':
    unittest.main()
