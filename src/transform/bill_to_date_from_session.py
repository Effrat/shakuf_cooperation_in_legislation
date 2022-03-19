import pandas as pd

def bill_to_date_from_session():
    """
    Creates bill_to_date_from_session table from KNS_PlenumSession and KNS_PlmSessionItem.
    Outputs report: '../data/reports/nan_dates_from_session.csv'
    """

    # ----- load -----
    KNS_PlenumSession = pd.read_excel(
        '../data/raw/KNS_PlenumSession.xlsx',
        parse_dates=['StartDate'], index_col=0)
    session_to_date = KNS_PlenumSession[['PlenumSessionID', 'StartDate']]
    session_to_date.columns = ['session_id', 'date']
    session_to_date['date'] = session_to_date['date'].dt.date
    session_to_date

    KNS_PlmSessionItem = pd.read_excel(
        '../data/raw/KNS_PlmSessionItem.xlsx', index_col=0)
    bills_sessions = KNS_PlmSessionItem[KNS_PlmSessionItem['ItemTypeID'] == 2] # filter only bills
    bills_sessions = bills_sessions[['ItemID', 'PlenumSessionID']]
    bills_sessions.columns = ['bill_id', 'session_id']
    bills_sessions = bills_sessions.groupby('bill_id').agg('min').reset_index()
    bills_sessions


    # ----- transform -----
    bill_to_date_from_session = pd.merge(
        session_to_date, bills_sessions,
        on='session_id', how='right')
    bill_to_date_from_session = bill_to_date_from_session.drop(columns=['session_id'])
    bill_to_date_from_session


    # ----- testing/feedback -----
    nan_dates_from_session = bill_to_date_from_session[bill_to_date_from_session['date'].isnull()]
    nan_dates_from_session.to_csv('../data/reports/nan_dates_from_session.csv', index=False)


    # ----- save -----
    bill_to_date_from_session.to_excel(
        '../data/transformed/bill_to_date_from_session.xlsx',
        sheet_name='bill_to_date_from_session', index=False)