import pandas as pd
from datetime import date


def members_of_faction_by_date():
    """
    Creates members_of_faction_by_date table from KNS_PersonToPosition.
    """
    today = date.today()

    KNS_PersonToPosition = pd.read_excel('../data/raw/KNS_PersonToPosition.xlsx')
    KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]
    members_of_faction = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin([48, 54])]
    members_of_faction = members_of_faction[['PersonID', 'FactionID', 'StartDate', 'FinishDate']]
    members_of_faction['FinishDate'].fillna(today, inplace=True)
    members_of_faction['StartDate'] = pd.to_datetime(members_of_faction['StartDate'])
    members_of_faction['FinishDate'] = pd.to_datetime(members_of_faction['FinishDate'])
    members_of_faction.sort_values('FinishDate', inplace=True, ascending=False)


    # missing records to be added
    manual_data_fillers = pd.DataFrame([
        # {'PersonID': 23631, 'FactionID': 967, 'Date': '2021-06-23'},
        # {'PersonID': 23631, 'FactionID': 967, 'Date': '2021-06-24'},
        # {'PersonID': 23673, 'FactionID': 963, 'Date': '2021-06-20'},
        # {'PersonID': 23673, 'FactionID': 963, 'Date': '2021-06-21'},
        # {'PersonID': 23512, 'FactionID': 966, 'Date': '2021-06-21'},
        # {'PersonID': 23512, 'FactionID': 966, 'Date': '2021-06-22'},
    ])
    manual_data_fillers['Date'] = pd.to_datetime(manual_data_fillers['Date'])

    members_of_faction_by_date = manual_data_fillers

    for row in (members_of_faction.sort_values('FinishDate', ascending=False).index):
        dates = pd.date_range(
            members_of_faction.loc[row]['StartDate'],
            members_of_faction.loc[row]['FinishDate'],
            closed='left')

        expanded_dates_batch = pd.DataFrame(index=dates)
        expanded_dates_batch['PersonID'] = members_of_faction.loc[row]['PersonID']
        expanded_dates_batch['FactionID'] = int(members_of_faction.loc[row]['FactionID'])
        expanded_dates_batch.index.name = 'Date'
        expanded_dates_batch.reset_index(inplace=True)
        print(expanded_dates_batch)
        members_of_faction_by_date = pd.concat([members_of_faction_by_date, expanded_dates_batch])
    members_of_faction_by_date.columns = ['person_id', 'faction_id', 'date']


    members_of_faction_by_date.to_csv(
        '../data/transformed/members_of_faction_by_date.csv',
        index=False)

    members_of_faction_by_date