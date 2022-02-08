#TODO: break into functions

import pandas as pd
from datetime import date
import plotly.express as px


members_of_faction_by_date = pd.read_csv('..\..\data\\expanded\\members_of_faction_by_date.csv')#, index_col=['Date', 'PersonID'])
members_of_faction_by_date['Date'] = pd.to_datetime(members_of_faction_by_date['Date'])
members_of_faction_by_date.set_index('Date', inplace=True)

todays_faction_from_members = set(members_of_faction_by_date.loc['26/1/2022']['FactionID'])
todays_faction_from_members
# fig = px.line(plot)
# fig.show()


# factions = pd.read_csv('..\..\data\\expanded\\factions_by_date.csv')
# factions['Date'] = pd.to_datetime(factions['Date'])
# factions
# todays_factions_from_factions = factions[factions['Date'] == '2022-01-26']
# todays_factions_from_factions
# if len(factions_from_members_of_faction_by_date - factions_from_factions) == 0:
#     print('No faction ids which are both in factions_from_members_of_faction_by_date and not in factions_from_factions')


# factions_from_factions - factions_from_members_of_faction_by_date


# # people_in_government_by_date = pd.read_csv('..\..\data\\expanded\\people_in_government_by_date.csv', index_col=['Date', 'PersonID'])
# # people_in_government_by_date

raam = members_of_faction_by_date[members_of_faction_by_date['FactionID'] == 973]
raam

# # faction_in_coalition = members_of_faction_by_date.join(people_in_government_by_date, on=['Date', 'PersonID'], how='inner')
# # faction_in_coalition = faction_in_coalition.reset_index()[['Date', 'FactionID']].drop_duplicates()

# # faction_in_coalition.to_csv('..\..\data\\to_powerbi\\faction_in_coalition.csv', index=False)

# # # manually add Raam faction to current coalition, though non of it's members is in the government
