import pandas as pd


def members_of_knesset_faction_by_date():
    """
    """

    members_of_knesset_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_by_date.csv',
        parse_dates=['date'])
    members_of_knesset_by_date

    members_of_faction_by_date = pd.read_csv(
        '../data/transformed/members_of_faction_by_date.csv',
        parse_dates=['date'])
    members_of_faction_by_date


    # ---- members of Knesset who are also members of a faction ----
    members_of_knesset_faction_by_date = pd.merge(
        members_of_knesset_by_date, members_of_faction_by_date, how='left')
    members_of_knesset_faction_by_date.sort_values('date', inplace=True)
    members_of_knesset_faction_by_date.drop_duplicates(
        subset=['date', 'person_id'], inplace=True, keep='first')


    members_of_knesset_faction_by_date.to_csv(
        '../data/transformed/members_of_knesset_faction_by_date.csv',
        index=False)
    members_of_knesset_faction_by_date