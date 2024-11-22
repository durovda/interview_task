"""
Ожидается, что после обработки файла 'data.txt' на консоль будут выведены следующие строки:

Итог по всем покупкам:
apple: 13
banana: 7
grape: 6

"""


class DataProcessor:

    @staticmethod
    def process_file(file_name):
        result = {}
        with open(file_name) as file_with_text_lines:
            for text_line in file_with_text_lines:
                pair = text_line.split(':')
                if len(pair) != 2:
                    continue
                key = pair[0].strip()
                value_as_string = pair[1].strip()
                if not value_as_string.isdigit():
                    continue
                value = int(value_as_string)
                if key in result.keys():
                    result[key] += value
                else:
                    result.update({key: value})
        print("Итог по всем покупкам:")
        for key, value in result.items():
            print(f'{key}: {value}')


if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_file('data.txt')