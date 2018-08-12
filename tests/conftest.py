import pytest

BASE_FIXTURES_PATH = 'tests/fixtures/'


@pytest.fixture()
def fr_hawking():
    files_list = [
        # path - encoding - success
        (BASE_FIXTURES_PATH + 'fr-hawking/' + 'UTF-8.txt', 'utf-8', True),
        (BASE_FIXTURES_PATH + 'fr-hawking/' + 'ASCII_altered.txt', 'ascii', True),
        (BASE_FIXTURES_PATH + 'fr-hawking/' + 'ISO-8859-1_altered.txt', 'ISO-8859-1', True),
        (BASE_FIXTURES_PATH + 'fr-hawking/' + 'ISO-8859-15_altered.txt', 'ISO-8859-15', False),
        (BASE_FIXTURES_PATH + 'fr-hawking/' + 'MacRoman_altered.txt', 'MacRoman', False),
        (BASE_FIXTURES_PATH + 'fr-hawking/' + 'Windows-1252.txt', 'Windows-1252', True),
    ]

    to_ret = []
    for file_path, encoding, success in files_list:
        with open(file_path, 'rb') as f:
            to_ret.append((f.read(), encoding, success))

    return to_ret


@pytest.fixture()
def fr_lfs():
    files_list = [
        # path - encoding - success
        (BASE_FIXTURES_PATH + 'fr-lfs/' + 'UTF-8.txt', 'utf-8', True),
        (BASE_FIXTURES_PATH + 'fr-lfs/' + 'ASCII_altered.txt', 'ascii', True),
        (BASE_FIXTURES_PATH + 'fr-lfs/' + 'ISO-8859-1_altered.txt', 'ISO-8859-1', True),
        (BASE_FIXTURES_PATH + 'fr-lfs/' + 'ISO-8859-15.txt', 'ISO-8859-15', False),
        (BASE_FIXTURES_PATH + 'fr-lfs/' + 'MacRoman.txt', 'MacRoman', False),
        (BASE_FIXTURES_PATH + 'fr-lfs/' + 'Windows-1252.txt', 'Windows-1252', True),
    ]

    to_ret = []
    for file_path, encoding, success in files_list:
        with open(file_path, 'rb') as f:
            to_ret.append((f.read(), encoding, success))

    return to_ret
