import pandas as pd


items = ['Apples, Early Yellow Transparent', 'Apples, Gala', 'Apples, Gold Rush','Apples, Red Rome Beauty', 'Apples, Spice', 'Basil, Fresh - Sweet Genovese (green)','Beets, Without Greens', 'Collards', 'Garlic Scapes', 'Jerusalem Artichokes','Lettuce, Head', 'Lettuce, Loose Leaf Green', 'Microgreens, Sunshine Mix','Okra, Green', 'Peppers, Bell (Green)', 'Peppers, Jalapeno', 'Pumpkin, Seminole','Rosemary, Fresh', 'Sweet Potatoes, Orange', 'Watermelon, Jubilee']


def myhash(user_name):
    import hashlib
    m = hashlib.sha256()
    m.update(bytes(user_name, 'utf-8'))
    return int(m.hexdigest()[:16], 16)


user_name = 'sterckxmj'
item = items[myhash(user_name) % len(items)]
print(f'{user_name} cleans subcategory {item}')


# def clean(subcategory, unit, units_sold):
#     if subcategory == 'Apples, Red Rome Beauty':
#         if unit == '1/4 Peck':
#             return unit, units_sold
#         elif unit == 'Peck':
#             return '1/4 Peck', str(int(units_sold) * 4)
#         elif unit == 'Bushel':
#             return '1/4 Peck', str(int(units_sold) * 16)
#     else:
#         return unit, units_sold
def clean(row):
    if row['SubCategory'] == 'Apples, Red Rome Beauty':
        if row['Unit'] == '1/4 Peck':
            return row
        elif row['Unit'] == 'Peck':
            row['Unit'] = '1/4 Peck'
            row['Units Sold'] = str(int(row['Units Sold']) * 4)
            return row
        elif row['Unit'] == 'Bushel':
            row['Unit'] = '1/4 Peck'
            row['Units Sold'] = str(int(row['Units Sold']) * 16)
            return row
    else:
        return row


def main():
    df = pd.read_csv('food.csv')
    df = df.apply(clean, axis=1)
    df.to_csv('cleaned_produce.csv')


if __name__ == '__main__':
    main()
