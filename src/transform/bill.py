import pandas as pd

def bill():
    """
    """
    bill_to_side = pd.read_excel(
        '../data/transformed/bill_to_side.xlsx')
    bill_to_side

    KNS_Bill = pd.read_excel(
        '../data/raw/KNS_Bill.xlsx',
        index_col=0)
    KNS_Bill = KNS_Bill[['BillID', 'Name', 'StatusID']]
    KNS_Bill.rename(columns={'BillID': 'bill_id', 'Name': 'name', 'StatusID': 'status_id'}, inplace=True)
    KNS_Bill['passed_third'] = KNS_Bill['status_id'].apply(lambda x: True if x == 118 else False)
    KNS_Bill.drop(columns=['status_id'], inplace=True)
    KNS_Bill

    bill = KNS_Bill.set_index(
        ['bill_id']).join(
            bill_to_side.set_index(
                ['bill_id']), how='left')
    bill.reset_index(inplace=True)
    bill.to_excel(
        '../data/model/dimensions/bill.xlsx',
        sheet_name='bill',
        index=False)
    bill