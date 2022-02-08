#TODO: break into functions

from email.utils import parsedate_to_datetime
from matplotlib.pyplot import legend
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

members_of_faction_by_date = pd.read_csv(f'..\..\data\\expanded\members_of_faction_by_date.csv')
members_of_faction_by_date['Date'] = pd.to_datetime(members_of_faction_by_date['Date'])
daily_total_members_of_faction = members_of_faction_by_date.groupby(['Date', 'FactionID']).nunique()
# daily_total_members_of_faction
daily_total_members_of_faction.reset_index('FactionID', inplace =True)
daily_total_members_of_faction.rename(columns={'PersonID': 'Count'}, inplace =True)
daily_total_members_of_faction['FactionID'] = pd.to_numeric(daily_total_members_of_faction['FactionID'], downcast='integer')
# daily_total_members_of_faction