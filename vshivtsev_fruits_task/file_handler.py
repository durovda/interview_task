from utils import str_to_int


class FileManager:
    def __init__(self, file_reader, line_parser, storage):
        self._file_reader = file_reader
        self._line_parser = line_parser
        self._storage = storage

    def stuff_counter(self):
        lines = self._file_reader.read_lines()
        for line in lines:
            if self._line_parser.is_key_value_format(line):
                stuff, count = self._line_parser.split_on_stuff_and_count(line)
                count = str_to_int(count)
                self._storage.add_or_update(stuff, count)
