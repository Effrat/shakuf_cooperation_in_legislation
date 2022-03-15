import os
from utils.folders_structure import create_folders

# Create folders in the parent directory.
folders = [
    '\\data\\raw',
    '\\data\\transformed',
    '\\data\\model\\dimensions',
    '\\data\\model\\facts',
    '\\data\\reports'
]

# parent directory
path = os.path.dirname(os.getcwd())

def create_required_folders():
    """
    Create required folders in the parent directory.
    """
    create_folders(path=path, folders=folders)