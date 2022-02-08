import numpy as np
import pandas as pd
import plotly.express as px

inner_initiators_to_bills = pd.read_excel('..\..\data\\precursors\inner_initiators_to_bills.xlsx')
inner_initiators_to_bills

# join w/ mk_in_coalition on person & date, to get:
# bill, person, date, faction, side, is_in_coalition and 
members_of_knesset_in_coalition_in_faction = pd.read_csv('..\..\data\\to_powerbi\members_of_knesset_in_coalition_in_faction.csv', parse_dates=['Date'])
members_of_knesset_in_coalition_in_faction

bill_to_date_to_mk = inner_initiators_to_bills.set_index(['PersonID', 'Date']).join(members_of_knesset_in_coalition_in_faction.set_index(['PersonID', 'Date']))
bill_to_date_to_mk

# ------- log errors
missing_coalition_data = bill_to_date_to_mk[bill_to_date_to_mk['In Coalition'].isna()]
missing_coalition_data.to_excel('..\..\data\\logs\missing_coalition_data.xlsx', header=True)
missing_coalition_data.groupby('KnessetNum').nunique()

# ------- export
bill_to_date_to_mk = bill_to_date_to_mk.reset_index().dropna()
bill_to_date_to_mk.to_excel('..\..\data\\precursors\\bill_to_date_to_mk.xlsx', header=True)
bill_to_date_to_mk