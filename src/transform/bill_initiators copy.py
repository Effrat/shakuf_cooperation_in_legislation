import pandas as pd

df = pd.read_csv(
    '../../data/transformed/members_of_knesset_faction_and_side_by_date.csv',
    parse_dates=['date'])
df = df.sort_values('date')
df

errors1 = pd.read_csv(
    '../../data/missing_data/no_faction_2020-03-15_-_2020-03-28.csv')
errors1['start_date'] = '2020-03-16'
errors1['end_date'] = '2020-04-07'
errors = errors1

errors
for i in errors.index:
    filter = (df['person_id'] == errors.loc[i]['person_id']) & (df['date'] >= errors.loc[i]['start_date']) & (df['date'] < errors.loc[i]['end_date'])
    to_fix = df[filter].copy()
    # print(to_fix)
    to_fix = to_fix.fillna(method='bfill')
    print(to_fix)
df[filter] = to_fix
df[filter]