import pandas as pd
from datetime import date


def people_in_government_by_date():
    """
    Creates people_in_government_by_date table from KNS_PersonToPosition.
    """
    today = date.today()
    KNS_PersonToPosition = pd.read_excel('../data/raw/KNS_PersonToPosition.xlsx')
    KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]
    # assumption: factions with at least one member in a government job are factions in the coalition or head of coalition.
    in_government = [31, 39, 40, 45, 49, 50, 51, 57, 59, 65, 73]
    coalition_or_knesset_chairman = [29, 30, 122, 123, 285078]
    people_in_government = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin(in_government + coalition_chairman)]
    people_in_government = people_in_government[['PersonID', 'PositionID', 'StartDate', 'FinishDate']]
    people_in_government['FinishDate'].fillna(today, inplace=True)
    people_in_government['StartDate'] = pd.to_datetime(people_in_government['StartDate'])
    people_in_government['FinishDate'] = pd.to_datetime(people_in_government['FinishDate'])

    people_in_government_by_date = pd.DataFrame()
    # expand dates
    for row in (people_in_government.index):
        dates = pd.date_range(
            people_in_government.loc[row]['StartDate'],
            people_in_government.loc[row]['FinishDate'],
            closed='left')

        expanded_dates_batch = pd.DataFrame(index=dates)
        expanded_dates_batch.columns.name = 'Date'
        expanded_dates_batch['PersonID'] = people_in_government.loc[row]['PersonID']
        print(expanded_dates_batch)
        people_in_government_by_date = pd.concat([people_in_government_by_date, expanded_dates_batch])
    people_in_government_by_date.reset_index(inplace=True)
    people_in_government_by_date.columns = ['date', 'person_id']

    people_in_government_by_date.to_excel(
        '../data/transformed/people_in_government_by_date.xlsx',
        sheet_name='people_in_government_by_date',
        header=True,
        index=False
        )

    people_in_government_by_date