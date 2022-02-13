import pandas as pd
from datetime import date

today = date.today()
def faction_transform():
    KNS_Faction = pd.read_excel('../data/raw/KNS_Faction.xlsx', index_col=0)
    faction = KNS_Faction[(KNS_Faction['FactionID'] != 911) & (KNS_Faction['FactionID'] != 356)]
    faction = faction[['FactionID', 'Name', 'KnessetNum', 'StartDate', 'FinishDate']]
    faction['StartDate'] = pd.to_datetime(faction['StartDate']).apply(lambda x: x.date())
    faction['FinishDate'] = pd.to_datetime(faction['FinishDate']).apply(lambda x: x.date())
    faction['FinishDate'].fillna(today, inplace=True)
    faction.sort_values('FinishDate')
    faction.to_excel(
        '../data/model/dimensions/faction.xlsx',
        sheet_name='faction',
        header=True,
        index=False
        )
    faction
