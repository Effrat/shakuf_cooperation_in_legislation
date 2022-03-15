import pandas as pd

def bill_to_date():
    """
    Creates bill_to_date table from bill_to_date_from_commettee_session and bill_to_date_from_session.
    """
    bill_to_date_from_commettee_session = pd.read_excel(
        '../data/transformed/bill_to_date_from_commettee_session.xlsx',
        parse_dates=['date'])

    bill_to_date_from_session = pd.read_excel(
        '../data/transformed/bill_to_date_from_session.xlsx',
        parse_dates=['date'])

    bill_to_date = pd.concat([
        bill_to_date_from_commettee_session,
        bill_to_date_from_session])

    bill_to_date = bill_to_date.groupby('bill_id').agg('min').reset_index()
    bill_to_date['date'] = bill_to_date['date'].dt.date

    bill_to_date.to_excel(
        '../data/transformed/bill_to_date.xlsx',
        sheet_name='bill_to_date', index=False)