import pandas as pd

def bill_to_date_from_session():
    """
    """
    KNS_PlmSessionItem = pd.read_excel(
        '../data/raw/KNS_PlmSessionItem.xlsx',
        index_col=0)
    KNS_PlmSessionItem
    # ---- filter only bills
    bills_sessions = KNS_PlmSessionItem[KNS_PlmSessionItem['ItemTypeID'] == 2][['ItemID', 'PlenumSessionID']]
    bills_sessions.columns = ['bill_id', 'session_id']
    bills_sessions = bills_sessions.groupby('bill_id').agg('min').reset_index()
    bills_sessions

    KNS_PlenumSession = pd.read_excel(
        '../data/raw/KNS_PlenumSession.xlsx',
        parse_dates=['StartDate'], index_col=0)
    session_to_date = KNS_PlenumSession[['PlenumSessionID', 'StartDate']]
    session_to_date.columns = ['session_id', 'date']
    session_to_date

    bill_to_date_from_session = bills_sessions.set_index(
        'session_id').join(
            session_to_date.set_index(
                'session_id'), how='left')
    bill_to_date_from_session.reset_index(inplace=True)
    bill_to_date_from_session = bill_to_date_from_session.drop(columns=['session_id'])
    bill_to_date_from_session['date'] = bill_to_date_from_session['date'].dt.date

    bill_to_date_from_session.to_excel(
        '../data/transformed/bill_to_date_from_session.xlsx',
        sheet_name='bill_to_date_from_session',
        index=False)
    bill_to_date_from_session