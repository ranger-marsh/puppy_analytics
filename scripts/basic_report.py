import analytics as A


def main():
    with open('basic.txt', 'w+') as report:
        litter = A.open_csv('tests/testing_data/test_data.csv')

        report.write('Ranked Days to Double\n')
        for rank in A.rank_days_to_double(litter):
            report.write(f'{rank[0]} : {rank[1]}\n')

        report.write('\nRanked Percent Weight Gained\n')
        for rank in A.rank_average_percent_weight_gain(litter):
            report.write(f'{rank[0]} : %{rank[1]}\n')

        report.write('\nRanked Percent Weight Gained Since Last Weigh-in\n')
        for rank in A.rank_percent_gained_one_day(litter):
            report.write(f'{rank[0]} : %{rank[1]}\n')


if __name__ == "__main__":
    main()
