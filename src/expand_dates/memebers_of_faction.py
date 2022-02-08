#TODO: break into functions

import pandas as pd
from datetime import date

today = date.today()

KNS_PersonToPosition = pd.read_excel('..\..\data\\raw\KNS_PersonToPosition.xlsx')
KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]
members_of_faction = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin([48, 54])]
members_of_faction = members_of_faction[['PersonID', 'FactionID', 'StartDate', 'FinishDate']]
members_of_faction['FinishDate'].fillna(today, inplace=True)
members_of_faction['StartDate'] = pd.to_datetime(members_of_faction['StartDate'])
members_of_faction['FinishDate'] = pd.to_datetime(members_of_faction['FinishDate'])
# members_of_faction.sort_values('FinishDate', inplace=True, ascending=False)

members_of_faction_by_date = pd.DataFrame()

for row in (members_of_faction.sort_values('FinishDate', ascending=False).index):
    # print(members_of_faction.loc[row])
    dates = pd.date_range(
        members_of_faction.loc[row]['StartDate'],
        members_of_faction.loc[row]['FinishDate'],
        closed='left')

    expanded_dates_batch = pd.DataFrame(index=dates)
    expanded_dates_batch['PersonID'] = members_of_faction.loc[row]['PersonID']
    expanded_dates_batch['FactionID'] = int(members_of_faction.loc[row]['FactionID'])
    print(expanded_dates_batch)
    members_of_faction_by_date = pd.concat([members_of_faction_by_date, expanded_dates_batch])

members_of_faction_by_date.columns.name = 'Date'
members_of_faction_by_date.to_csv(f'..\..\data\\expanded\members_of_faction_by_date.csv', index_label='Date')

members_of_faction_by_date