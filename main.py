import shutil
import os
import time
from find_zips import find_zip_files
from unzip_file import unzip
from delete_file import del_folder_contain
from capture_pdf_data import capture_pdf_data
from conn_aws import search_record
from filename_reasign import filename_reasign
from get_files_to_process import get_files
file_to_process = ''

def start_process(dir):

    while True:

        current_path = os.getcwd()

        # Find zip files into "resultado" directory
        file_to_process = find_zip_files(dir)

        # if Valid zip file, move file to proceso directory
        if file_to_process != '':
            # Remove all contain on procesos folder and temp folder
            del_folder_contain(current_path+'/procesos', current_path+'/procesos/temp', current_path+'/procesos/finalizados')
            # unzip the file
            unzip(file_to_process, current_path+'/procesos/temp')
            # move to proceso directory
            shutil.move(file_to_process, current_path+'/procesos/')

            # return cuit and recnros list for query
            cuit, recnros = capture_pdf_data()

            if cuit != '' and len(recnros) > 0:
                # Find records by cuit and recnros list
                # Get all data from aws
                print(f'lo que va a procesar el search record cuit {cuit} y {recnros}')
                dataAws = search_record(cuit, recnros)
                if len(dataAws) > 0 and len(recnros) > 0 and cuit != '':
                    # Iterate in temp directory and change all filename according to the platform CUIL_YEAR_MONTH_CLEARINGTYPE.pdf
                    filename_reasign(dataAws)
                else:
                    # TODO: Move file_to_process to errors folder
                    print(f'El archivo {file_to_process} no pudo ser identificado con los registros en la plataforma :: Revisar!')
            else:
                # TODO: Move file_to_process to errors folder
                print(f'El archivo {file_to_process} no pudo ser identificado con los registros en la plataforma :: Revisar!')

        time.sleep(60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_process('./resultados')