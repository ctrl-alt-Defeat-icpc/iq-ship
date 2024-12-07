from iqs.utils import zipfile, os, shutil

def io2zip(des, input_path, output_path):
    # zipping folder
    with zipfile.ZipFile(os.path.join(des, 'problem.zip'), 'w', zipfile.ZIP_DEFLATED) as zipf:
        for dir in [input_path, output_path]:
            for root, _, files in os.walk(dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, des)
                    zipf.write(file_path, arcname)
                    os.remove(file_path)
    
    # deleting extra folders
    shutil.rmtree(input_path)
    shutil.rmtree(output_path)