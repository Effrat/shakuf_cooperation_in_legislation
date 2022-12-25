import pandas as pd
from datetime import date


# def members_of_knesset_by_date():
#     """
#     Creates members_of_knesset_by_date table from KNS_PersonToPosition by expanding dates.
#     """
today = date.today()

# ----- load -----
KNS_PersonToPosition = pd.read_excel('../../data/raw/KNS_PersonToPosition.xlsx')

# ----- transform -----
KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]
members_of_knesset = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin([43, 61])] # member of knesset
members_of_knesset = members_of_knesset[['PersonID', 'StartDate', 'FinishDate', 'KnessetNum']]
# members_of_knesset['FinishDate'].fillna(today, inplace=True)
# members_of_knesset['StartDate'] = pd.to_datetime(members_of_knesset['StartDate'])
# members_of_knesset['FinishDate'] = pd.to_datetime(members_of_knesset['FinishDate'])
# members_of_knesset.sort_values('FinishDate', inplace=True)
members_of_knesset = members_of_knesset[members_of_knesset['KnessetNum'] == 24]

for person_id in members_of_knesset['PersonID'].values:
    df = members_of_knesset[members_of_knesset['PersonID'] == person_id]
    if len(df) > 1:
        print(person_id)
        print(df.iloc[0]['FinishDate'])
        print(df.iloc[1]['StartDate'])
        print('\n')

# members_of_knesset

# members_of_knesset_by_date = pd.DataFrame()

# # ----- expand dates -----
# for row in (members_of_knesset.index):
#     dates = pd.date_range(
#         members_of_knesset.loc[row]['StartDate'],
#         members_of_knesset.loc[row]['FinishDate'],
#         closed='left')
#     expanded_dates_batch = pd.DataFrame(index=dates)
#     expanded_dates_batch['person_id'] = members_of_knesset.loc[row]['PersonID']
#     expanded_dates_batch['knesset_num'] = members_of_knesset.loc[row]['KnessetNum']
#     members_of_knesset_by_date = pd.concat(
#         [members_of_knesset_by_date, expanded_dates_batch])

# members_of_knesset_by_date.reset_index(inplace=True)
# members_of_knesset_by_date.rename(columns={'index': 'date'}, inplace=True)
# members_of_knesset_by_date['knesset_num'] = members_of_knesset_by_date['knesset_num'].astype(int)
# members_of_knesset_by_date[members_of_knesset_by_date['person_id'] == 30662]


# # ----- save -----
# members_of_knesset_by_date.to_csv(
#     '../../data/transformed/members_of_knesset_by_date.csv', index=False)