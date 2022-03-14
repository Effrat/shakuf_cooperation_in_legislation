import pandas as pd
from datetime import date



# def faction_side_by_date():
#     """
#     """
today = date.today()


# ===================   import data   ===================
members_of_faction_by_date = pd.read_csv(
    '../../data/transformed/members_of_faction_by_date.csv',
    parse_dates=['date'])
members_of_faction_by_date.drop_duplicates(inplace=True)
members_of_faction_by_date
people_in_government_by_date = pd.read_excel(
    '../../data/transformed/people_in_government_by_date.xlsx')
people_in_government_by_date = people_in_government_by_date[['date', 'person_id']].drop_duplicates()
people_in_government_by_date



# ===================    factions in Knesset   ===================
factions_in_knesset = members_of_faction_by_date[['date', 'faction_id']].drop_duplicates()
factions_in_knesset


# ===================   factions in coalition   ===================
"""
If at least one member of the faction is in government (or coalition chairman) -
then the faction is in coalition.
"""
factions_in_coalition_by_date = people_in_government_by_date.set_index(
    ['date', 'person_id']).join(
        members_of_faction_by_date.set_index(
            ['date', 'person_id']), how='inner')
factions_in_coalition_by_date = factions_in_coalition_by_date.reset_index()[['date', 'faction_id']]
factions_in_coalition_by_date.drop_duplicates(inplace=True)
factions_in_coalition_by_date

# # ===================   manual data corrections   ===================
# # add Raam
# dates = pd.date_range('2021-06-14', today, closed='left')
# raam = pd.DataFrame(index=dates)
# raam.index.name = 'date'
# raam['faction_id'] = 973
# raam.reset_index(inplace=True)
# factions_in_coalition_by_date = factions_in_coalition_by_date.append(raam, ignore_index=True)

# # add Israel Betenu
# dates = pd.date_range('2021-06-14', today, closed='left')
# israel_betenu = pd.DataFrame(index=dates)
# israel_betenu.index.name = 'date'
# israel_betenu['faction_id'] = 968
# israel_betenu.reset_index(inplace=True)
# factions_in_coalition_by_date = factions_in_coalition_by_date.append(israel_betenu, ignore_index=True)

# # add Meretz
# dates = pd.date_range('2021-07-18', '2021-07-26', closed='left')
# meretz = pd.DataFrame(index=dates)
# meretz.index.name = 'date'
# meretz['faction_id'] = 970
# meretz.reset_index(inplace=True)
# factions_in_coalition_by_date = factions_in_coalition_by_date.append(meretz, ignore_index=True)

# factions_in_coalition_by_date.drop_duplicates(inplace=True)
# factions_in_coalition_by_date

# ===================    faction in/out of coalition   ===================
factions_in_coalition_by_date['faction_side'] = 'coalition'

faction_side_by_date = factions_in_knesset.set_index(
    ['date', 'faction_id']).join(
        factions_in_coalition_by_date.set_index(
            ['date', 'faction_id']), how='left')
faction_side_by_date = faction_side_by_date.reset_index().drop_duplicates(
    subset=['date', 'faction_id'])
faction_side_by_date['faction_side'].fillna('opposition', inplace=True)
faction_side_by_date.to_csv(
    '../../data/transformed/faction_side_by_date.csv',
    index=False)
faction_side_by_date