import pandas as pd
from datetime import datetime
import plotly.express as px


def members_of_knesset_by_date_test():
    """
    """
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    members_of_knesset_by_date = pd.read_csv(
        '../data/transformed/members_of_knesset_by_date.csv',
        parse_dates=['date'])
    members_of_knesset_by_date

    count_mks_by_date = members_of_knesset_by_date.groupby('date').nunique()[['person_id']]
    count_mks_by_date['missing_mks'] = 120 - count_mks_by_date['person_id']
    count_mks_by_date.drop(['person_id'], axis=1, inplace=True)
    count_mks_by_date = count_mks_by_date['1949-02-14':]


    fig = px.area(
        count_mks_by_date,
        title=f'Total missing memebers of knesset {now}')
    fig.write_html(f'../data/reports/missing_mks_{now}.html')
    fig.show()