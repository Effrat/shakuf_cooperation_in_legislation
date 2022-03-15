import pandas as pd
from datetime import date


def faction():
    '''
    Creates faction table from KNS_Faction.
    '''
    today = date.today()

    KNS_Faction = pd.read_excel('../data/raw/KNS_Faction.xlsx', index_col=0)
    faction = KNS_Faction[KNS_Faction['FactionID'] != 911]
    faction = faction[['FactionID', 'Name', 'KnessetNum', 'StartDate', 'FinishDate']]
    faction['FinishDate'].fillna(today, inplace=True)
    faction['StartDate'] = pd.to_datetime(faction['StartDate']).apply(lambda x: x.date())
    faction['FinishDate'] = pd.to_datetime(faction['FinishDate']).apply(lambda x: x.date())
    faction.columns = ['faction_id', 'name', 'knesset_num', 'start_date', 'end_date']

    faction.to_excel(
        '../data/model/dimensions/faction.xlsx',
        sheet_name='faction',
        header=True,
        index=False)