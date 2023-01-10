import zipfile

def unzip(file, dir_target):
    with zipfile.ZipFile(file, 'r') as zipRef:
        zipRef.extractall(dir_target)