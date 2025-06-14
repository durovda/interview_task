class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_lines(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError as error:
            print(f'Не найден файл: "{error.filename}"')
            return []
