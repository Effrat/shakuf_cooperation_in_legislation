import pandas as pd
from datetime import date


def members_of_faction_by_date():
    """
    Creates members_of_faction_by_date table from KNS_PersonToPosition by expanding dates.
    """
    today = date.today()

    KNS_PersonToPosition = pd.read_excel('../data/raw/KNS_PersonToPosition.xlsx')
    KNS_PersonToPosition = KNS_PersonToPosition[KNS_PersonToPosition['PersonID'] != 30299]

    members_of_faction = KNS_PersonToPosition[KNS_PersonToPosition['PositionID'].isin([48, 54])] # member of faction
    members_of_faction = members_of_faction[['PersonID', 'FactionID', 'StartDate', 'FinishDate']]
    members_of_faction['FinishDate'].fillna(today, inplace=True)
    members_of_faction['StartDate'] = pd.to_datetime(members_of_faction['StartDate'])
    members_of_faction['FinishDate'] = pd.to_datetime(members_of_faction['FinishDate'])
    members_of_faction.sort_values('FinishDate', inplace=True, ascending=False)

    members_of_faction_by_date = pd.DataFrame(columns=['person_id', 'faction_id', 'date'])


    # ----- add missing records ----- 
    manual_data_fillers = pd.DataFrame([
        {'person_id': 23631, 'faction_id': 967, 'date': '2021-06-23'}, # Karin Elharar + Yesh Atid
        {'person_id': 23631, 'faction_id': 967, 'date': '2021-06-24'}, # Karin Elharar + Yesh Atid
        {'person_id': 23673, 'faction_id': 963, 'date': '2021-06-20'}, # Omer Bar-Lev + Ha'avoda
        {'person_id': 23673, 'faction_id': 963, 'date': '2021-06-21'}, # Omer Bar-Lev + Ha'avoda
        {'person_id': 23512, 'faction_id': 966, 'date': '2021-06-21'}, # Ayelet Shaked + Yemina
        {'person_id': 23512, 'faction_id': 966, 'date': '2021-06-22'}, # Ayelet Shaked + Yemina
    ])
    manual_data_fillers['date'] = pd.to_datetime(manual_data_fillers['date'])
    members_of_faction_by_date = pd.concat([members_of_faction_by_date, manual_data_fillers])


    # ----- expand dates -----
    for row in (members_of_faction.sort_values('FinishDate', ascending=False).index):
        dates = pd.date_range(
            members_of_faction.loc[row]['StartDate'],
            members_of_faction.loc[row]['FinishDate'],
            closed='left')

        expanded_dates_batch = pd.DataFrame(index=dates)
        expanded_dates_batch['person_id'] = members_of_faction.loc[row]['PersonID']
        expanded_dates_batch['faction_id'] = int(members_of_faction.loc[row]['FactionID'])
        expanded_dates_batch.index.name = 'date'
        expanded_dates_batch.reset_index(inplace=True)
        members_of_faction_by_date = pd.concat([members_of_faction_by_date, expanded_dates_batch])

    members_of_faction_by_date.to_csv(
        '../data/transformed/members_of_faction_by_date.csv',
        index=False)

    members_of_faction_by_date