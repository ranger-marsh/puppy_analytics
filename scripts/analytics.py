
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
    if len(weight_list) < 3:
        print(f'{weight_list[0]} does not have enough data to proceed.')
        return False
    return True


def daily_weight_gains(weight_list):
    weights = [float(day) for day in weight_list[1:]]
    gains = [round(day, 2) for day in np.diff(weights)]
    return gains


def daily_percent_gains(weight_list):
    gains = daily_weight_gains(weight_list)
    percentages = list()
    for index, gain in enumerate(gains):
        percentages.append(round((gain / float(weight_list[index + 1])) * 100, 2))
    return percentages


def main():
    pass


if __name__ == '__main__':
    main()
