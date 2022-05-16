import pandas as pd

def bill_sponsors_w_type():
    # ----- load -----
    bill_sponsors = pd.read_csv(
        '../data/transformed/bill_sponsors.csv', parse_dates=['date'])
    bill_sponsors = bill_sponsors[['bill_id', 'person_id', 'date', 'faction_id']]
    bill_sponsors

    bill_to_type = pd.read_excel(
        '../data/transformed/bill_to_type.xlsx')
    bill_to_type


    # ----- transform -----
    bill_sponsors_w_type = pd.merge(
        bill_sponsors, bill_to_type, on='bill_id', how='right')
    # filter 24th Knesset by date
    bill_sponsors_w_type = bill_sponsors_w_type[bill_sponsors_w_type['date'] > '2021-04-05']
    bill_sponsors_w_type

    # ----- save -----
    bill_sponsors_w_type.to_excel(
        '../data/transformed/bill_sponsors_w_type.xlsx',
        index=False)

    # ----- export to json -----
    bill_sponsors_w_type.to_json(
        '../data/transformed/bill_sponsors_w_type.json',
        orient='records')