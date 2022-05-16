import pandas as pd

def all_bill_sponsors_to_date():
    """
    Creates all_bill_sponsors_to_date table from bill_to_date and all_bills_sponsors.
    """

    
    # ----- load -----
    bill_to_date = pd.read_excel(
        '../data/transformed/bill_to_date.xlsx',
        parse_dates=['date'])
    bill_to_date

    all_bills_sponsors = pd.read_excel(
        '../data/transformed/all_bill_sponsors.xlsx')
    all_bills_sponsors


    # ----- testing/feedback -----
    all_bill_sponsors_to_date = pd.merge(
        bill_to_date, all_bills_sponsors, on='bill_id', how='outer')
    all_bill_sponsors_to_date

    # bills w/ sponsors w/o dates
    bills_w_sponsors_wo_dates = all_bill_sponsors_to_date[all_bill_sponsors_to_date['date'].isnull()]
    bills_w_sponsors_wo_dates = bills_w_sponsors_wo_dates[['bill_id']].drop_duplicates()
    bills_w_sponsors_wo_dates.to_csv(
        '../data/reports/bills_w_sponsors_wo_dates.csv', index=False)

    # bills w/ dates w/ missing sponsors data
    bills_w_date_wo_sponsors = all_bill_sponsors_to_date[all_bill_sponsors_to_date['person_id'].isnull()]
    bills_w_date_wo_sponsors = bills_w_date_wo_sponsors[['bill_id']].drop_duplicates()
    bills_w_date_wo_sponsors.to_csv(
        '../data/reports/bills_w_date_wo_sponsors.csv', index=False)
    bills_w_date_wo_sponsors['bill_id'].values.tolist()



    # ----- transform -----
    all_bill_sponsors_to_date = pd.merge(
        bill_to_date, all_bills_sponsors, on='bill_id', how='inner')
    all_bill_sponsors_to_date



    # ----- save -----
    all_bill_sponsors_to_date.to_excel(
        '../data/transformed/all_bill_sponsors_to_date.xlsx',
        sheet_name='all_bill_sponsors_to_date', index=False)
    all_bill_sponsors_to_date