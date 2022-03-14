import pandas as pd
import plotly.express as px
from datetime import datetime


now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def bill_test():
    """
    """
    bill = pd.read_excel('../data/model/dimensions/bill.xlsx')
    bill

    # check for bills without 'bill_side' data
    # count distinct missing for each 'knesset_num'
    bills_count_wo_side_by_knesset = bill[pd.isna(
        bill['bill_side'])].groupby(
            ['knesset_num']).nunique()['bill_id']
    fig = px.bar(
        bills_count_wo_side_by_knesset,
        title=f'Total bills without bill_side {now}')
    fig.write_html(f'../../data/reports/bill_test_no_side_{now}.html')
    fig.show()

    # check for bills without 'passed_third' data
    # count distinct missing for each 'knesset_num'
    bills_count_wo_passed_third_by_knesset = bill[pd.isna(
        bill['passed_third'])].groupby(
            ['knesset_num']).nunique()['bill_id']
    fig = px.bar(
        bills_count_wo_passed_third_by_knesset,
        title=f'Total bills without passed_third {now}')
    fig.write_html(f'../data/reports/bill_test_no_passed_{now}.html')
    fig.show()