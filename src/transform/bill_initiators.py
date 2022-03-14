import pandas as pd


def bill_initiators():
    """
    """
    members_of_knesset_faction_and_side_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_faction_and_side_by_date.csv',
        parse_dates=['date'])
    members_of_knesset_faction_and_side_by_date

    all_bill_initiators_to_date = pd.read_excel(
        '../data/transformed/all_bill_initiators_to_date.xlsx',
        parse_dates=['date'])
    all_bill_initiators_to_date

    bill_initiators = all_bill_initiators_to_date.set_index(
        ['person_id', 'date']).join(
            members_of_knesset_faction_and_side_by_date.set_index(
                ['person_id', 'date']), how='left')
    bill_initiators.reset_index(inplace=True)
    bill_initiators['faction_id'] = bill_initiators['faction_id'].fillna(0)
    bill_initiators['faction_id'] = bill_initiators['faction_id'].astype('Int64')

    bill_initiators.to_csv(
        '../data/model/facts/bill_initiators.csv',
        index=False)
    bill_initiators