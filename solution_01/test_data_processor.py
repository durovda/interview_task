from solution_01.interview_task import DataProcessor


def test_calculate_results():
    file_as_text_lines = [
        'apple:  10',
        'banana: 5',
        'orange: три',
        'grape:  двадцать три',
        '',
        'apple : 3',
        'banana: 2',
        'box of oranges',
        'grape : 6'
    ]

    expected_result = {
        'apple': 13,
        'banana': 7,
        'grape': 6,
    }

    processor = DataProcessor()
    actual_result = processor._calculate_result(file_as_text_lines)

    assert actual_result == expected_result


def test_calculate_results_when_data_is_correct():
    file_as_text_lines = [
        'apple: 10',
        'banana: 5',
        'apple: 3',
    ]

    expected_result = {
        'apple': 13,
        'banana': 5,
    }

    processor = DataProcessor()
    actual_result = processor._calculate_result(file_as_text_lines)

    assert actual_result == expected_result


def test_calculate_results_when_number_written_in_words():
    file_as_text_lines = [
        'apple: 10',
        'banana: пять',
    ]

    expected_result = {
        'apple': 10,
    }

    processor = DataProcessor()
    actual_result = processor._calculate_result(file_as_text_lines)

    assert actual_result == expected_result


def test_is_text_line_correct():
    processor = DataProcessor()
    assert processor._is_text_line_correct('apple: 10')


def test_is_text_line_not_correct():
    processor = DataProcessor()
    assert not processor._is_text_line_correct('')
    assert not processor._is_text_line_correct('box of oranges')


def test_convert_text_line_to_key_value_pair():
    processor = DataProcessor()
    key, value = processor._convert_text_line_to_key_value_pair('apple: 10')
    assert key == 'apple' and value == 10
    key, value = processor._convert_text_line_to_key_value_pair(' apple :  10 ')
    assert key == 'apple' and value == 10


def test_add_data_to_result_when_adding_item():
    processor = DataProcessor()
    result = {'apple': 13}
    processor._add_data_to_result(key='banana', value=5, result=result)
    assert result == {'apple': 13, 'banana': 5}


def test_add_data_to_result_when_updating_item():
    processor = DataProcessor()
    result = {'apple': 10}
    processor._add_data_to_result('apple', 3, result)
    assert result == {'apple': 13}
