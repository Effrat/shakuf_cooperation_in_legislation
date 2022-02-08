import numpy as np
import pandas as pd



# --------- bills to initiator/joiner by first date of plenum item
# --------- see how many initiators/joiners are not included if filtering by the first date

# --------- import raw plenum items and filter by bills 
# KNS_PlmSessionItem = pd.read_excel('..\..\data\\raw\KNS_PlmSessionItem.xlsx', index_col=0)
# plenum_items_bills = KNS_PlmSessionItem[KNS_PlmSessionItem['ItemTypeID'] == 2]
# --------- for faster performance
# plenum_items_bills = plenum_items_bills[['PlenumSessionID', 'ItemID']]
# session_to_bills = plenum_items_bills.rename(columns={'ItemID': 'BillID'})
# # session_to_bills = plenum_items_bills.groupby('BillID').min()
# # session_to_bills = session_to_bills.reset_index()
# session_to_bills.to_excel('..\..\data\\precursors\session_to_bills.xlsx', header=True)
session_to_bills = pd.read_excel('..\..\data\\precursors\session_to_bills.xlsx', index_col=0)
session_to_bills

# --------- import raw plenum sessions to get dates
KNS_PlenumSession = pd.read_excel('..\..\data\\raw\KNS_PlenumSession.xlsx', index_col=0, parse_dates=['StartDate'])
sessions_to_dates = KNS_PlenumSession[['PlenumSessionID', 'StartDate', 'KnessetNum']]
sessions_to_dates['StartDate'] = sessions_to_dates['StartDate'].dt.date
# sessions_to_dates.groupby('PlenumSessionID').min()
sessions_to_dates

# --------- group by bill ID, aggregate earliest start date
bills_to_sessions_first_date = session_to_bills.set_index('PlenumSessionID').join(sessions_to_dates.set_index('PlenumSessionID'))
bills_to_sessions_first_date = bills_to_sessions_first_date.groupby('BillID').min()
bills_to_sessions_first_date.rename(columns={'StartDate': 'Date'}, inplace=True)
bills_to_sessions_first_date


# join bill initiator, left and inner - see the difference
KNS_BillInitiator = pd.read_excel('..\..\data\\raw\KNS_BillInitiator.xlsx', index_col=0)
KNS_BillInitiator['IsInitiator'].fillna(0, inplace=True)

left_initiators_to_bills = KNS_BillInitiator[['BillID', 'PersonID', 'IsInitiator', 'Ordinal']].set_index('BillID').join(bills_to_sessions_first_date, how='left')
left_initiators_to_bills
print(left_initiators_to_bills)
errors = len(left_initiators_to_bills[(left_initiators_to_bills['Date']).isna()]) / len(left_initiators_to_bills)
print(f'missing dates: {errors}')
missing_dates_for_sessions = left_initiators_to_bills[(left_initiators_to_bills['Date']).isna()].reset_index()
print(missing_dates_for_sessions)
missing_dates_for_sessions.to_excel('..\..\data\\logs\missing_dates_for_sessions.xlsx', header=True)

inner_initiators_to_bills = left_initiators_to_bills.dropna()
inner_initiators_to_bills.to_excel('..\..\data\\precursors\inner_initiators_to_bills.xlsx', header=True)