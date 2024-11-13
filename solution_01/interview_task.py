"""
Ожидается, что после обработки файла 'data.txt' на консоль будут выведены следующие строки:

Итог по всем покупкам:
apple: 13
banana: 7
grape: 6

"""


class DataProcessor:

    def process_file(self, file_name):
        file = open(file_name)
        file_as_text_lines = [i for i in file]
        result = self._calculate_result(file_as_text_lines)
        print("Итог по всем покупкам:")
        for key, value in result.items():
            print(f'{key}: {value}')

    def _calculate_result(self, file_as_text_lines):
        result = {}
        for text_line in file_as_text_lines:
            if not self._is_text_line_correct(text_line):
                continue
            key, value = self._convert_text_line_to_key_value_pair(text_line)
            self._add_data_to_result(key, value, result)
        return result

    @staticmethod
    def _is_text_line_correct(text_line):
        pair = text_line.split(':')
        if len(pair) != 2:
            return False
        value_as_string = pair[1].strip()
        if not value_as_string.isdigit():
            return False
        return True

    @staticmethod
    def _convert_text_line_to_key_value_pair(text_line):
        pair = text_line.split(':')
        key = pair[0].strip()
        value = int(pair[1].strip())
        return key, value

    @staticmethod
    def _add_data_to_result(key, value, result):
        if key in result.keys():
            for exist_key, exist_value in result.items():
                if key == exist_key:
                    result[key] = exist_value + value
        else:
            result.update({key: value})


if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_file('data_correct.txt')