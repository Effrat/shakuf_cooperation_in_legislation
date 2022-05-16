import pandas as pd


def bill_sponsors():
    """
    Creates bill_sponsors table from members_of_knesset_faction_and_side_by_date and all_bill_sponsors_to_date.
    """

    # ----- load -----
    members_of_knesset_faction_and_side_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_faction_and_side_by_date.csv',
        parse_dates=['date'])

    all_bill_sponsors_to_date = pd.read_excel(
        '../data/transformed/all_bill_sponsors_to_date.xlsx',
        parse_dates=['date'])

    # ----- transform -----
    bill_sponsors = pd.merge(
        all_bill_sponsors_to_date, members_of_knesset_faction_and_side_by_date,
        on=['person_id', 'date'], how='inner')


    # ----- save -----
    bill_sponsors.to_csv(
        '../data/transformed/bill_sponsors.csv',
        index=False)