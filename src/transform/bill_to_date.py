import pandas as pd

def bill_to_date():
    """
    This function assigns a date to each bill,
    according to the first plenum session for which the bill was to be discussed.
    """
    KNS_PlmSessionItem = pd.read_excel('../data/raw/KNS_PlmSessionItem.xlsx', index_col=0)
    KNS_PlmSessionItem
    # ---- filter only bills
    bills_sessions = KNS_PlmSessionItem[KNS_PlmSessionItem['ItemTypeID'] == 2][['ItemID', 'PlenumSessionID']]
    bills_sessions.columns = ['bill_id', 'session_id']
    bills_sessions = bills_sessions.groupby('bill_id').agg('min').reset_index()
    bills_sessions

    KNS_PlenumSession = pd.read_excel('../data/raw/KNS_PlenumSession.xlsx', index_col=0)
    KNS_PlenumSession
    session_to_date = KNS_PlenumSession[['PlenumSessionID', 'StartDate']]
    session_to_date.columns = ['session_id', 'date']
    session_to_date

    bill_to_date = pd.merge(bills_sessions, session_to_date, on='session_id', how='left')
    bill_to_date = bill_to_date.drop(columns=['session_id'])
    bill_to_date['date'] = pd.to_datetime(bill_to_date['date'])
    bill_to_date['date'] = bill_to_date['date'].dt.date

    bill_to_date.to_excel(
        '../data/transformed/bill_to_date.xlsx',
        sheet_name='bill_to_date',
        index=False
    )
    bill_to_date