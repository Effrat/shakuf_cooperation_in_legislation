from email.utils import parsedate_to_datetime
import pandas as pd
import plotly.express as px
from datetime import date, timedelta



# members_of_faction_by_date = pd.read_csv(
#     '..\..\data\\expanded\members_of_faction_by_date.csv')
# members_of_faction_by_date['Date'] = pd.to_datetime(members_of_faction_by_date['Date'])
# members_of_faction_by_date.sort_values(by='Date', inplace=True)

# karin_elharar = members_of_faction_by_date[(members_of_faction_by_date['PersonID'] == 23631)]
# for i in karin_elharar.index:
#     print(karin_elharar.loc[i])

# omer_bar_lev = members_of_faction_by_date[(members_of_faction_by_date['PersonID'] == 23673)]
#     print(omer_bar_lev.loc[i])

# ayelet_shaked = members_of_faction_by_date[(members_of_faction_by_date['PersonID'] == 23512)]
# for i in ayelet_shaked.index:
#     print(ayelet_shaked.loc[i])


# un = members_of_faction_by_date[(members_of_faction_by_date['PersonID'] == 30719)]
# for i in un.index:
#     print(un.loc[i])

# daily_total_members_of_faction = members_of_faction_by_date.groupby(['Date', 'FactionID']).nunique()



# members_of_faction_by_date[members_of_faction_by_date['FactionID'] == 968]


KNS_PersonToPosition = pd.read_excel('..\..\data\\raw\\KNS_PersonToPosition.xlsx', index_col=0)
KNS_PersonToPosition[(KNS_PersonToPosition['PersonID'] == 427)].sort_values('StartDate')# & (KNS_PersonToPosition['PositionID'] == )]
# KNS_PersonToPosition