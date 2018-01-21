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
    puppy_list = A.open_csv('testing_data/test_data.csv')
    assert puppy_list[0] == ['Puppy 1', '14', '14.9', '15.2', '15.85', '17.55', '19.95', '20.5', '22.6', '24.05']
    assert puppy_list[1] == ['Puppy 2', '17.8', '18.4', '19.1', '20', '22.45', '23.3', '24', '25.2', '26.4']
    assert puppy_list[2] == ['Puppy 3', '16.7', '17.3', '18.25', '20.05', '21.9', '23.05', '24.85', '24.9', '28.95']
    assert puppy_list[3] == ['Puppy 4', '14.8', '14.8', '15.9', '16.7', '19.25', '20.8', '22.45', '23.65', '26.05']
    assert puppy_list[4] == ['Puppy 5', '15.8', '16.7', '18.15', '19.9', '21.4', '22.95', '24.93', '26.3', '30.25']
    assert puppy_list[5] == ['Puppy 6', '15.7', '15.83', '17', '18.6', '19.1', '20.7', '22', '22.35', '23.6']
    assert puppy_list[6] == ['Puppy 7', '12.7', '13.3', '14.05', '16', '17.05', '18.75', '21.05', '22', '24.25']
    assert puppy_list[7] == ['Puppy 8', '15.7', '16.3', '17.4', '19.2', '19.8', '20.65', '22.6', '23.75', '25.85']
    assert puppy_list[8] == ['Puppy 9', '15.9', '16.1', '18', '19.95', '21.25', '22.1', '22.1', '24.25', '26.4']


def test_check_data():
    short = ['Puppy 1', '14']
    enough = ['Puppy 1', '14', '15']
    assert A.check_data(short) == False
    assert A.check_data(enough) == True


def daily_weight_gains():
    puppy1 = ['Puppy 1', '14', '14.9', '15.2', '15.85', '17.55', '19.95', '20.5', '22.6', '24.05']
    puppy9 = ['Puppy 9', '15.9', '16.1', '18', '19.95', '21.25', '22.1', '22.1', '24.25', '26.4']
    assert A.daily_weight_gains(puppy1) == [.9, .3, .65, 1.7, 2.4, .55, 2.1, 1.45]
    assert A.daily_weight_gains(puppy9) == [.2, 1.9, 1.95, 1.3, .85, 0, 2.15, 2.15]


def test_daily_percent_gains():
    puppy2 = ['Puppy 2', '17.8', '18.4', '19.1', '20', '22.45', '23.3', '24', '25.2', '26.4']
    assert A.daily_percent_gains(puppy2) == [3.37, 3.80, 4.71, 12.25, 3.79, 3.0, 5.0, 4.76]
