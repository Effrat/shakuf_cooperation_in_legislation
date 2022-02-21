#TODO: break into two parts?


import pandas as pd




def members_of_knesset_faction_and_side_by_date():
    """
    Create a table of members of the knesset and their faction and side by date.
    """
    faction_side_by_date = pd.read_csv(
        '../data/transformed/faction_side_by_date.csv',
        parse_dates=['date'])
    faction_side_by_date
    members_of_knesset_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_by_date.csv',
        parse_dates=['date'])
    members_of_knesset_by_date
    members_of_faction_by_date = pd.read_csv(
        '../data/transformed/members_of_faction_by_date.csv',
        parse_dates=['date'])
    members_of_faction_by_date


    # ---- members of Knesset who are also members of a faction ----
    members_of_knesset_faction_by_date = members_of_knesset_by_date.set_index(
        ['date', 'person_id']).join(
            members_of_faction_by_date.set_index(
                ['date', 'person_id']), how='left')
    members_of_knesset_faction_by_date = members_of_knesset_faction_by_date.reset_index()
    members_of_knesset_faction_by_date.drop_duplicates(subset=['date', 'person_id'], inplace=True)
    members_of_knesset_faction_by_date

    members_of_knesset_faction_and_side_by_date = members_of_knesset_faction_by_date.set_index(
        ['date', 'faction_id']).join(
            faction_side_by_date.set_index(
                ['date', 'faction_id']), how='left')
    members_of_knesset_faction_and_side_by_date.rename(columns={'faction_side': 'person_side'}, inplace=True)
    members_of_knesset_faction_and_side_by_date = members_of_knesset_faction_and_side_by_date.reset_index()
    # members_of_knesset_faction_and_side_by_date['faction_id'].fillna(0, inplace=True)
    # members_of_knesset_faction_and_side_by_date['faction_id'] = members_of_knesset_faction_and_side_by_date['faction_id'].astype('Int64')
    # members_of_knesset_faction_and_side_by_date['person_side'].fillna('unknown', inplace=True)
    members_of_knesset_faction_and_side_by_date.drop_duplicates(subset=['date', 'person_id'], inplace=True)
    
    # ---- manually add missing data ----
    df = members_of_knesset_faction_and_side_by_date
    errors1 = pd.read_csv(
        '../data/missing_data/no_faction_2020-03-15_-_2020-03-28.csv')
    errors1['start_date'] = '2020-03-16'
    errors1['end_date'] = '2020-04-07'
    errors = errors1

    for i in errors.index:
        filter = (df['person_id'] == errors.loc[i]['person_id']) & (df['date'] >= errors.loc[i]['start_date']) & (df['date'] < errors.loc[i]['end_date'])
        to_fix = df[filter].copy()
        # print(to_fix)
        to_fix = to_fix.fillna(method='bfill')
        # print(to_fix)
        df[filter] = to_fix
    
    members_of_knesset_faction_and_side_by_date = df
    
    members_of_knesset_faction_and_side_by_date.to_csv(
        '../data/transformed/members_of_knesset_faction_and_side_by_date.csv',
        index=False)
    print(members_of_knesset_faction_and_side_by_date.sort_values('person_side'))



