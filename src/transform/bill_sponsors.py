import pandas as pd


def bill_sponsors():
    """
    Creates bill_sponsors table from members_of_knesset_faction_and_side_by_date and all_bill_sponsors_to_date.
    """
    members_of_knesset_faction_and_side_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_faction_and_side_by_date.csv',
        parse_dates=['date'])
    members_of_knesset_faction_and_side_by_date

    all_bill_sponsors_to_date = pd.read_excel(
        '../data/transformed/all_bill_sponsors_to_date.xlsx',
        parse_dates=['date'])
    all_bill_sponsors_to_date

    bill_sponsors = pd.merge(
        all_bill_sponsors_to_date, members_of_knesset_faction_and_side_by_date,
        on=['person_id', 'date'], how='outer')
    bill_sponsors.reset_index(inplace=True)
    # bill_sponsors['faction_id'] = bill_sponsors['faction_id'].fillna(0)
    # bill_sponsors['faction_id'] = bill_sponsors['faction_id'].astype('Int64')

    bill_sponsors.to_csv(
        '../data/model/facts/bill_sponsors.csv',
        index=False)
    bill_sponsors