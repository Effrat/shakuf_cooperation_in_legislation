#TODO: break into functions

import pandas as pd




# ===================   import data   ===================
factions_side = pd.read_excel('..\..\data\\expanded\\factions_side.xlsx', index_col=0)
factions_side['FactionID'] = factions_side['FactionID'].astype('Int64')
factions_side
members_of_knesset_by_date = pd.read_csv('..\..\data\\expanded\\members_of_knesset_by_date.csv', parse_dates=['Date'])
members_of_knesset_by_date
members_of_faction_by_date = pd.read_csv('..\..\data\\expanded\\members_of_faction_by_date.csv', parse_dates=['Date'])
members_of_faction_by_date


# ===================     members of Knesset who are members of a faction   ===================
members_of_knesset_by_faction = members_of_knesset_by_date.set_index(['Date', 'PersonID']).join(members_of_faction_by_date.set_index(['Date', 'PersonID']), how='left')
members_of_knesset_by_faction = members_of_knesset_by_faction.reset_index().drop_duplicates(subset=['Date', 'PersonID'])
members_of_knesset_by_faction['FactionID'] = members_of_knesset_by_faction['FactionID'].astype('Int64')
members_of_knesset_by_faction

members_of_knesset_by_faction_and_side = members_of_knesset_by_faction.set_index(['Date', 'FactionID']).join(factions_side.set_index(['Date', 'FactionID']), how='left')
members_of_knesset_by_faction_and_side = members_of_knesset_by_faction_and_side.reset_index().drop_duplicates()
members_of_knesset_by_faction_and_side.to_csv('..\..\data\\expanded\\members_of_knesset_by_faction_and_side.csv',)
members_of_knesset_by_faction_and_side.sort_values('Side')



