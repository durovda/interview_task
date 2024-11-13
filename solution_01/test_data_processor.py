from solution_01.interview_task import DataProcessor


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


def test_calculate_results():
    file_as_text_lines = [
        'apple:  10',
        'banana: 5',
        'orange: три',
        'grape:  два',
        '',
        'apple:  3',
        'banana: 2',
        'box of oranges',
        'grape:  6'
    ]

    expected_result = {
        'apple': 13,
        'banana': 7,
        'grape': 6,
    }

    processor = DataProcessor()
    actual_result = processor._calculate_result(file_as_text_lines)

    assert actual_result == expected_result

