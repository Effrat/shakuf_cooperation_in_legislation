import pandas as pd



def members_of_knesset_faction_and_side_by_date():
    """
    Creates members_of_knesset_faction_and_side_by_date table from members_of_knesset_faction_by_date and faction_side_by_date.
    """

    # ----- load -----
    members_of_knesset_faction_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_faction_by_date.csv',
        parse_dates=['date'])

    faction_side_by_date = pd.read_csv(
        '../data/transformed/faction_side_by_date.csv',
        parse_dates=['date'])

    # ----- transform -----
    # ---- members of Knesset who are also members of a faction and their side by date ----
    members_of_knesset_faction_and_side_by_date = pd.merge(
        members_of_knesset_faction_by_date, faction_side_by_date,
        on=['date', 'faction_id'], how='left')
    members_of_knesset_faction_and_side_by_date.rename(columns={'faction_side': 'person_side'}, inplace=True)
    members_of_knesset_faction_and_side_by_date.drop_duplicates(subset=['date', 'person_id'], inplace=True)

    # ----- save -----
    members_of_knesset_faction_and_side_by_date.to_csv(
        '../data/transformed/members_of_knesset_faction_and_side_by_date.csv',
        index=False)



