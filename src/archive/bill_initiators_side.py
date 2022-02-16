from email import header
import numpy as np
import pandas as pd
import plotly.express as px

bill_to_date_to_mk = pd.read_excel('..\..\data\\precursors\\bill_to_date_to_mk.xlsx', index_col=0)
bill_to_date_to_mk

# mks_in_bill_initiators = bill_to_date_to_mk[['BillID', 'PersonID']][bill_to_date_to_mk['IsInitiator'] == 1]
# total_mks_in_bill_initiators = mks_in_bill_initiators.groupby('BillID').nunique()
# total_mks_in_bill_initiators

mks_in_coalition_in_bill_initiators = bill_to_date_to_mk[['BillID', 'PersonID']][(bill_to_date_to_mk['IsInitiator'] == 1) & (bill_to_date_to_mk['In Coalition'] == True)]
total_mks_in_coalition_in_bill_initiators = mks_in_coalition_in_bill_initiators.groupby('BillID').nunique()
total_mks_in_coalition_in_bill_initiators.rename(columns={'PersonID': 'InitiatorsInCoalition'}, inplace=True)

mks_in_coalition_in_bill_joiners = bill_to_date_to_mk[['BillID', 'PersonID']][(bill_to_date_to_mk['IsInitiator'] == 0) & (bill_to_date_to_mk['In Coalition'] == True)]
total_mks_in_coalition_in_bill_joiners = mks_in_coalition_in_bill_joiners.groupby('BillID').nunique()
total_mks_in_coalition_in_bill_joiners.rename(columns={'PersonID': 'JoinersInCoalition'}, inplace=True)

mks_in_opposition_in_bill_initiators = bill_to_date_to_mk[['BillID', 'PersonID']][(bill_to_date_to_mk['IsInitiator'] == 1) & (bill_to_date_to_mk['In Coalition'] == False)]
total_mks_in_opposition_in_bill_initiators = mks_in_opposition_in_bill_initiators.groupby('BillID').nunique()
total_mks_in_opposition_in_bill_initiators.rename(columns={'PersonID': 'InitiatorsInOpposition'}, inplace=True)

mks_in_opposition_in_bill_joiners = bill_to_date_to_mk[['BillID', 'PersonID']][(bill_to_date_to_mk['IsInitiator'] == 0) & (bill_to_date_to_mk['In Coalition'] == False)]
total_mks_in_opposition_in_bill_joiners = mks_in_opposition_in_bill_joiners.groupby('BillID').nunique()
total_mks_in_opposition_in_bill_joiners.rename(columns={'PersonID': 'JoinersInOpposition'}, inplace=True)

bill_initiators_side = pd.concat(
    [
        total_mks_in_coalition_in_bill_initiators,
        total_mks_in_opposition_in_bill_initiators,
        total_mks_in_coalition_in_bill_joiners,
        total_mks_in_opposition_in_bill_joiners
    ], axis=1)
bill_initiators_side.fillna(0, inplace=True)
bill_initiators_side['TotalInitiators'] = bill_initiators_side['InitiatorsInCoalition'] + bill_initiators_side['InitiatorsInOpposition']
bill_initiators_side['InitiatorsSide'] = 'Bipartisan'
bill_initiators_side['InitiatorsSide'][(bill_initiators_side['InitiatorsInCoalition'] / bill_initiators_side['TotalInitiators']) > 0.5] = 'Coalition'
bill_initiators_side['InitiatorsSide'][(bill_initiators_side['InitiatorsInOpposition'] / bill_initiators_side['TotalInitiators']) > 0.5] = 'Opposition'

bill_initiators_side['TotalJoiners'] = bill_initiators_side['JoinersInCoalition'] + bill_initiators_side['JoinersInOpposition']
bill_initiators_side['JoinersSide'] = 'Bipartisan'
bill_initiators_side['JoinersSide'][(bill_initiators_side['JoinersInCoalition'] / bill_initiators_side['TotalJoiners']) > 0.5] = 'Coalition'
bill_initiators_side['JoinersSide'][(bill_initiators_side['JoinersInOpposition'] / bill_initiators_side['TotalJoiners']) > 0.5] = 'Opposition'

# bill_initiators_side.drop(labels=['InitiatorsInCoalition', 'InitiatorsInOpposition', 'TotalInitiators', 'JoinersInCoalition', 'JoinersInOpposition', 'TotalJoiners'], axis=1, inplace=True)
bill_initiators_side.reset_index(inplace=True)
print(bill_initiators_side[['BillID', 'InitiatorsSide']].groupby('InitiatorsSide').nunique())
print(bill_initiators_side[['BillID', 'JoinersSide']].groupby('JoinersSide').nunique())
bill_initiators_side.to_excel('..\..\data\\precursors\\bill_initiators_side.xlsx', header=True)
bill_initiators_side