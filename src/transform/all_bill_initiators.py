import pandas as pd


# def all_bill_initiators():
#     """"
#     """
# members_of_knesset_faction_and_side_by_date = pd.read_csv(
#     '../data/transformed/members_of_knesset_faction_and_side_by_date.csv')
# members_of_knesset_faction_and_side_by_date['date'] = pd.to_datetime(
#     members_of_knesset_faction_and_side_by_date['date'])
# print(members_of_knesset_faction_and_side_by_date.info())
# members_of_knesset_faction_and_side_by_date.info()
# bill_to_date = pd.read_excel(
#     '../data/transformed/bill_to_date.xlsx',
#     parse_dates=['date'])
# bill_to_date
# print(bill_to_date.info())

KNS_BillInitiator = pd.read_excel(
    '../../data/raw/KNS_BillInitiator.xlsx',
    index_col=0)
KNS_BillInitiator.drop(columns=['BillInitiatorID', 'LastUpdatedDate', 'Ordinal'], inplace=True)
KNS_BillInitiator.columns = ['bill_id', 'person_id', 'is_initiator']
KNS_BillInitiator['is_initiator'].fillna(False, inplace=True)
KNS_BillInitiator['is_initiator'] = KNS_BillInitiator['is_initiator'].astype(bool)
KNS_BillInitiator
print(KNS_BillInitiator.info())
KNS_BillInitiator

KNS_BillHistoryInitiator = pd.read_excel(
    '../../data/raw/KNS_BillHistoryInitiator.xlsx',
    index_col=0)
KNS_BillHistoryInitiator.drop(columns=[
    'BillHistoryInitiatorID',
    'StartDate',
    'EndDate',
    'ReasonID',
    'ReasonDesc',
    'LastUpdatedDate'], inplace=True)
KNS_BillHistoryInitiator.columns = ['bill_id', 'person_id', 'is_initiator']
KNS_BillHistoryInitiator['is_initiator'].fillna(False, inplace=True)
KNS_BillHistoryInitiator['is_initiator'] = KNS_BillHistoryInitiator['is_initiator'].astype(bool)
KNS_BillHistoryInitiator
print(KNS_BillHistoryInitiator.info())
KNS_BillHistoryInitiator

all_bills_initiators = pd.concat([KNS_BillInitiator, KNS_BillHistoryInitiator])
all_bills_initiators = all_bills_initiators.groupby(['bill_id', 'person_id']).agg('max')
all_bills_initiators.reset_index(inplace=True)
all_bills_initiators.to_excel(
    '../../data/transformed/all_bills_initiators.xlsx',
    sheet_name='all_bills_initiators',
    index=False)
all_bills_initiators
