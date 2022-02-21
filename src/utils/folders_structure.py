import os


def create_folders(path, folders):
    """
    Create folders in given directory, according to a list of folders.
    """
    for folder in folders:
        if not os.path.exists(path + folder):
            os.makedirs(path + folder)
            print('Path created:\n' + path + folder)
