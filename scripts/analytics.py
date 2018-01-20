
#!/usr/bin/env python3
import csv


def open_csv(path):
        # Open the CSV file and return a list of list. each nested list is for a
        # puppy and weights.
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the headers
        return list(reader)


def one_day(puppy_list):
    if len(puppy_list) < 3:
        print('Not enough data for one day gains')
        return None
    return(round(float(puppy_list[-1]) - float(puppy_list[-2]), 2))


def two_day(puppy_list):
    if len(puppy_list) < 4:
        print('Not enough data for one day gains')
        return None
    return(round(float(puppy_list[-1]) - float(puppy_list[-3]), 2))


def three_day(puppy_list):
    if len(puppy_list) < 5:
        print('Not enough data for one day gains')
        return None
    return(round(float(puppy_list[-1]) - float(puppy_list[-4]), 2))


def four_day(puppy_list):
    if len(puppy_list) < 6:
        print('Not enough data for one day gains')
        return None
    return(round(float(puppy_list[-1]) - float(puppy_list[-5]), 2))


def five_day(puppy_list):
    if len(puppy_list) < 7:
        print('Not enough data for one day gains')
        return None
    return(round(float(puppy_list[-1]) - float(puppy_list[-6]), 2))


def main():
    pass


if __name__ == '__main__':
    main()
