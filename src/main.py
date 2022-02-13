from retrieve_odata import retrieve_raw_data
from transform.knesset import knesset_transform
from transform.person import person_transform



def update_data():
    # retrieve_raw_data()
    # knesset_transform()
    person_transform()



if __name__ == '__main__':
    update_data()
    print('Data update complete.')