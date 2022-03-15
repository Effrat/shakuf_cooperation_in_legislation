import pandas as pd

def bill_to_date_from_committee_session():
    """
    Creates bill_to_date_from_committee_session table from KNS_CmtSessionItem and KNS_CommitteeSession.
    """
    KNS_CmtSessionItem = pd.read_excel(
        '../data/raw/KNS_CmtSessionItem.xlsx', index_col=0)

    # ---- filter only bills
    bills_committee_sessions = KNS_CmtSessionItem[KNS_CmtSessionItem['ItemTypeID'] == 2][['ItemID', 'CommitteeSessionID']]
    bills_committee_sessions.columns = ['bill_id', 'session_id']
    bills_committee_sessions = bills_committee_sessions.groupby('bill_id').agg('min').reset_index()

    KNS_CommitteeSession = pd.read_excel(
        '../data/raw/KNS_CommitteeSession.xlsx',
        parse_dates=['StartDate'], index_col=0)
    KNS_CommitteeSession
    committee_session_to_date = KNS_CommitteeSession[['CommitteeSessionID', 'StartDate']]
    committee_session_to_date.columns = ['session_id', 'date']

    bill_to_date_from_committee_session = pd.merge(
        bills_committee_sessions, committee_session_to_date,
        on='session_id', how='left')
    bill_to_date_from_committee_session = bill_to_date_from_committee_session.drop(columns=['session_id'])
    bill_to_date_from_committee_session['date'] = bill_to_date_from_committee_session['date'].dt.date

    bill_to_date_from_committee_session.to_excel(
        '../data/transformed/bill_to_date_from_committee_session.xlsx',
        sheet_name='bill_to_date_from_committee_session',
        index=False)
