import os
import fnmatch

# Capture pdf Data
def capture_pdf_data():

    fileNumber = 0
    recnros = []

    for file in os.listdir('./procesos/temp/'):
        # list con los recnro de cada pdf y el numero de cuit de la empresa admin y retornarlos
        if file != '__MACOSX':
            filename, extention = os.path.splitext(file)
            # datahash = filename.split('#')
            data = filename.split('_')
            if len(data) == 5:
                recnros.append(data[4])

    return data[0].replace('-', ''), recnros