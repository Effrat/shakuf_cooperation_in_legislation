import pandas as pd

# def bill_to_date_test():
#     """
#     """
bill_to_date = pd.read_excel(
    '../../data/transformed/bill_to_date.xlsx',
    parse_dates=['date'])
print('bill_to_date.nunique:')
print(bill_to_date.nunique())

bill_ids_set_from_bill_to_date = set(bill_to_date['bill_id'])
# print(bill_ids_set_from_bill_to_date)

all_bills_initiators = pd.read_excel(
    '../../data/transformed/all_bills_initiators.xlsx')
all_bills_initiators
print('all_bills_initiators.nunique:')
print(all_bills_initiators.nunique())

bill_ids_set_from_all_bills_initiators = set(all_bills_initiators['bill_id'])
# print(bill_ids_set_from_all_bills_initiators)

print('Bills which have initiator data, but no date data (never scheduled for discussion):')
no_date_bills = list(bill_ids_set_from_all_bills_initiators - bill_ids_set_from_bill_to_date)
print(f'Total bills: {len(no_date_bills)}')
print(no_date_bills)



# latest printout:

# bill_to_date.nunique:
# bill_id    50322
# date        4136
# dtype: int64
# all_bills_initiators.nunique:
# bill_id         43920
# person_id         844
# is_initiator        2
# dtype: int64
# Bills which have initiator data, but no date data (never scheduled for discussion):
# 86
# [150536, 97304, 2072604, 172578, 150008, 141868, 149552, 145462, 149558, 89658, 432189, 149566, 130112, 151109, 130126, 320593, 2078292, 151035, 371292, 320625, 151158, 151160, 151161, 320635, 2078337, 151178, 2015378, 2073238, 152218, 2073244, 150689, 151208, 344749, 343229, 24778, 81613, 151250, 2077401, 150754, 149762, 176911, 84752, 84754, 27923, 149275, 143145, 150315, 174383, 174384, 174385, 174386, 174387, 174388, 372549, 149348, 174439, 150389, 113532, 320902, 429960, 292234, 133004, 150421, 150935, 150941, 150953, 320431, 17840, 320945, 320433, 320434, 320436, 475066, 150975, 549332, 149475, 151017, 84457, 151019, 84460, 84461, 84462, 84463, 2066424, 94203, 81406]