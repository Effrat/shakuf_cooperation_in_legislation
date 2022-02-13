#TODO: break into functions

import pandas as pd
from datetime import date

today = date.today()
factions_by_date = pd.read_csv('..\..\data\\expanded\\factions_by_date.csv', index_col='Date')
earliest_date = factions_by_date.index.min()

date = pd.date_range(earliest_date, today, closed='left')
date = pd.DataFrame(index=date)
date.index.name = 'Date'
# add knesset number + government number for each day


date.to_csv('..\..\data\\to_powerbi\date.csv', index_label='Date')

date
