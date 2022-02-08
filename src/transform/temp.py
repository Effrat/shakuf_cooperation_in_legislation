#TODO: break into functions

import pandas as pd




# ===================   import   ===================
KNS_BillInitiator = pd.read_excel('..\..\data\\raw\\KNS_BillInitiator.xlsx', index_col=0)
KNS_BillInitiator['IsInitiator'].replace(1, 'Initiator', inplace=True)
KNS_BillInitiator['IsInitiator'].fillna('Not Initiator', inplace=True)
KNS_BillInitiator.rename(columns={'IsInitiator': 'Initiator'}, inplace=True)
KNS_BillInitiator.drop(['LastUpdatedDate'], axis=1, inplace=True)
KNS_BillInitiator

members_of_knesset_by_faction_and_side = pd.read_csv(
    '..\..\data\\expanded\\members_of_knesset_by_faction_and_side.csv',
    parse_dates=['Date'],
    index_col=0
)
members_of_knesset_by_faction_and_side

bill = pd.read_excel('..\..\data\\to_powerbi\\bill.xlsx')
bill = bill[['BillID', 'Date', 'InitiatorsSide']]
bill


# ===================     transformations   ===================
bill_initiators = bill.set_index('BillID').join(KNS_BillInitiator.set_index('BillID'), how='left')
bill_initiators.reset_index(inplace=True)
bill_initiators

bill_initiators = bill_initiators.set_index(['PersonID', 'Date']).join(
    members_of_knesset_by_faction_and_side.set_index(['PersonID', 'Date']), how='left')
bill_initiators.reset_index(inplace=True)
bill_initiators.drop_duplicates(subset=['BillInitiatorID'], inplace=True)
bill_initiators.to_excel(
    '..\..\data\\to_powerbi\\bill_initiators.xlsx',
    sheet_name='bill_initiators',
    header=True
    )
bill_initiators