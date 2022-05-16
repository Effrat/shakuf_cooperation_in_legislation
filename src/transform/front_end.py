import pandas as pd


def front_end():
    """
    Creates front_end table from bill_sponsors_w_type, person and faction.
    """

    # ----- load -----
    person = pd.read_excel('../data/transformed/person.xlsx')
    person = person[['person_id', 'full_name', 'site_id']]
    person

    bill_sponsors_w_type = pd.read_excel(
        '../data/transformed/bill_sponsors_w_type.xlsx',
        parse_dates=['date'])
    bill_sponsors_w_type

    # ----- transform -----
    front_end = pd.merge(person, bill_sponsors_w_type, on='person_id', how='right')
    front_end['site_id'] = front_end['site_id'].astype(int)
    front_end

    # ----- export as json -----
    front_end.to_json('../data/transformed/front_end.json', orient='records')