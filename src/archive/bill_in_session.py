import pandas as pd
import numpy as np
# from datetime.datetime import timedelta

# =========================     import plenum sessions and session items     =========================
KNS_PlenumSession = pd.read_csv(
    '..\..\data\\raw\KNS_PlenumSession.csv',
    index_col='PlenumSessionID',
    parse_dates=['StartDate'],
    )
KNS_PlmSessionItem = pd.read_csv(
    '..\..\data\\raw\KNS_PlmSessionItem.csv',
    index_col='plmPlenumSessionID'
    )

# =========================     filter only bills and join by session id     =========================
bills_sessions = KNS_PlmSessionItem[KNS_PlmSessionItem['ItemTypeID'] == 2][['ItemID', 'PlenumSessionID']]
bills_sessions = bills_sessions.reset_index(drop=True).set_index('PlenumSessionID')
bills_sessions = bills_sessions.join(KNS_PlenumSession[['StartDate']], how='left')


# =========================     cleanup dates     =========================
bills_sessions.columns = ['BillID', 'Date']
bills_sessions['Date'] = bills_sessions['Date'].dt.date
starts = bills_sessions.groupby('BillID').min()
starts.columns = ['StartDate']
ends = bills_sessions.groupby('BillID').max()
ends.columns = ['EndDate']
bill_in_session = starts.join(ends, how='outer')


# =========================     export     =========================
bill_in_session.to_csv('..\..\data\\to_powerbi\\bill_in_session.csv', index='BillID')
bill_in_session


# bill_in_session['days'] = (bill_in_session['EndDate'] - bill_in_session['StartDate']) / np.timedelta64(1, 'D')
bill_in_session#['days']#.value_counts()