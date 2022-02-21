# TODO: add urls for images and mk pages
import pandas as pd


def person():
    '''
    This function transforms the KNS_Person dataframe to a dimension for the FE data model.
    '''
    KNS_Person = pd.read_excel('..\data\\raw\\KNS_Person.xlsx', index_col=0)
    KNS_Person = KNS_Person[['PersonID', 'LastName', 'FirstName', 'GenderDesc']].drop_duplicates()
    KNS_Person
    KNS_MkSiteCode = pd.read_excel('..\data\\raw\\KNS_MkSiteCode.xlsx', index_col=0)
    KNS_MkSiteCode = KNS_MkSiteCode[['KnsID', 'SiteId']]
    KNS_MkSiteCode.rename(columns={'KnsID': 'PersonID'}, inplace=True)
    KNS_MkSiteCode

    person = KNS_MkSiteCode.set_index('PersonID').join(KNS_Person.set_index('PersonID'), how='outer').reset_index()
    person['SiteId'] = person['SiteId'].astype('Int64')
    person['FullName'] = person['FirstName'] + ' ' + person['LastName']
    person.columns = ['person_id', 'site_id', 'last_name', 'first_name', 'gender', 'full_name']
    person.to_excel(
        '..\data\\model\\dimensions\\person.xlsx',
        sheet_name='person',
        index=False
        )
    person