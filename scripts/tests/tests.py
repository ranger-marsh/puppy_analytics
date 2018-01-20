#!/usr/bin/env python3

"""
Test using pytest http://doc.pytest.org/en/latest/
Tests for analytics.py
"""

import analytics as A


def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_file_open():
    # Open file read to list.
    puppy_cict = A.open_text_file('testing_data/test_data.txt')
    
