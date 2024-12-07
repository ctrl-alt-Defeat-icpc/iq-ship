from iqs.utils import zipfile, os, shutil

def io2zip(path):
    # zipping folder
    zipname = 'problem.zip'
    with zipfile.ZipFile(os.path.join(path, zipname), 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(path):
            for file in files:
                if file == zipname:
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, path)
                zipf.write(file_path, arcname)
    
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            if not item == zipname:
                os.remove(os.path.join(path, item))
        else: # directories
            shutil.rmtree(os.path.join(path, item))