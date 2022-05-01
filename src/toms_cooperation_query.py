# Each bill will be considered 'bipartisan' if there are at least one sponsor (either initiator or joiner) of each side (opposition/coalition), and 'single-sided' if all sponsors represent the same side.

# Let's count total bills in each category.


import pandas as pd



# ----- load -----
bill_sponsors = pd.read_csv(
    '../data/model/facts/bill_sponsors.csv', parse_dates=['date'])
bill_sponsors.groupby('is_initiator').nunique()
bill_sponsors['person_side'] = bill_sponsors['person_side'].astype(str)
bill_sponsors.groupby(['person_side']).nunique()
bill_sponsors


# ----- transform -----
initiators = bill_sponsors[bill_sponsors['is_initiator'] == True]
initiators = initiators[['bill_id', 'person_id', 'person_side']]
initiators['person_side'].fillna('unknown', inplace=True)
initiators

bill_to_total_sponsors_by_side = initiators.groupby(['bill_id', 'person_side']).nunique().reset_index()
bill_to_total_sponsors_by_side = bill_to_total_sponsors_by_side.pivot_table(
    index='bill_id', columns='person_side', values='person_id', aggfunc='nunique')
bill_to_total_sponsors_by_side.reset_index(inplace=True)
bill_to_total_sponsors_by_side

# ----- save -----
bill_to_total_sponsors_by_side.to_excel(
    '../data/transformed/bill_to_total_sponsors_by_side.xlsx',
    sheet_name='bill_to_total_sponsors_by_side', index=False)