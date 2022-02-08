#TODO: break into functions

import pandas as pd
from datetime import date

today = date.today()
# import from raw
KNS_PersonToPosition = pd.read_excel('..\..\data\\raw\KNS_PersonToPosition.xlsx')
KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]
# filter relevant records
in_government = [31, 39, 40, 45, 49, 50, 51, 57, 59, 65, 73]
in_coalition = [29, 30, 122, 123]
people_in_government = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin(in_government + in_coalition)]
# select relevant columns
people_in_government = people_in_government[['PersonID', 'PositionID', 'StartDate', 'FinishDate']]
# people_in_government = people_in_government[['PersonID', 'StartDate', 'FinishDate']]
# fill missing w/ today's date
people_in_government['FinishDate'].fillna(today, inplace=True)
# cast date columns to date
people_in_government['StartDate'] = pd.to_datetime(people_in_government['StartDate'])
people_in_government['FinishDate'] = pd.to_datetime(people_in_government['FinishDate'])

people_in_government_by_date = pd.DataFrame()
# expand dates
for row in (people_in_government.index):
    # print(people_in_government.loc[row])
    dates = pd.date_range(
        people_in_government.loc[row]['StartDate'],
        people_in_government.loc[row]['FinishDate'],
        closed='left')

    expanded_dates_batch = pd.DataFrame(index=dates)
    expanded_dates_batch.columns.name = 'Date'
    expanded_dates_batch['PersonID'] = people_in_government.loc[row]['PersonID']
    expanded_dates_batch['PositionID'] = people_in_government.loc[row]['PositionID']
    print(expanded_dates_batch)
    people_in_government_by_date = pd.concat([people_in_government_by_date, expanded_dates_batch])
people_in_government_by_date.to_excel(
    '..\..\data\\expanded\people_in_government_by_date.xlsx',
    sheet_name='people_in_government_by_date',
    header=True,
    index_label='Date'
    )

people_in_government_by_date