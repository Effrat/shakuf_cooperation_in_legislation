import pandas as pd


def bill_to_side():
    """
    Creates bill_to_side table from bill_sponsors.
    """

    # ----- load -----
    bill_sponsors = pd.read_csv(
        '../data/model/facts/bill_sponsors.csv', parse_dates=['date'])
    bill_sponsors.groupby('is_initiator').nunique()
    bill_sponsors['person_side'] = bill_sponsors['person_side'].astype(str)
    bill_sponsors



    # ----- transform -----
    initiators = bill_sponsors[bill_sponsors['is_initiator'] == True]
    initiators = initiators[['bill_id', 'person_id', 'person_side']]
    initiators['person_side'].fillna('unknown', inplace=True)
    initiators

    bill_to_side = initiators.groupby(['bill_id', 'person_side']).nunique().reset_index()
    bill_to_side = bill_to_side.pivot_table(
        index='bill_id', columns='person_side', values='person_id', aggfunc='nunique')
    bill_to_side.reset_index(inplace=True)



    # ----- records to exclude -----
    nans_in_bill_sponsors_side = bill_to_side[bill_to_side['nan'].notnull()]
    nans_in_bill_sponsors_side.to_csv(
        '../data/reports/nans_in_bill_sponsors_side.csv', index=False)
    nans_in_bill_sponsors_side

    bills_to_drop = nans_in_bill_sponsors_side['bill_id'].drop_duplicates().values.tolist()
    bills_to_drop

    # ----- logic definition -----
    bill_to_side = bill_to_side[bill_to_side['bill_id'].isin(bills_to_drop) == False]
    bill_to_side['total'] = bill_to_side.sum(axis=1)
    bill_to_side['bill_side'] = 'unknown'
    bill_to_side['bill_side'][bill_to_side['coalition'] > bill_to_side['total'] / 2] = 'coalition'
    bill_to_side['bill_side'][bill_to_side['opposition'] > bill_to_side['total'] / 2] = 'opposition'
    bill_to_side['bill_side'][bill_to_side['coalition'] == bill_to_side['opposition']] = 'bipartisan'
    bill_to_side['bill_side'][bill_to_side['nan'] >= bill_to_side['total'] / 2] = 'unknown'
    bill_to_side





    # ----- save -----
    bill_to_side = bill_to_side[['bill_id', 'bill_side']].drop_duplicates()
    bill_to_side.to_excel(
        '../data/transformed/bill_to_side.xlsx', index=False)