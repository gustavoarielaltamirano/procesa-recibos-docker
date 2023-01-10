import os
import fnmatch
import shutil
from smb.SMBConnection import SMBConnection

# Connect to the Windows share network directory
server_name = "192.168.10.236"
user_name = "galtamirano@central"
password = "Juanita7$"
host = "induccion-colaboradores"
remote_host = "file00.grupo-gestion.com.ar"
domain = "central"
use_ntlm_v2 = True

client = SMBConnection(user_name, password, domain, use_ntlm_v2=use_ntlm_v2)
client.connect(ip=server_name, port=445, sock_family=None, timeout=60)

# Define share network dir for ZIP process
NET_WIN_DIR = "GrupoDoc\\Documentos Compartidos\\BOTSRECIBOSGG"
# Define share network dir for processed files
NET_WIN_DIR_FINAL = 'GrupoDoc\\Documentos Compartidos\\BOTSRECIBOSGG\\listos'


def get_files():

    current_path = os.getcwd()

    # List the contents of the directory
    zip_to_process = client.listPath(NET_WIN_DIR, "/")

    for file in zip_to_process:
        if fnmatch.fnmatch(file, '*.zip'):
            # file_path = os.path.join(root, file)
            shutil.move(NET_WIN_DIR+'\\'+file, current_path+'/resultados/')
            print('Archivo zip identificado: ', file)

    if zip_to_process == '':
        print('No hay archivos zip para procesar, se vuelve a consultar en 1 min...')
