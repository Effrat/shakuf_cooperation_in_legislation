# TODO: user feedbacks (printouts) for for all modules: conformity, coherence.

from folders_structure.create_folders import create_required_folders
from retrieve.odata import retrieve_raw_data
from transform.faction import faction
from transform.knesset import knesset
from transform.knesset_by_date import knesset_by_date
from transform.person import person
from transform.bill_to_date_from_session import bill_to_date_from_session
from transform.bill_to_date_from_committee_session import bill_to_date_from_committee_session
from transform.all_bill_sponsors import all_bill_sponsors
from transform.members_of_knesset_by_date import members_of_knesset_by_date
from testing.members_of_knesset_by_date_test import members_of_knesset_by_date_test
from transform.people_in_government_by_date import people_in_government_by_date
from transform.members_of_faction_by_date import members_of_faction_by_date
from transform.dates import dates
from transform.bill_to_date import bill_to_date
from transform.members_of_knesset_faction_by_date import members_of_knesset_faction_by_date
from transform.faction_side_by_date import faction_side_by_date
from transform.all_bill_sponsors_to_date import all_bill_sponsors_to_date
from transform.members_of_knesset_faction_and_side_by_date import members_of_knesset_faction_and_side_by_date
from transform.bill_sponsors import bill_sponsors
from transform.bill_to_type import bill_to_type
from transform.bill_sponsors_w_type import bill_sponsors_w_type
from transform.front_end import front_end
from transform.latest_faction import latest_faction

def update_data():
    """
    Updates the raw source data and transforms it as necessary, to create tables for the front-end data model.
    """
    # # ----- step 0 -----
    # create_required_folders()
    # retrieve_raw_data()
    
    # # ----- step 1 -----
    # faction()
    # knesset()
    # knesset_by_date()
    # person()
    # bill_to_date_from_session()
    # bill_to_date_from_committee_session()
    # all_bill_sponsors()
    # members_of_knesset_by_date()
    # members_of_faction_by_date()
    # people_in_government_by_date()

    # # ----- step 2 -----
    # dates()
    # bill_to_date()
    # members_of_knesset_faction_by_date()
    # faction_side_by_date()

    # # ----- step 3 -----
    # # faction_side_by_date_test #TODO: create unit test
    # all_bill_sponsors_to_date()
    # members_of_knesset_faction_and_side_by_date()
    # latest_faction()

    # # ----- step 4 -----
    # # test_all_bill_sponsors_to_date #TODO: create unit test
    # # members_of_knesset_faction_and_side_by_date_test() #TODO: create unit test

    # # ----- step 5 -----
    # bill_sponsors()

    # # ----- step 6 -----
    # # # test_bill_sponsors() #TODO: create unit test

    # # ----- step 7 -----
    # bill_to_type()

    # # ----- step 8 -----
    # bill_sponsors_w_type()

    # # ----- step 10 -----
    # front_end()


 


if __name__ == '__main__':
    update_data()
   
    # print('Data update complete.')