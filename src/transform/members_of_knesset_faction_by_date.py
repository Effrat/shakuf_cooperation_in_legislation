import pandas as pd


# def members_of_knesset_faction_by_date():
#     """
#     Creates members_of_knesset_faction_by_date table from members_of_knesset_by_date and members_of_faction_by_date.
#     """


# ----- load -----
members_of_knesset_by_date = pd.read_csv(
    '../../data/transformed/members_of_knesset_by_date.csv',
    parse_dates=['date'])

members_of_faction_by_date = pd.read_csv(
    '../../data/transformed/members_of_faction_by_date.csv',
    parse_dates=['date'])



# ----- transform -----
members_of_knesset_faction_by_date = pd.merge(
    members_of_knesset_by_date, members_of_faction_by_date, how='left')
    # if knesset_num is NaN, then not a Member of Knesset (Norwegian?)
members_of_knesset_faction_by_date.sort_values('date', inplace=True)
members_of_knesset_faction_by_date.drop_duplicates(
    subset=['date', 'person_id'], inplace=True, keep='first')



# ----- testing/feedback -----
# members of Knesset w/o faction affiliation
no_faction = members_of_knesset_faction_by_date[members_of_knesset_faction_by_date['faction_id'].isnull()]
no_faction = no_faction[['date', 'person_id']].drop_duplicates()
no_faction['date'] = no_faction['date'].dt.strftime('%Y-%m-%d')
no_faction.to_csv(
    '../../data/reports/members_of_knesset_wo_faction.csv',
    index=False)



# ----- save -----
members_of_knesset_faction_by_date.to_csv(
    '../../data/transformed/members_of_knesset_faction_by_date.csv', index=False)