import pytest
from ya_disk import YaUploader

with open('ya_token.txt', 'r', encoding='utf-8') as yandex_file:
    token_ya = yandex_file.read().strip()
token_ya_no_valid = 'token'

TEST_DATA_GF = ([
    [201, 'test', token_ya],
    [409, 'test', token_ya],
    [404, '3//test', token_ya],
    [401, 'test', token_ya_no_valid]
])

TEST_DATA_FF = ([
    [200, 'test', token_ya],
    [404, 'test2', token_ya],
    [401, 'test', token_ya_no_valid]
])


class TestRestApiPy:
    """ класс тестов """

    @pytest.mark.parametrize('expected_result, path_folder, token', TEST_DATA_GF)
    def test_create_folder(self, expected_result, path_folder, token):
        assert YaUploader(token).create_folder(path_folder) == expected_result
        if expected_result == 201:
            code_answer = YaUploader(token).get_find_folders(path_folder)
            if code_answer == 200:
                print(f'Папка {path_folder} найдена в каталоге')
            else:
                print(f'Папка {path_folder} не найдена. Статуст ответа: {code_answer}')

    @pytest.mark.parametrize('expected_result, path_folder, token', TEST_DATA_FF)
    def test_find_folder(self, expected_result, path_folder, token):
        assert YaUploader(token).get_find_folders(path_folder) == expected_result
