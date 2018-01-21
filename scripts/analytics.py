
#!/usr/bin/env python3
import csv
import numpy as np


def open_csv(path):
        # Open the CSV file and return a list of list. each nested list is for a
        # puppy and weights.
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the headers
        return list(reader)


def check_data(weight_list):
    # Check that a puppy as at least two recorded weights.
    if len(weight_list) < 3:
        print(f'{weight_list[0]} does not have enough data to proceed.')
        return False
    return True


def daily_weight_gains(weight_list):
    # Return a list of weight gain compared from the previous day.
    weights = [float(day) for day in weight_list[1:]]
    gains = [round(day, 2) for day in np.diff(weights)]
    return gains


def daily_percent_gains(weight_list):
    # Percent gained daily.
    gains = daily_weight_gains(weight_list)
    percentages = list()
    for index, gain in enumerate(gains, 1):
        percentages.append(round((gain / float(weight_list[index])) * 100, 2))
    return percentages


def total_weight_gains(weight_list):
    # Total weight gain
    gains = [round(float(day) - float(weight_list[1]), 2) for day in weight_list[2:]]
    return gains


def total_percent_gains(weight_list):
    # Toal percent gained.
    percentages = [round(((float(day) / float(weight_list[1]) * 100) - 100), 2) for day in weight_list[2:]]
    return percentages


def average_daily_gains(weight_list):
    average = round(np.mean(daily_weight_gains(weight_list)), 2)
    return average


def average_percent_gains(weight_list):
    average = round(np.mean(daily_percent_gains(weight_list)), 2)
    return average


def days_to_double(weight_list):
    days = round(float(weight_list[1]) / average_daily_gains(weight_list), 2)
    return days


def projected_weight(weight_list, days_to_project):
    projection = round((average_daily_gains(weight_list) * days_to_project) + float(weight_list[1]), 2)
    return projection


def expected_daily_gain(dam_weight):
    # Expect daily gain based on 1.5G per pound of dam weight per day.
    expected = round(dam_weight * 0.0529109, 2)  # 1.5 Grams in ounces.
    return expected


def main():
    pass


if __name__ == '__main__':
    main()
