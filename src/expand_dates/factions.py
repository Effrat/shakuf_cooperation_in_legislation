import pandas as pd
from datetime import date

today = date.today()

KNS_Faction = pd.read_excel('..\..\data\\raw\KNS_Faction.xlsx', index_col=0)
factions = KNS_Faction[(KNS_Faction['FactionID'] != 911) & (KNS_Faction['FactionID'] != 356)]
factions.info()
factions['StartDate'] = pd.to_datetime(factions['StartDate'])
factions['FinishDate'] = pd.to_datetime(factions['FinishDate'])
factions['FinishDate'].fillna(today, inplace=True)
# factions[factions['IsCurrent'] == True]['FinishDate'].fillna(today, inplace=True)
factions.sort_values('StartDate', inplace=True, ascending=False)
factions

factions_by_date = pd.DataFrame()

for faction_id in (factions.index):
    # print(factions.loc[faction_id])
    dates = pd.date_range(
        factions.loc[faction_id]['StartDate'],
        factions.loc[faction_id]['FinishDate'],
        closed='left')

    expanded_dates_batch = pd.DataFrame(index=dates)
    expanded_dates_batch.columns.name = 'Date'
    expanded_dates_batch['FactionID'] = faction_id
    expanded_dates_batch['Name'] = factions.loc[faction_id]['Name']
    expanded_dates_batch['KnessetNum'] = factions.loc[faction_id]['KnessetNum']
    print(expanded_dates_batch)
    factions_by_date = pd.concat([factions_by_date, expanded_dates_batch])

factions_by_date.to_excel(
    '..\..\data\\expanded\\factions_by_date.xlsx',
    sheet_name='factions_by_date',
    header=True,
    index_label='Date'
    )

factions_by_date