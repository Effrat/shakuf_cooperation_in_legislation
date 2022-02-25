# TODO: manage user feedbacks (printouts + docstrings) for for all modules: conformity, coherence.

from folders_structure.create_folders import create_required_folders
from retrieve.odata import retrieve_raw_data
from transform.knesset import knesset
from transform.knesset_by_date import knesset_by_date
from transform.person import person
from transform.faction import faction
from transform.bill_to_date_from_session import bill_to_date_from_session
from transform.bill_to_date_from_commettee_session import bill_to_date_from_commettee_session
from transform.bill_to_date import bill_to_date
from transform.members_of_faction_by_date import members_of_faction_by_date
from transform.people_in_government_by_date import people_in_government_by_date
from transform.members_of_knesset_by_date import members_of_knesset_by_date
from transform.dates import dates
from transform.members_of_knesset_faction_and_side_by_date import members_of_knesset_faction_and_side_by_date
from transform.bill_initiators import bill_initiators
from transform.bill_to_side import bill_to_side
from transform.bill import bill

def update_data():
    # ===== prerequisites ===== 
    # create_required_folders()
    # retrieve_raw_data()
    
    # ===== data transformations =====

    # ----- step 1 -----
    # knesset()
    # knesset_by_date()
    # person()
    # faction() # contains manual data corrections
    # bill_to_date_from_session()
    # bill_to_date_from_commettee_session()
    # bill_to_date()
    # members_of_faction_by_date()
    # people_in_government_by_date()
    # members_of_knesset_by_date()

    # ----- step 2 -----
    # dates()
    # members_of_knesset_faction_and_side_by_date()
    # bill_initiators()
    # bill_to_side()
    # bill()


 


if __name__ == '__main__':
    update_data()
   
    # print('Data update complete.')