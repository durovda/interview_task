from unittest.mock import patch

import pytest

from file_handler import FileManager
from file_reader import FileReader
from line_parser import LineParser
from storage import Storage


@pytest.mark.parametrize('line', ('apple : 10',
                                  'banana: 5',
                                  'orange: -3',
                                  '  grape:444 '))
def test_is_key_value_format_when_line_valid(line):
    line_parser = LineParser()
    assert line_parser.is_key_value_format(line)


@pytest.mark.parametrize('line', (' ',
                                  '',
                                  'box of oranges',
                                  'banana: five'))
def test_is_key_value_format_when_line_not_valid(line):
    line_parser = LineParser()
    assert not line_parser.is_key_value_format(line)


def test_split_on_stuff_and_count():
    line_parser = LineParser()
    assert ('apple', '10') == line_parser.split_on_stuff_and_count('apple: 10')


def test_add_or_update_storage():
    storage = Storage()

    storage.add_or_update('apple', 7)
    storage.add_or_update('orange', 2)
    storage.add_or_update('apple', 1)

    assert {'apple': 8, 'orange': 2} == storage.get_dict_storage()


def test_read_lines_when_filename_correct():
    file_reader = FileReader('fruits.txt')
    assert file_reader.read_lines()


@patch('builtins.print')
def test_read_lines_when_filename_wrong(mock_print):
    file_reader = FileReader('unknown_name.txt')

    file_reader.read_lines()

    mock_print.assert_called_once_with('Не найден файл: "unknown_name.txt"')


def test_stuff_counter():
    line_parser = LineParser()
    file_reader = FileReader('fruits.txt')
    fruit_storage = Storage()
    file_handler = FileManager(file_reader, line_parser, fruit_storage)

    file_handler.stuff_counter()

    assert {'apple': 7, 'banana': 9, 'grape': 7, 'orange': 3} == fruit_storage.get_dict_storage()


