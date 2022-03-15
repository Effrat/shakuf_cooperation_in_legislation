import pandas as pd

def bill_to_date_from_commettee_session():
    """
    Creates bill_to_date_from_commettee_session table from KNS_CmtSessionItem and KNS_CommitteeSession.
    """
    KNS_CmtSessionItem = pd.read_excel(
        '../data/raw/KNS_CmtSessionItem.xlsx',
        index_col=0)
    KNS_CmtSessionItem
    # ---- filter only bills
    bills_commettee_sessions = KNS_CmtSessionItem[KNS_CmtSessionItem['ItemTypeID'] == 2][['ItemID', 'CommitteeSessionID']]
    bills_commettee_sessions.columns = ['bill_id', 'session_id']
    bills_commettee_sessions = bills_commettee_sessions.groupby('bill_id').agg('min').reset_index()
    bills_commettee_sessions

    KNS_CommitteeSession = pd.read_excel(
        '../data/raw/KNS_CommitteeSession.xlsx',
        parse_dates=['StartDate'], index_col=0)
    KNS_CommitteeSession
    commettee_session_to_date = KNS_CommitteeSession[['CommitteeSessionID', 'StartDate']]
    commettee_session_to_date.columns = ['session_id', 'date']
    commettee_session_to_date

    bill_to_date_from_commettee_session = pd.merge(
        bills_commettee_sessions, commettee_session_to_date,
        on='session_id', how='left')
    bill_to_date_from_commettee_session = bill_to_date_from_commettee_session.drop(columns=['session_id'])
    bill_to_date_from_commettee_session['date'] = bill_to_date_from_commettee_session['date'].dt.date

    bill_to_date_from_commettee_session.to_excel(
        '../data/transformed/bill_to_date_from_commettee_session.xlsx',
        sheet_name='bill_to_date_from_commettee_session',
        index=False)
    bill_to_date_from_commettee_session