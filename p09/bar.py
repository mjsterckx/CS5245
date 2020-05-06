# Author: Matthias Sterckx
# Additional credit features: Compute expected month of sale and display; Use the names of the months on the x-axis
# Resources used: Matplotlib documentation; Pandas documentation

import pandas as pd
import matplotlib.pyplot as plt


months = {}
month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
               7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
month_names_full = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
                    'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
                    'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'}


def extract(row):
    if row['Month Sold'][3:6] not in months.keys():
        months[row['Month Sold'][3:6]] = 0
    months[row['Month Sold'][3:6]] += float(row['Units Sold'])


def calculate_average(month, units):
    numerator = 0
    denominator = 0
    for i in range(len(month)):
        numerator += month[i] * units[i]
        denominator += units[i]
    if numerator == 0:
        return 0
    return round((numerator / denominator), 2)


def main():
    df = pd.read_csv('food_cleaned.csv')
    category = input('Enter SubCategory: ')
    df = df[df['Month Sold'].str.contains('19')]
    df = df[df['SubCategory'] == category]
    unit = df['Unit'].iloc[0]
    df.apply(extract, axis=1)
    keys = []
    values = []
    month_numbers = []
    for i in range(1, 13):
        if month_names[i] in months.keys() and months[month_names[i]] > 0:
            keys.append(month_names_full[month_names[i]])
            values.append(months[month_names[i]])
            month_numbers.append(i)
    average = calculate_average(month_numbers, values)
    plt.bar(keys, values)
    plt.xlabel('Month (Average = ' + str(average) + ')')
    plt.ylabel('Units Sold')
    plt.title(unit + 's of ' + category)
    plt.savefig(''.join(e for e in category if e.isalnum()) + '.png')


if __name__ == '__main__':
    main()
