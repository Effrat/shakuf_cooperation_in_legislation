import pandas as pd
from sqlalchemy import column


def latest_faction():
    """
    Creates latest_faction table faction and members_of_knesset_faction_by_date.
    """

    # ----- load -----
    members_of_knesset_faction_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_faction_by_date.csv',
        parse_dates=['date'])
    members_of_knesset_faction_by_date

    faction = pd.read_excel('../data/transformed/faction.xlsx')
    faction = faction[['faction_id', 'name']]
    faction.rename(columns={'name': 'faction_name'}, inplace=True)
    faction

    # ----- transform -----
    latest_faction = members_of_knesset_faction_by_date.dropna()[['faction_id', 'date', 'person_id']]
    latest_faction['faction_id'] = latest_faction['faction_id'].astype(int)
    latest_faction = latest_faction.sort_values('date')
    latest_faction = latest_faction.groupby('person_id').agg({'date': 'max', 'faction_id': 'last'})
    latest_faction.reset_index(inplace=True)
    latest_faction.drop(columns=['date'], inplace=True)
    latest_faction = pd.merge(latest_faction, faction, on='faction_id', how='left')
    latest_faction.drop(columns=['faction_id'], inplace=True)
    latest_faction

    # ----- export as json -----
    latest_faction.to_json('../data/transformed/latest_faction.json', orient='records')