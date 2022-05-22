import pandas as pd


# Examine if Bibi, indeed, has no cooperations in legislation
bill_sponsors = pd.read_csv('../../data/transformed/bill_sponsors.csv',
    parse_dates=['date'])
bill_sponsors

# faction_side_by_date = pd.read_csv('../../data/transformed/faction_side_by_date.csv',
#     parse_dates=['date'])
# faction_side_by_date


bill_ids = bill_sponsors[(bill_sponsors['person_id'] == 965) & (bill_sponsors['knesset_num'] == 24)]['bill_id'].values

# for bill_id in bill_ids:
#     print('bill id: ', bill_id)
#     sponsors = bill_sponsors[(bill_sponsors['bill_id'] == bill_id) & (bill_sponsors['faction_id'] == 966)]['person_id'].values
#     print('sponsors: ', sponsors)
#     bill_date = bill_sponsors[bill_sponsors['bill_id'] == bill_id]['date'].unique()[0]
#     print('bill date: ', bill_date)
#     bill_sponsors_factions = bill_sponsors[bill_sponsors['bill_id'] == bill_id]['faction_id'].unique()
#     print('sponsors from factions: ', bill_sponsors_factions)

#     faction_side_by_date_for_bill = faction_side_by_date[(faction_side_by_date['date'] == bill_date) & (faction_side_by_date['faction_id'].isin(bill_sponsors_factions))]
#     print(faction_side_by_date_for_bill, '\n')

# Result: two bills seem to have one member of the coalition, but it's Shikli, so in fact, there's no cooperation.


# Examine whether these two bills are categorised as single-sided.
bill_to_type = pd.read_excel('../../data/transformed/bill_to_type.xlsx')
bill_to_type[bill_to_type['bill_id'].isin(bill_ids)]
# Result: All three bills are categorized as single-sided, which is the correct result.