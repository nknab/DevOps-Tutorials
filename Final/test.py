'''
File: test.py
Project: Final
File Created: Tuesday, 14th June 2022 10:17:30 AM
Author: nknab
Email: adverb_rushed_09@icloud.com
Version: 1.0
Brief: Unit testing the various function is the main.
-----
Last Modified: Tuesday, 14th June 2022 10:20:50 AM
Modified By: nknab
-----
Copyright ©2022 nknab
'''

from main import *

def test_count_char():
    """
    Test the count_char() function
    """
    input1, input2 = "Bonjour&", "bonjour"
    expected1, expected2 = 8, 7

    result1 = count_char(input1)
    result2 = count_char(input2)

    assert expected1 == result1
    assert expected2 == result2

def test_ck_maj():
    """
    Test the chk_maj() function
    """
    input1, input2 = "Bonjour&", "bonjour"
    expected1, expected2 = True, False

    result1 = chk_maj(input1)
    result2 = chk_maj(input2)

    assert expected1 == result1
    assert expected2 == result2

def test_chk_special():
    """
    Test the chk_special() function
    """
    input1, input2 = "Bonjour&", "Bonjour"
    expected1, expected2 = True, False

    result1 = chk_special(input1)
    result2 = chk_special(input2)

    assert expected1 == result1
    assert expected2 == result2

def test_chk_valid():
    """
    Test the chk_valid() function
    """
    input1, input2, input3 = "C8h-N7ULBZZPUa-c!WDuRuqsr", "bkasdjhas", "dsfs"
    expected1, expected2, expected3 = True, False, False

    result1 = chk_valid(input1)
    result2 = chk_valid(input2)
    result3 = chk_valid(input3)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3
