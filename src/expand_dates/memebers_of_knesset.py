import pandas as pd
from datetime import date

today = date.today()

KNS_PersonToPosition = pd.read_excel('..\..\data\\raw\KNS_PersonToPosition.xlsx')
KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]
members_of_knesset = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin([43, 61])]
members_of_knesset = members_of_knesset[['PersonID', 'StartDate', 'FinishDate']]
members_of_knesset['FinishDate'].fillna(today, inplace=True)
members_of_knesset['StartDate'] = pd.to_datetime(members_of_knesset['StartDate'])
members_of_knesset['FinishDate'] = pd.to_datetime(members_of_knesset['FinishDate'])
members_of_knesset.sort_values('FinishDate', inplace=True)
members_of_knesset

members_of_knesset_by_date = pd.DataFrame()

for row in (members_of_knesset.index):
    # print(members_of_knesset.loc[row])
    dates = pd.date_range(
        members_of_knesset.loc[row]['StartDate'],
        members_of_knesset.loc[row]['FinishDate'],
        closed='left')

    expanded_dates_batch = pd.DataFrame(index=dates)
    expanded_dates_batch['PersonID'] = members_of_knesset.loc[row]['PersonID']
    expanded_dates_batch.columns.name = 'Date'
    print(expanded_dates_batch)
    members_of_knesset_by_date = pd.concat([members_of_knesset_by_date, expanded_dates_batch])

members_of_knesset_by_date.to_csv(
    '..\..\data\\expanded\members_of_knesset_by_date.csv',
    index_label='Date'
    )

