import pandas as pd

def all_bill_initiators_to_date():
    """
    """
    bill_to_date = pd.read_excel(
        '../data/transformed/bill_to_date.xlsx',
        parse_dates=['date'])
    bill_to_date

    all_bills_initiators = pd.read_excel(
        '../data/transformed/all_bills_initiators.xlsx')
    all_bills_initiators

    all_bill_initiators_to_date = bill_to_date.set_index(
        'bill_id').join(
            all_bills_initiators.set_index(
                'bill_id'), how='right').reset_index()

    print('all_bill_initiators_to_date.nunique:')
    print(all_bill_initiators_to_date.nunique())

    all_bill_initiators_to_date.to_excel(
        '../data/transformed/all_bill_initiators_to_date.xlsx',
        sheet_name='all_bill_initiators_to_date',
        index=False)
    all_bill_initiators_to_date