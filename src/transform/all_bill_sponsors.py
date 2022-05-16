import pandas as pd


def all_bill_sponsors():
    """
    Creates all_bill_initiators table from KNS_BillInitiator and KNS_BillHistoryInitiator.
    """
    # ----- load -----
    KNS_BillInitiator = pd.read_excel(
        '../data/raw/KNS_BillInitiator.xlsx',
        index_col=0)
    KNS_BillInitiator.drop(columns=['BillInitiatorID', 'LastUpdatedDate', 'Ordinal', 'IsInitiator'], inplace=True)
    KNS_BillInitiator.columns = ['bill_id', 'person_id']

    KNS_BillHistoryInitiator = pd.read_excel(
        '../data/raw/KNS_BillHistoryInitiator.xlsx',
        index_col=0)
    KNS_BillHistoryInitiator.drop(columns=[
        'BillHistoryInitiatorID', 'StartDate', 'EndDate',
        'ReasonID', 'ReasonDesc', 'LastUpdatedDate', 'IsInitiator'], inplace=True)
    KNS_BillHistoryInitiator.columns = ['bill_id', 'person_id']

    # ----- transform -----
    all_bill_sponsors = pd.concat([KNS_BillInitiator, KNS_BillHistoryInitiator])
    all_bill_sponsors = all_bill_sponsors.groupby(['bill_id', 'person_id']).agg('max')
    all_bill_sponsors.reset_index(inplace=True)

    # ----- save -----
    all_bill_sponsors.to_excel(
        '../data/transformed/all_bill_sponsors.xlsx',
        sheet_name='all_bill_sponsors', index=False)
