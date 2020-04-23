import pandas as pd


def main():
    df_person = pd.read_csv('basic_person.csv')
    df_student = pd.read_csv('person_detail_f.csv')
    df_map = pd.read_csv('student_detail_v.csv')
    joined = df_map.groupby(['acct_id_new'], as_index=False).max().groupby(['student_id_new'], as_index=False).max()
    joined = joined.join(df_student.set_index('person_detail_id_new'), on='person_detail_id_new')
    joined = joined.join(df_person.set_index('acct_id_new'), on='acct_id_new')
    joined.set_index('student_id_new')
    joined.to_csv('joined.csv', index=False)


if __name__ == '__main__':
    main()
