import pandas as pd
from datetime import date

today = date.today()


def date_create():
    knesset_by_date = pd.read_excel('../data/expanded/knesset_by_date.xlsx')
    # knesset_by_date
    earliest_date = knesset_by_date['Date'].min()
    date = pd.date_range(earliest_date, today, closed='left')
    date = pd.DataFrame(index=date)
    date.index.name = 'Date'
    date['year'] = date.index.year

    date = date.join(knesset_by_date.set_index('Date'), how='left')
    date.reset_index(inplace=True)

    date.to_excel(
        '../data/model/dimensions/date.xlsx',
        sheet_name='date',
        index=False
        )

    date
