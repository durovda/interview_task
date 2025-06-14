from utils import is_valid_string


class LineParser:

    def is_key_value_format(self, line):
        return is_valid_string("^\s*\w+\s*:\s*-?\d+\s*?$", line)

    def split_on_stuff_and_count(self, line):
        stuff, count = map(str.strip, line.strip().split(':'))
        return stuff, count
