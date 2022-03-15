import pandas as pd
from datetime import date


def knesset_by_date():
    """
    Creates knesset_by_date table from KNS_KnessetDates.
    """
    today = date.today()

    KNS_KnessetDates = pd.read_excel('..\data\\raw\KNS_KnessetDates.xlsx', index_col=0)
    knesset = KNS_KnessetDates[['KnessetNum', 'Name', 'Assembly', 'Plenum', 'PlenumStart', 'PlenumFinish', 'IsCurrent']]
    knesset['PlenumFinish'].fillna(today, inplace=True)
    knesset['PlenumStart'] = pd.to_datetime(knesset['PlenumStart'])
    knesset['PlenumFinish'] = pd.to_datetime(knesset['PlenumFinish'])
    knesset.sort_values('PlenumStart', inplace=True, ascending=False)

    knesset_by_date = pd.DataFrame()
    for knesset_date_id in (knesset.index):
        # print(knesset.loc[knesset_date_id])
        dates = pd.date_range(
            knesset.loc[knesset_date_id]['PlenumStart'],
            knesset.loc[knesset_date_id]['PlenumFinish'],
            closed='left')

        expanded_dates_batch = pd.DataFrame(index=dates)
        expanded_dates_batch['KnessetNum'] = knesset.loc[knesset_date_id]['KnessetNum']
        expanded_dates_batch['Assembly'] = knesset.loc[knesset_date_id]['Assembly']
        expanded_dates_batch['Plenum'] = knesset.loc[knesset_date_id]['Plenum']
        print(expanded_dates_batch)
        knesset_by_date = pd.concat([knesset_by_date, expanded_dates_batch])
    knesset_by_date.reset_index(inplace=True)
    knesset_by_date.columns = ['date', 'knesset_num', 'assembly', 'plenum']

    knesset_by_date.to_excel(
        '..\data\\transformed\\knesset_by_date.xlsx',
        sheet_name='knesset_by_date',
        index=False
        )

    knesset_by_date
