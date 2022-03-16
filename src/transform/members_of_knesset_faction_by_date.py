import pandas as pd


def members_of_knesset_faction_by_date():
    """
    Creates members_of_knesset_faction_by_date table from members_of_knesset_by_date and members_of_faction_by_date.
    """
    members_of_knesset_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_by_date.csv',
        parse_dates=['date'])

    members_of_faction_by_date = pd.read_csv(
        '../data/transformed/members_of_faction_by_date.csv',
        parse_dates=['date'])


    members_of_knesset_faction_by_date = pd.merge(
        members_of_knesset_by_date, members_of_faction_by_date, how='outer')
        # if knesset_num is NaN, then not a Member of Knesset (Norwegian?)
    members_of_knesset_faction_by_date.sort_values('date', inplace=True)
    members_of_knesset_faction_by_date.drop_duplicates(
        subset=['date', 'person_id'], inplace=True, keep='first')


    members_of_knesset_faction_by_date.to_csv(
        '../data/transformed/members_of_knesset_faction_by_date.csv', index=False)