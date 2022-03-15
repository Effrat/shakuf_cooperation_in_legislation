import pandas as pd
from datetime import date

def dates():
    """
    Creates dates table from knesset_by_date.
    """
    today = date.today()
    knesset_by_dates = pd.read_excel('../data/transformed/knesset_by_date.xlsx')
    earliest_date = knesset_by_dates['date'].min()
    dates = pd.date_range(earliest_date, today, closed='left')
    dates = pd.DataFrame(index=dates)
    dates.index.name = 'date'
    dates['year'] = dates.index.year

    dates = dates.join(knesset_by_dates.set_index('date'), how='left')
    dates[['knesset_num', 'assembly', 'plenum']] = dates[['knesset_num', 'assembly', 'plenum']].astype('Int64')
    dates.reset_index(inplace=True)

    dates.sort_values(by=['date'], inplace=True)
    dates['knesset_num'].fillna(method='ffill', inplace=True)
    dates['assembly'].fillna(method='ffill', inplace=True)
    dates['plenum'].fillna(method='ffill', inplace=True)

    dates.to_excel(
        '../data/model/dimensions/dates.xlsx',
        sheet_name='dates',
        index=False
        )

    dates
