from email.utils import parsedate_to_datetime
import pandas as pd
import plotly.express as px
from datetime import date, timedelta


# members_of_knesset_in_knesset_by_date = pd.read_csv(f'..\..\data\\expanded\members_of_knesset_in_knesset_by_date.csv')
# members_of_knesset_in_knesset_by_date['Date'] = pd.to_datetime(members_of_knesset_in_knesset_by_date['Date'])
# daily_total_members_of_knesset = members_of_knesset_in_knesset_by_date.groupby('Date').nunique()
# daily_total_members_of_knesset.rename(columns={'PersonID': 'Count'}, inplace=True)
# daily_total_members_of_knesset.index = pd.to_datetime(daily_total_members_of_knesset.index)
# # daily_total_members_of_knesset
# fig = px.area(daily_total_members_of_knesset)
# fig.show()

members_of_faction_by_date = pd.read_csv(f'..\..\data\\expanded\members_of_faction_by_date.csv')
members_of_faction_by_date['Date'] = pd.to_datetime(members_of_faction_by_date['Date'])
daily_total_members_of_faction = members_of_faction_by_date.groupby(['Date', 'FactionID']).nunique()
# daily_total_members_of_faction
daily_total_members_of_faction.reset_index('FactionID', inplace =True)
daily_total_members_of_faction.rename(columns={'PersonID': 'Count'}, inplace =True)
daily_total_members_of_faction['FactionID'] = pd.to_numeric(daily_total_members_of_faction['FactionID'], downcast='integer')
# daily_total_members_of_faction

fig = px.area(daily_total_members_of_faction, color='FactionID')
fig.write_html('..\charts\daily_total_members_of_faction.html')
fig.show()


# # compare set of PersoIDs for current day to compare between members of Knesset to members of factions
# today_str = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')

# todays_presons_ids_from_members_of_knesset = set(members_of_knesset_in_knesset_by_date.set_index('Date').loc[today_str]['PersonID'])
# todays_presons_ids_from_members_of_factions = set(members_of_faction_by_date.set_index('Date').loc[today_str]['PersonID'])
# print((todays_presons_ids_from_members_of_factions))
# print((todays_presons_ids_from_members_of_knesset))
# print((todays_presons_ids_from_members_of_knesset - todays_presons_ids_from_members_of_factions))
# print((todays_presons_ids_from_members_of_factions - todays_presons_ids_from_members_of_knesset))

# the records are a complete match
# why aren't threre 120 bebmers of factions?
# iterate over persons, check for positions (why don't some of them have a faction?)
