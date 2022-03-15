import pandas as pd
from math import floor
import requests
from IPython.display import clear_output

BATCH_SIZE = 100

def retrieve_table(suffix):
    data = odata_get_data_from_suffix(suffix)
    df = pd.DataFrame(data)
    df.to_excel(f'..\data\\raw\{suffix}.xlsx', header=True)
    # clear_output(wait=True)
    print(f'Retrieval of {suffix} table is done.')

def odata_get_data_from_suffix(suffix, partial=1):
    base_url = concat_base_url(suffix)
    return odata_get_records(base_url, partial)

def odata_get_record_count(base_url):
    url = f'{base_url}/$count'
    r = requests.get(url)
    record_count = int(r.text)
    return(record_count)

def odata_get_hundred_records(base_url, skip):
    url = f'{base_url}/?$skip={skip}&$format=json'
    r = requests.get(url)
    j = r.json()
    return j['value']

def odata_get_records(base_url, pratial=1, skips=[], data=[], iter=1, metadata=[]):
    errors = []
    if len(skips) == 0:
        record_count = odata_get_record_count(base_url)
        record_count = floor(record_count * pratial)
        skips = range(0, int(record_count), BATCH_SIZE)
    else:
        record_count = len(skips) * BATCH_SIZE
    batch = 0
    for skip in skips:
        try:
            batch_records = odata_get_hundred_records(base_url, skip)
            data = data + batch_records
        except:
            errors.append(skip)
            batch_records = []
        batch = batch + 1
        # user feedback
        # TODO: fix percentage calculation
        pct_errors = '{:.2%}'.format(len(errors) / record_count)
        pct_done = '{:.2%}'.format((batch * BATCH_SIZE) / record_count)
        clear_output(wait=True)
        md = {
            'iter': iter,
            'records': record_count,
            'pct_done': pct_done,
            'pct_errors': pct_errors,
            'errors': len(errors),
            'batch': batch,
            'records in batch': len(batch_records),
        }
        print(base_url.split('/')[-1])
        print(pd.DataFrame(metadata + [md]))

    if len(errors) == 0:
        return(data)
    else:
        return odata_get_records(base_url=base_url, skips=errors.copy(), data=data, iter=iter+1, metadata=metadata+[md])

def concat_base_url(suffix):
    root_url = 'https://knesset.gov.il/Odata/ParliamentInfo.svc'
    return f'{root_url}/{suffix}'

