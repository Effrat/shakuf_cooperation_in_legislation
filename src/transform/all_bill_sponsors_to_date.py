import pandas as pd

def all_bill_sponsors_to_date():
    """
    Creates all_bill_sponsors_to_date table from bill_to_date and all_bills_sponsors.
    """
    bill_to_date = pd.read_excel(
        '../data/transformed/bill_to_date.xlsx',
        parse_dates=['date'])

    all_bills_sponsors = pd.read_excel(
        '../data/transformed/all_bills_sponsors.xlsx')

    all_bill_sponsors_to_date = pd.merge(
        bill_to_date, all_bills_sponsors, on='bill_id', how='right')

    all_bill_sponsors_to_date.to_excel(
        '../data/transformed/all_bill_sponsors_to_date.xlsx',
        sheet_name='all_bill_sponsors_to_date', index=False)