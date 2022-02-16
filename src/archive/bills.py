import pandas as pd

# bill_initiators_side = pd.read_excel('..\..\data\\precursors\\bill_initiators_side.xlsx', index_col='BillID')
# bill_initiators_side = bill_initiators_side[['InitiatorsSide']]

# bill_to_date_to_mk = pd.read_excel('..\..\data\\precursors\\bill_to_date_to_mk.xlsx', index_col='BillID')
# bill_to_date_to_mk = bill_to_date_to_mk[['Date']]

# bill = bill_initiators_side.join(bill_to_date_to_mk, how='inner')
# bill

KNS_Bill = pd.read_excel('../../data/raw/KNS_Bill.xlsx')
bills = KNS_Bill[['BillID', 'Name', 'StatusID']]
bills.to_excel(
    '../../data/to_powerbi/bill.xlsx',
    sheet_name='bills',
    header=True,
    )
bills

# bill = bill.join(KNS_Bill, how='inner')
# bill.to_excel('..\..\data\\to_powerbi\\bill.xlsx', header=True)
# bill
