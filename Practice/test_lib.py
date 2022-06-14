
from lib import *

def test_average():
    input1 = [11, -11, 10, 20]
    expected_result = 7.5
    actual_result = average(input1)

    assert expected_result == actual_result


def test_minimum():
    input1 = [11, -11, 10, 20]
    expected_result = -11

    actual_result = minimum(input1)
    assert expected_result == actual_result

test_average()

test_minimum()