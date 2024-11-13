"""
Ожидается, что после обработки файла 'data.txt' на консоль будут выведены следующие строки:

Итог по всем покупкам:
apple: 13
banana: 7
grape: 6

"""


class data_processor:

    def __init__(self, filename):
        self.name = filename

    def processData(self):
        res = {}
        file = open(self.name)
        f = [i for i in file]
        for i in range(len(f)):
            s = f[i].strip()
            if type(s) == str:
                s_list = s.split(':')
                x = []
                x.append(s_list[0])
                x.append(s_list[1])
                key = x[0]
                value = int(x[1])
                if key in res.keys():
                    for exist_key, exist_value in res.items():
                        if key == exist_key:
                            res[key] = exist_value + value
                else:
                    res.update({key: value})
        print("Итог по всем покупкам:")
        print(res)


processor = data_processor('data.txt')
processor.processData()