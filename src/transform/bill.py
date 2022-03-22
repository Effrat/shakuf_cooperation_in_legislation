import pandas as pd

def bill():
    """
    Creates bill table from bill_to_side and KNS_Bill.
    """


    # ----- load -----
    bill_to_side = pd.read_excel(
        '../data/transformed/bill_to_side.xlsx')
    bill_to_side


    KNS_Bill = pd.read_excel(
        '../data/raw/KNS_Bill.xlsx',
        index_col=0)
    KNS_Bill = KNS_Bill[['BillID', 'Name', 'KnessetNum', 'StatusID']]
    KNS_Bill.rename(columns={'BillID': 'bill_id', 'Name': 'name', 'KnessetNum': 'knesset_num', 'StatusID': 'status_id'}, inplace=True)
    KNS_Bill['passed_third'] = KNS_Bill['status_id'].apply(lambda x: True if x == 118 else False)
    KNS_Bill.drop(columns=['status_id'], inplace=True)
    KNS_Bill



    # ----- transform -----
    bill = pd.merge(bill_to_side, KNS_Bill, on=['bill_id'], how='left')



    # ----- save -----
    bill.to_excel(
        '../data/model/dimensions/bill.xlsx',
        sheet_name='bill', index=False)
    bill