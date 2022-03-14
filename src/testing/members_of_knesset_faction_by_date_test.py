import pandas as pd
import plotly.express as px
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

members_of_knesset_faction_by_date = pd.read_csv(
    '../../data/transformed/members_of_knesset_faction_by_date.csv',
    parse_dates=['date'])
members_of_knesset_faction_by_date

# ----- filter data for 24th Knesset only
start_date_k24 = '2021-04-06'
members_of_knesset_faction_by_date = members_of_knesset_faction_by_date[members_of_knesset_faction_by_date['date'] >= start_date_k24]
members_of_knesset_faction_by_date

total_mks = members_of_knesset_faction_by_date.groupby(['date', 'faction_id'])[['person_id']].nunique().reset_index()
total_mks

fig = px.area(total_mks, color='faction_id',
    x='date', y='person_id',
    title=f'Total Members of Knesset by Faction {now}')
fig.write_html(f'../../data/reports/members_of_knesset_faction_by_date_test_{now}.html', auto_open=True)
fig.show()
