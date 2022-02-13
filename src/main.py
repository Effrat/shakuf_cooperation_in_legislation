from retrieve.odata import retrieve_raw_data
from transform.knesset import knesset_transform
from transform.person import person_transform
from transform.date import date_create
from transform.faction import faction_transform
from expand_dates.factions import factions_expand

def update_data():
    # date_create()
    # retrieve_raw_data()
    # knesset_transform()
    # person_transform()
    # faction_transform()
    factions_expand()



if __name__ == '__main__':
    update_data()
    print('Data update complete.')