import pandas as pd


def bill_to_side():
    """
    Creates bill_to_side table from bill_sponsors.
    """
    bill_sponsors = pd.read_csv(
        '../data/model/facts/bill_sponsors.csv', parse_dates=['date'])
    bill_sponsors.groupby('is_initiator').nunique()
    bill_sponsors['person_side'] = bill_sponsors['person_side'].astype(str)

    initiators = bill_sponsors[bill_sponsors['is_initiator'] == True]
    initiators = initiators[['bill_id', 'person_id', 'person_side']]
    initiators['person_side'].fillna('unknown', inplace=True)

    bill_to_side = initiators.groupby(['bill_id', 'person_side']).nunique().reset_index()
    bill_to_side = bill_to_side.pivot(index='bill_id', columns='person_side', values='person_id')
    bill_to_side['total'] = bill_to_side.sum(axis=1)
    bill_to_side['bill_side'] = 'unknown'
    bill_to_side['bill_side'][bill_to_side['coalition'] > bill_to_side['total'] / 2] = 'coalition'
    bill_to_side['bill_side'][bill_to_side['opposition'] > bill_to_side['total'] / 2] = 'opposition'
    bill_to_side['bill_side'][bill_to_side['coalition'] == bill_to_side['opposition']] = 'bipartisan'
    bill_to_side = bill_to_side[['bill_side']].reset_index('bill_id')

    bill_to_side.to_excel(
        '../data/transformed/bill_to_side.xlsx', index=False)