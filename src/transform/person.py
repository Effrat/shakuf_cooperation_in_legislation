# TODO: add urls for images and mk pages?
import pandas as pd


def person():
    '''
    Creates person table from KNS_Person and KNS_MkSiteCode.
    '''

    # ----- load -----
    KNS_Person = pd.read_excel('../data/raw/KNS_Person.xlsx', index_col=0)
    KNS_Person = KNS_Person[['PersonID', 'LastName', 'FirstName', 'GenderDesc']].drop_duplicates()

    KNS_MkSiteCode = pd.read_excel('../data/raw/KNS_MkSiteCode.xlsx', index_col=0)
    KNS_MkSiteCode = KNS_MkSiteCode[['KnsID', 'SiteId']]
    KNS_MkSiteCode.rename(columns={'KnsID': 'PersonID'}, inplace=True)


    # ----- transform -----
    person = pd.merge(KNS_Person, KNS_MkSiteCode,
        on='PersonID', how='left')
    person['SiteId'] = person['SiteId'].astype('Int64')
    person['FullName'] = person['FirstName'] + ' ' + person['LastName']
    person.columns = ['person_id', 'last_name', 'first_name', 'gender', 'site_id', 'full_name']


    # ----- testing/feedback -----
    missing_site_code = pd.merge(KNS_Person, KNS_MkSiteCode,
        on='PersonID', how='outer')
    missing_site_code = missing_site_code[missing_site_code['SiteId'].isnull()]
    missing_site_code = missing_site_code[['PersonID']]
    missing_site_code.drop_duplicates(inplace=True)
    missing_site_code.rename(columns={'PersonID': 'person_id'}, inplace=True)
    missing_site_code.to_csv('../data/reports/missing_site_code.csv', index=False)


    # ----- save -----
    person.to_excel(
        '../data/transformed/person.xlsx',
        sheet_name='person', index=False)

    # ----- export to json -----
    person.to_json(
        '../data/transformed/person.json',
        orient='records')