class Storage:
    def __init__(self):
        self._dict_storage = {}

    def add_or_update(self, stuff, count):
        if stuff not in self._dict_storage:
            self._dict_storage[stuff] = count
        else:
            self._dict_storage[stuff] += count

    def get_dict_storage(self):
        return self._dict_storage
