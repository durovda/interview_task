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
            if type(text_line) == str:
                s_list = text_line.split(':')
                x = []
                x.append(s_list[0])
                x.append(s_list[1])
                key = x[0]
                value = int(x[1])
                if key in result.keys():
                    for exist_key, exist_value in result.items():
                        if key == exist_key:
                            result[key] = exist_value + value
                else:
                    result.update({key: value})
        return result


if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_file('data_correct.txt')