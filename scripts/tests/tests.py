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
    assert puppy_list[0] == ['Puppy 1', '14', '15.2', '15.85', '17.55', '19.95', '20.5', '22.6', '24.05']
    assert puppy_list[1] == ['Puppy 2', '17.8', '19.1', '20', '22.45', '23.3', '24', '25.2', '26.4']
    assert puppy_list[2] == ['Puppy 3', '16.7', '18.25', '20.05', '21.9', '23.05', '24.85', '24.9', '28.95']
    assert puppy_list[3] == ['Puppy 4', '14.8', '15.9', '16.7', '19.25', '20.8', '22.45', '23.65', '26.05']
    assert puppy_list[4] == ['Puppy 5', '15.8', '18.15', '19.9', '21.4', '22.95', '24.93', '26.3', '30.25']
    assert puppy_list[5] == ['Puppy 6', '15.7', '17', '18.6', '19.1', '20.7', '22', '22.35', '23.6']
    assert puppy_list[6] == ['Puppy 7', '12.7', '14.05', '16', '17.05', '18.75', '21.05', '22', '24.25']
    assert puppy_list[7] == ['Puppy 8', '15.7', '17.4', '19.2', '19.8', '20.65', '22.6', '23.75', '25.85']
    assert puppy_list[8] == ['Puppy 9', '15.9', '18', '19.95', '21.25', '22.1', '22.1', '24.25', '26.4']


def test_check_data():
    short = ['Puppy 1', '14']
    enough = ['Puppy 1', '14', '15']
    assert A.check_data(short) == False
    assert A.check_data(enough) == True


def daily_weight_gains():
    puppy1 = ['Puppy 1', '14', '15.2', '15.85', '17.55', '19.95', '20.5', '22.6', '24.05']
    puppy9 = ['Puppy 9', '15.9', '18', '19.95', '21.25', '22.1', '22.1', '24.25', '26.4']
    assert A.daily_weight_gains(puppy1) == [.9, .65, 1.7, 2.4, .55, 2.1, 1.45]
    assert A.daily_weight_gains(puppy9) == [.2, 1.95, 1.3, .85, 0, 2.15, 2.15]


def test_daily_percent_gains():
    puppy2 = ['Puppy 2', '17.8', '19.1', '20', '22.45', '23.3', '24', '25.2', '26.4']
    assert A.daily_percent_gains(puppy2) == [7.3, 4.71, 12.25, 3.79, 3.0, 5.0, 4.76]


def test_total_weight_gains():
    puppy3 = ['Puppy 3', '16.7', '18.25', '20.05', '21.9', '23.05', '24.85', '24.9', '28.95']
    assert A.total_weight_gains(puppy3) == [1.55, 3.35, 5.2, 6.35, 8.15, 8.2, 12.25]


def test_total_percent_gains():
    puppy4 = ['Puppy 4', '14.8', '15.9', '16.7', '19.25', '20.8', '22.45', '23.65', '26.05']
    assert A.total_percent_gains(puppy4) == [7.43, 12.84, 30.07, 40.54, 51.69, 59.80, 76.01]


def test_average_daily_gains():
    puppy6 = ['Puppy 6', '15.7', '17', '18.6', '19.1', '20.7', '22', '22.35', '23.6']
    assert A.average_daily_gains(puppy6) == 1.13


def test_average_percent_gains():
    puppy5 = ['Puppy 5', '15.8', '18.15', '19.9', '21.4', '22.95', '24.93', '26.3', '30.25']
    assert A.average_percent_gains(puppy5) == 9.78


def test_days_to_double():
    puppy6 = ['Puppy 6', '15.7', '17', '18.6', '19.1', '20.7', '22', '22.35', '23.6']
    assert A.days_to_double(puppy6) == 13.89


def test_projected_weight():
    puppy6 = ['Puppy 6', '15.7', '17', '18.6', '19.1', '20.7', '22', '22.35', '23.6']
    assert A.projected_weight(puppy6, 7) == 23.61
    assert A.projected_weight(puppy6, 5.5) == 21.92


def test_expected_daily_gain():
    assert A.expected_daily_gain(65.0) == 3.44


def test_rank_days_to_double():
    litter = A.open_csv('testing_data/test_data.csv')
    assert A.rank_days_to_double(litter) == [['Puppy 2', 14.47],
                                             ['Puppy 6', 13.89],
                                             ['Puppy 8', 10.83],
                                             ['Puppy 9', 10.6],
                                             ['Puppy 1', 9.72],
                                             ['Puppy 3', 9.54],
                                             ['Puppy 4', 9.19],
                                             ['Puppy 7', 7.7],
                                             ['Puppy 5', 7.67]]


def test_rank_average_percent_weight_gain():
    litter = A.open_csv('testing_data/test_data.csv')
    assert A.rank_average_percent_weight_gain(litter) == [['Puppy 2', 5.83],
                                                          ['Puppy 6', 6.03],
                                                          ['Puppy 8', 7.42],
                                                          ['Puppy 9', 7.59],
                                                          ['Puppy 1', 8.1],
                                                          ['Puppy 3', 8.27],
                                                          ['Puppy 4', 8.46],
                                                          ['Puppy 7', 9.72],
                                                          ['Puppy 5', 9.78]]


def test_rank_percent_gained_one_day():
    litter = A.open_csv('testing_data/test_data.csv')
    assert A.rank_percent_gained_one_day(litter) == [['Puppy 2', 4.76],
                                                     ['Puppy 6', 5.59],
                                                     ['Puppy 1', 6.42],
                                                     ['Puppy 8', 8.84],
                                                     ['Puppy 9', 8.87],
                                                     ['Puppy 4', 10.15],
                                                     ['Puppy 7', 10.23],
                                                     ['Puppy 5', 15.02],
                                                     ['Puppy 3', 16.27]]
