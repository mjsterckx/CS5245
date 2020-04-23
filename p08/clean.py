import pandas as pd
import string
import re
from city_name_map import city_name_map


def clean_city(city):
    if isinstance(city, str):
        city = city.strip()
        city = re.sub(r'\s+', ' ', city)
        city = city.title()
        city = re.sub(',.*$', '', city)
        if city.endswith(' Nc'):
            city = city[:-3]
        if city in city_name_map.keys():
            city = city_name_map[city]
    return city


def clean_state(state):
    if isinstance(state, str):
        state = state.upper()
        if state == 'NO':
            state = 'NC'
    return state


def clean_zip_code(zip_code):
    if isinstance(zip_code, str):
        zip_code = re.sub('[^0-9]', '', str(zip_code))
        zip_code = str(zip_code)[:5]
        if len(zip_code) < 5:
            zip_code = float('nan')
    return float(zip_code)


def main():
    df_person = pd.read_csv('basic_person.csv', index_col='acct_id_new')
    df_person['city'] = df_person['city'].apply(clean_city)
    df_person['state'] = df_person['state'].apply(clean_state)
    df_person['zip'] = df_person['zip'].apply(clean_zip_code)
    df_person.to_csv('cleaned.csv')


if __name__ == '__main__':
    main()
