import re


def str_to_int(string):
    return int(string)


def is_valid_string(re_pattern, line):
    return re.search(re_pattern, line)
