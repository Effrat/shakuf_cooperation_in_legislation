from datetime import date
import pandas as pd

def bill_to_date():
    """
    Creates bill_to_date table from bill_to_date_from_committee_session and bill_to_date_from_session.
    """
    # ----- load -----
    bill_to_date_from_committee_session = pd.read_excel(
        '../data/transformed/bill_to_date_from_committee_session.xlsx',
        parse_dates=['date'])

    bill_to_date_from_session = pd.read_excel(
        '../data/transformed/bill_to_date_from_session.xlsx',
        parse_dates=['date'])

    # ----- transform -----
    bill_to_date = pd.concat([
        bill_to_date_from_committee_session,
        bill_to_date_from_session])

    bill_to_date = bill_to_date.groupby('bill_id').agg('min').reset_index()
    # ids = bill_to_date[(bill_to_date['date'] >= '2021-04-07') & (bill_to_date['date'] < '2021-06-16')]['bill_id'].values
    # bill_to_date['date'][bill_to_date['bill_id'].isin(ids)] = '2021-06-16'
    # bill_to_date['date'] = bill_to_date['date'].dt.date
    # bill_to_date[bill_to_date['bill_id'].isin(ids)]

    # ----- save -----
    bill_to_date.to_excel(
        '../data/transformed/bill_to_date.xlsx',
        sheet_name='bill_to_date', index=False)