import pandas as pd
from datetime import date

today = date.today()


# ===================   import data   ===================
members_of_faction_by_date = pd.read_csv(
    '..\..\data\\expanded\\members_of_faction_by_date.csv',
    parse_dates=['Date'])
members_of_faction_by_date.drop_duplicates(inplace=True)
members_of_faction_by_date
people_in_government_by_date = pd.read_excel('..\..\data\\expanded\\people_in_government_by_date.xlsx')
people_in_government_by_date = people_in_government_by_date[['Date', 'PersonID']].drop_duplicates()
people_in_government_by_date



# ===================    factions in Knesset   ===================
factions_in_knesset = members_of_faction_by_date[['Date', 'FactionID']].drop_duplicates()
factions_in_knesset

# fig = px.area(factions_in_knesset.groupby('Date').nunique(), title='Total Factions in Knesset')
# fig.show()



# ===================   factions in coalition   ===================
"""
If at least one member of the faction is in government (or coalition chairman) -
then the faction is in coalition.
"""
factions_in_coalition = people_in_government_by_date.set_index(['Date', 'PersonID']).join(members_of_faction_by_date.set_index(['Date', 'PersonID']), how='inner')
factions_in_coalition = factions_in_coalition.reset_index()[['Date', 'FactionID']]

# add Raam
dates = pd.date_range('2021-06-14', today, closed='left')
raam = pd.DataFrame(index=dates)
raam.index.name = 'Date'
raam['FactionID'] = 973
raam.reset_index(inplace=True)
factions_in_coalition = factions_in_coalition.append(raam, ignore_index=True)

# add Israel Betenu
dates = pd.date_range('2021-06-14', today, closed='left')
israel_betenu = pd.DataFrame(index=dates)
israel_betenu.index.name = 'Date'
israel_betenu['FactionID'] = 968
israel_betenu.reset_index(inplace=True)
factions_in_coalition = factions_in_coalition.append(israel_betenu, ignore_index=True)

# add Meretz
dates = pd.date_range('2021-07-18', '2021-07-26', closed='left')
meretz = pd.DataFrame(index=dates)
meretz.index.name = 'Date'
meretz['FactionID'] = 970
meretz.reset_index(inplace=True)
factions_in_coalition = factions_in_coalition.append(meretz, ignore_index=True)

factions_in_coalition.drop_duplicates(inplace=True)
factions_in_coalition['Side'] = 'Coalition'
factions_in_coalition

# fig = px.area(factions_in_coalition.groupby('Date').nunique(), title='Total Factions in Coalition')
# fig.show()



# ===================    faction in/out of coalition   ===================
factions_side = factions_in_knesset.set_index(['Date', 'FactionID']).join(factions_in_coalition.set_index(['Date', 'FactionID']), how='left')
factions_side = factions_side.reset_index().drop_duplicates(subset=['Date', 'FactionID'])
factions_side['Side'].fillna('Opposition', inplace=True)
factions_side.to_csv('..\..\data\\expanded\\factions_side.csv', index=False)
factions_side

# fig = px.line(daily_total_factions, title='Factions in/out of Coalition')
# fig.show()