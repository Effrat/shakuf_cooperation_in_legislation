import pandas as pd
from datetime import date

def knesset():
    '''
    Creates knesset table from KNS_Knesset.
    '''
    today = date.today()

    KNS_KnessetDates = pd.read_excel('../data/raw/KNS_KnessetDates.xlsx', index_col=0)
    knesset = KNS_KnessetDates[['KnessetNum', 'Name', 'PlenumStart', 'PlenumFinish', 'IsCurrent']]
    knesset['PlenumFinish'].fillna(today, inplace=True)
    knesset[['PlenumStart', 'PlenumFinish']] = knesset[['PlenumStart', 'PlenumFinish']].apply(pd.to_datetime)
    knesset = knesset.groupby('KnessetNum').agg({'Name': 'max', 'PlenumStart': 'min', 'PlenumFinish': 'max'})
    knesset.reset_index(inplace=True)

    knesset.columns = ['knesset_num', 'name', 'start_date', 'end_date']
    knesset.to_excel(
        '../data/model/dimensions/knesset.xlsx',
        sheet_name='knesset',
        index=False)
    knesset