import pandas as pd

sharen_haskel_replace_0_w_882 = pd.read_csv(
    '../../data/missing_data/sharen_haskel_replace_0_w_882.csv',
    parse_dates=['date'])
original_data = sharen_haskel_replace_0_w_882.copy()
sharen_haskel_replace_0_w_882['faction_id'] = 882
sharen_haskel_replace_0_w_882
original_data['faction_id'][original_data['date'].isin(
    sharen_haskel_replace_0_w_882['date'])] = sharen_haskel_replace_0_w_882['faction_id']

original_data