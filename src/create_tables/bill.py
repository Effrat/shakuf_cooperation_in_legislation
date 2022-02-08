#TODO: break into functions

import numpy as np
import pandas as pd
import plotly.express as px



# ===================   import data   ===================
KNS_Bill = pd.read_csv(
    '..\..\data\\raw\\KNS_Bill.csv',
    # parse_dates=['LastUpdatedDate', 'PublicationDate'],
    dtype={'Name': str},
    low_memory=False
    )

KNS_Bill = KNS_Bill[['BillID', 'Name']]#, 'Name']]

# KNS_Bill['Name'] = KNS_Bill['Name'].str.replace('"', '|||')
KNS_Bill.to_csv('..\..\data\\to_powerbi\\bill.csv', index=False)


KNS_Bill 