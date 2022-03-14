import pandas as pd
from datetime import datetime
import plotly.express as px


# def faction_side_by_date_test():
#     """
#     """
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

faction_side_by_date = pd.read_csv(
    '../../data/transformed/faction_side_by_date.csv',
    parse_dates=['date'])
faction_side_by_date

count_factions_by_side_and_date = faction_side_by_date.groupby(['date', 'faction_side']).nunique()
count_factions_by_side_and_date.reset_index(inplace=True)
# count_factions_by_side_and_date.pivot(index='date', columns='faction_side', values='faction_id')

fig = px.area(count_factions_by_side_and_date, x='date', y='faction_id', color='faction_side')
fig.update_layout(title='Total factions by side and date')
# fig.write_html('../../reports/faction_side_by_date_test.html', auto_open=True)
fig.show()