import pandas as pd


def bill_to_type():
    """
    Creates bill_to_type table from bill_sponsors.
    """

    # ----- load -----
    bill_sponsors = pd.read_csv(
        '../data/transformed/bill_sponsors.csv', parse_dates=['date'])
    bill_sponsors = bill_sponsors[['bill_id', 'person_side', 'person_id']]
    bill_sponsors = bill_sponsors[bill_sponsors['bill_id'].notnull()]
    bill_sponsors['person_side'] = bill_sponsors['person_side'].astype(str)
    bill_sponsors['bill_id'] = bill_sponsors['bill_id'].astype('int64')
    bill_sponsors

    # fill-in missing side data here

    # ----- missing side data -----
    missing_side_data = bill_sponsors[bill_sponsors['person_side'] == 'nan']
    missing_side_bill_ids = set(missing_side_data['bill_id'])
    missing_side_data = bill_sponsors[bill_sponsors['bill_id'].isin(missing_side_bill_ids)]
    missing_side_data = missing_side_data.pivot_table(index='bill_id',
        columns='person_side', values='person_id', aggfunc='nunique').reset_index()
    missing_side_data_w_unclear_bill_type = missing_side_data[(missing_side_data['opposition']).isnull() | (missing_side_data['coalition']).isnull()]

    missing_side_data_w_unclear_bill_type.to_excel(
        '../data/reports/missing_side_data_w_unclear_bill_type.xlsx',
        sheet_name='missing_side_data_w_unclear_bill_type', index=False)

    # # ----- records to exclude -----
    unclear_bill_type_ids = set(missing_side_data_w_unclear_bill_type['bill_id'])
    unclear_bill_type_ids

    # ----- logic definition -----
    bill_to_type = bill_sponsors[bill_sponsors['bill_id'].isin(unclear_bill_type_ids) == False]
    bill_to_type = bill_to_type.pivot_table(index='bill_id', columns='person_side', values='person_id', aggfunc='nunique').reset_index()
    bill_to_type.drop(columns='nan', inplace=True)
    bill_to_type['bill_type'] = 'bipartisan'
    bill_to_type['bill_type'][bill_to_type['opposition'].isnull() | bill_to_type['coalition'].isnull()] = 'single-sided'

    bill_to_type


    # ----- save -----
    bill_to_type = bill_to_type[['bill_id', 'bill_type']].drop_duplicates()
    bill_to_type.to_excel(
        '../data/transformed/bill_to_type.xlsx', index=False)
    bill_to_type