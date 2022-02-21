import pandas as pd


def bill_initiators():
    """"
    Create a table of bill initiators for the FE data model.
    """
    members_of_knesset_faction_and_side_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_faction_and_side_by_date.csv')
    members_of_knesset_faction_and_side_by_date['date'] = pd.to_datetime(
        members_of_knesset_faction_and_side_by_date['date'])
    # print(members_of_knesset_faction_and_side_by_date.info())
    # members_of_knesset_faction_and_side_by_date.info()
    bill_to_date = pd.read_excel(
        '../data/transformed/bill_to_date.xlsx',
        parse_dates=['date'])
    bill_to_date
    print(bill_to_date.info())

    KNS_BillInitiator = pd.read_excel(
        '../data/raw/KNS_BillInitiator.xlsx',
        index_col=0)
    KNS_BillInitiator.drop(columns=['BillInitiatorID', 'LastUpdatedDate', 'Ordinal'], inplace=True)
    KNS_BillInitiator.columns = ['bill_id', 'person_id', 'is_initiator']
    KNS_BillInitiator['is_initiator'].fillna(False, inplace=True)
    KNS_BillInitiator['is_initiator'] = KNS_BillInitiator['is_initiator'].astype(bool)
    KNS_BillInitiator
    print(KNS_BillInitiator.info())
    KNS_BillInitiator.info()

    bill_initiators = KNS_BillInitiator.set_index(
        'bill_id').join(bill_to_date.set_index('bill_id'), how='left')
    bill_initiators.reset_index(inplace=True)
    bill_initiators

    print(bill_initiators.info())
    bill_initiators = bill_initiators.set_index(
        ['date', 'person_id']).join(
            members_of_knesset_faction_and_side_by_date.set_index(
                ['date', 'person_id']), how='left')
    bill_initiators.reset_index(inplace=True)
    bill_initiators['faction_id'] = bill_initiators['faction_id'].fillna(0)
    bill_initiators['faction_id'] = bill_initiators['faction_id'].astype('Int64')
    bill_initiators.to_csv(
        '../data/model/facts/bill_initiators.csv',
        index=False)
    bill_initiators