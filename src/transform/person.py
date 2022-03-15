# TODO: add urls for images and mk pages
import pandas as pd


def person():
    '''
    Creates person table from KNS_Person and KNS_MkSiteCode.
    '''
    KNS_Person = pd.read_excel('../data/raw/KNS_Person.xlsx', index_col=0)
    KNS_Person = KNS_Person[['PersonID', 'LastName', 'FirstName', 'GenderDesc']].drop_duplicates()
    KNS_Person
    KNS_MkSiteCode = pd.read_excel('../data/raw/KNS_MkSiteCode.xlsx', index_col=0)
    KNS_MkSiteCode = KNS_MkSiteCode[['KnsID', 'SiteId']]
    KNS_MkSiteCode.rename(columns={'KnsID': 'PersonID'}, inplace=True)
    KNS_MkSiteCode

    person = pd.merge(
        KNS_Person, KNS_MkSiteCode,
        on='PersonID', how='left')
    person['SiteId'] = person['SiteId'].astype('Int64')
    person['FullName'] = person['FirstName'] + ' ' + person['LastName']
    person.columns = ['person_id', 'last_name', 'first_name', 'gender', 'site_id', 'full_name']
    person.to_excel(
        '../data/model/dimensions/person.xlsx',
        sheet_name='person',
        index=False
        )
    person