#TODO: break into functions

# import numpy as np
from operator import index
import pandas as pd
# from datetime import date
# import plotly.express as px



# ===================   import data   ===================
KNS_Person = pd.read_csv('..\..\data\\raw\\KNS_Person.csv', index_col='PersonID')
KNS_MkSiteCode = pd.read_csv('..\..\data\\raw\\KNS_MkSiteCode.csv', index_col='KnsID')

person = KNS_MkSiteCode[['MKSiteCode']].join(KNS_Person).reset_index()
person.to_csv('..\..\data\\to_powerbi\\person.csv', index=False)