#TODO: break into functions

import pandas as pd
import plotly.express as px

mks_w_position_in_coalition_by_date = pd.read_csv(f'..\..\data\\expanded\mks_w_position_in_coalition_by_date.csv')
mks_w_position_in_coalition_by_date = mks_w_position_in_coalition_by_date[['Date', 'FactID']]
mks_w_position_in_coalition_by_date.drop_duplicates(inplace=True)
mks_w_position_in_coalition_by_date['Date'] = pd.to_datetime(mks_w_position_in_coalition_by_date['Date'])
daily_total_members_of_knesset_w_position_in_gov = mks_w_position_in_coalition_by_date.groupby('Date').nunique()
# daily_total_members_of_knesset_w_position_in_gov

fig = px.area(daily_total_members_of_knesset_w_position_in_gov)
fig.show()