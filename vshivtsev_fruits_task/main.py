from file_handler import FileManager
from file_reader import FileReader
from line_parser import LineParser
from storage import Storage


if __name__ == "__main__":
    file_reader = FileReader('fruits.txt')
    line_parser = LineParser()
    fruit_storage = Storage()
    file_handler = FileManager(file_reader, line_parser, fruit_storage)

    file_handler.stuff_counter()

    print(fruit_storage.get_dict_storage())
