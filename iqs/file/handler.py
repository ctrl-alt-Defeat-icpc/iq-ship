from iqs.utils import os, zipfile, shutil, sys
from iqs.changers.changer01 import run as run01
from iqs.changers.changer20 import run as run20
from iqs.changers.changer30 import run as run30
from iqs.changers.changer40 import run as run40
from iqs.changers.changer50 import run as run50

def unzipSrc(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                extract_to = os.path.join(root, os.path.splitext(file)[0])
                os.makedirs(extract_to, exist_ok=True)
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_to)
                os.remove(zip_file_path)
                unzipSrc(extract_to) # recursive call

def clearFolders(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)  # Remove files or symbolic links
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove directories and their contents

def run(details):
    temp_src = os.path.join(details['srcdir'], '.tmp')

    # clear des folder and .tmp folder
    clearFolders(details['desdir'])
    if os.path.exists(temp_src):
        shutil.rmtree(temp_src)
    
    # Checking if the src folder contains anything other than the source folder/file (the .tmp folder isn't important)
    if len([item for item in os.listdir(details['srcdir']) if item != '.tmp']) != 1:
        sys.exit('Error: There should not be more than one file or folder in the source folder!')

    # extract all zip files in .tmp folder
    shutil.copytree(details['srcdir'], temp_src)
    unzipSrc(temp_src)

    if details['desver'] == 0 and details['srcver'] == 2:
        run20(temp_src, details['desdir'])
    elif details['desver'] == 0 and details['srcver'] == 3:
        run30(temp_src, details['desdir'])
    elif details['desver'] == 0 and details['srcver'] == 4:
        run40(temp_src, details['desdir'])
    elif details['desver'] == 0 and details['srcver'] == 5:
        run50(temp_src, details['desdir'])
    elif details['desver'] == 1 and details['srcver'] == 0:
        run01(temp_src, details['desdir'])