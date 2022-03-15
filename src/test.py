# TODO: user feedbacks (printouts) for for all modules: conformity, coherence.

from folders_structure.create_folders import create_required_folders
from retrieve.odata import retrieve_raw_data
from transform.faction import faction
from transform.knesset import knesset
from transform.knesset_by_date import knesset_by_date
from transform.person import person
from transform.bill_to_date_from_session import bill_to_date_from_session
from transform.bill_to_date_from_commettee_session import bill_to_date_from_commettee_session
from transform.all_bill_initiators import all_bill_initiators
from transform.members_of_knesset_by_date import members_of_knesset_by_date
from testing.members_of_knesset_by_date_test import members_of_knesset_by_date_test
from transform.people_in_government_by_date import people_in_government_by_date
from transform.members_of_faction_by_date import members_of_faction_by_date
from transform.dates import dates
from transform.bill_to_date import bill_to_date
from transform.members_of_knesset_faction_by_date import members_of_knesset_faction_by_date
from transform.faction_side_by_date import faction_side_by_date
from transform.all_bill_initiators_to_date import all_bill_initiators_to_date
from transform.members_of_knesset_faction_and_side_by_date import members_of_knesset_faction_and_side_by_date
from transform.bill_initiators import bill_initiators
from transform.bill_to_side import bill_to_side
from transform.bill import bill


def test():
    # bill()
    print("testing...")


 


test()