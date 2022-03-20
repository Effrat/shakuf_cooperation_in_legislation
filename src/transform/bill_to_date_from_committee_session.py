import pandas as pd

def bill_to_date_from_committee_session():
    """
    Creates bill_to_date_from_committee_session table from KNS_CmtSessionItem and KNS_CommitteeSession.
    """

    # ----- load -----
    KNS_CommitteeSession = pd.read_excel(
        '../data/raw/KNS_CommitteeSession.xlsx',
        parse_dates=['StartDate'], index_col=0)
    KNS_CommitteeSession
    committee_session_to_date = KNS_CommitteeSession[['CommitteeSessionID', 'StartDate']]
    committee_session_to_date.columns = ['session_id', 'date']

    KNS_CmtSessionItem = pd.read_excel(
        '../data/raw/KNS_CmtSessionItem.xlsx', index_col=0)  
    bills_committee_sessions = KNS_CmtSessionItem[KNS_CmtSessionItem['ItemTypeID'] == 2] # filter only bills
    bills_committee_sessions = bills_committee_sessions[['ItemID', 'CommitteeSessionID']]
    bills_committee_sessions.columns = ['bill_id', 'session_id']
    bills_committee_sessions = bills_committee_sessions.groupby('bill_id').agg('min').reset_index()

    # ----- transform -----
    bill_to_date_from_committee_session = pd.merge(
        committee_session_to_date, bills_committee_sessions,
        on='session_id', how='right')
    bill_to_date_from_committee_session = bill_to_date_from_committee_session.drop(columns=['session_id'])
    bill_to_date_from_committee_session['date'] = bill_to_date_from_committee_session['date'].dt.date

    # ----- testing/feedback -----
    nan_dates_from_session = bill_to_date_from_committee_session[bill_to_date_from_committee_session['date'].isnull()]
    nan_dates_from_session.to_csv('../data/reports/nan_dates_from_committee_session.csv', index=False)


    # ----- save -----
    bill_to_date_from_committee_session.to_excel(
        '../data/transformed/bill_to_date_from_committee_session.xlsx',
        sheet_name='bill_to_date_from_committee_session',
        index=False)
