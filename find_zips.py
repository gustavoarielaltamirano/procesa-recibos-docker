import os
import fnmatch

# Find zip files into "resultado" directory
def find_zip_files(dir_resultado):

    file_path = ''

    for root, dirs, files in os.walk(dir_resultado):
        for file in files:
            if fnmatch.fnmatch(file, '*.zip'):
                file_path = os.path.join(root, file)
                print('Archivo zip identificado: ', file_path)

    if file_path == '':
        print('No hay archivos zip para procesar, se vuelve a consultar en 1 min...')

    return file_path