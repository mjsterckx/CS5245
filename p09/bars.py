# Author: Matthias Sterckx
# Additional credit features: Show average purchase month; Sort subcategories by average purchase month
# Resources used: Matplotlib documentation; Pandas documentation

import pandas as pd
import matplotlib.pyplot as plt

subcategories = {}
month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
               7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


def extract(row):
    if row['SubCategory'] not in subcategories.keys():
        subcategories[row['SubCategory']] = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
                                             'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}
    months = subcategories[row['SubCategory']]
    months[row['Month Sold'][3:6]] += float(row['Units Sold'])
    row['SubCategory'] = months


def calculate_average(units):
    numerator = 0
    denominator = 0
    for i in range(1, 13):
        numerator += i * units[i - 1]
        denominator += units[i - 1]
    if numerator == 0:
        return 0
    return round((numerator / denominator), 2)


def main():
    df = pd.read_csv('food_cleaned.csv')
    category = input('Keep subcategories that start with: ')
    df = df[df['Month Sold'].str.contains('19')]
    df = df[df['SubCategory'].str.match(category)]
    df.apply(extract, axis=1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    averages = []
    averages_month = []
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for c in subcategories.keys():
        values = []
        for i in range(1, 13):
            values.append(subcategories[c][month_names[i]])
        average = calculate_average(values)
        averages.append(average)
        averages_month.append(c)
        subcategories[c]['average'] = average
    averages_month_sorted = [x for _, x in sorted(zip(averages, averages_month), key=lambda pair: pair[0])]
    p = 0
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    for c in averages_month_sorted:
        months = subcategories[c]
        values = []
        for i in range(1, 13):
            values.append(months[month_names[i]])
        ax1 = fig.add_subplot(len(averages_month_sorted), 1, 1 + p)
        ax1.bar(month_numbers, values, color=colors[p % len(colors)])
        ax1.get_yaxis().set_ticks([])
        ax1.set_ylim([0, sum(values)])
        ax1.text(0, 0, c + ' (' + str(subcategories[c]['average']) + ')')
        ax1.axis('off')
        p += 1
    x_ticks = ['', '', '2', '', '4', '', '6', '', '8', '', '10', '', '12', '']
    y_ticks = list(map(str, list(range(len(averages_month_sorted))))) + ['']
    ax.set_xticks(range(14))
    ax.set_xticklabels(x_ticks)
    ax.set_yticks(range(len(averages_month_sorted) + 1))
    ax.set_yticklabels(y_ticks)
    fig.subplots_adjust(hspace=0)
    ax.set_xlabel('Month')
    ax.set_ylabel('Normalized Counts')
    plt.savefig(''.join(e for e in category if e.isalnum()) + '.png')


if __name__ == '__main__':
    main()
