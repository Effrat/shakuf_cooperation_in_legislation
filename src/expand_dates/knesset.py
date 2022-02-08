#TODO: break into functions

import pandas as pd
from datetime import date

today = date.today()

KNS_KnessetDates = pd.read_excel('..\..\data\\raw\KNS_KnessetDates.xlsx')
# knesset = KNS_KnessetDates[KNS_KnessetDates.index != 911]
knesset = KNS_KnessetDates#[['KnessetNum', 'Assembly', 'Plenum', 'PlenumStart', 'PlenumFinish', 'IsCurrent']]
knesset['PlenumFinish'].fillna(today, inplace=True)
knesset['PlenumStart'] = pd.to_datetime(knesset['PlenumStart'])
knesset['PlenumFinish'] = pd.to_datetime(knesset['PlenumFinish'])
# knesset.info()
knesset.sort_values('PlenumFinish', inplace=True, ascending=False)
knesset

knesset_by_date = pd.DataFrame()

# knesset['KnessetDateID'].values

for knesset_date_id in (knesset.index):
    # print(knesset.loc[knesset_date_id])
    dates = pd.date_range(
        knesset.loc[knesset_date_id]['PlenumStart'],
        knesset.loc[knesset_date_id]['PlenumFinish'],
        closed='left')

    expanded_dates_batch = pd.DataFrame(index=dates)
    expanded_dates_batch.columns.name = 'Date'
    expanded_dates_batch['KnessetNum'] = knesset.loc[knesset_date_id]['KnessetNum']
    expanded_dates_batch['Assembly'] = knesset.loc[knesset_date_id]['Assembly']
    expanded_dates_batch['Plenum'] = knesset.loc[knesset_date_id]['Plenum']
    print(expanded_dates_batch)
    knesset_by_date = pd.concat([knesset_by_date, expanded_dates_batch])

knesset_by_date.to_excel(f'..\..\data\\expanded\\knesset_by_date.xlsx', header=True)

knesset_by_date