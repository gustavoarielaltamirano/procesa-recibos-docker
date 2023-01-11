import os
import fnmatch
import shutil
from smb.base import SharedFile
from smb.SMBConnection import SMBConnection

# listSharedFileObj = []

# Connect to the Windows share network directory
# server_name = "192.168.10.236"
# user_name = "galtamirano@central"
# password = "Juanita7$"
# host = "induccion-colaboradores"
# remote_host = "file00.grupo-gestion.com.ar"
# domain = "central"
# use_ntlm_v2 = True

# client = SMBConnection(user_name, password, my_name=host, remote_name=remote_host, use_ntlm_v2=use_ntlm_v2)
# client.connect(ip=server_name, port=139, sock_family=None, timeout=60)

# Define share network dir for ZIP process
# NET_WIN_DIR = "GrupoDoc\\Documentos Compartidos\\BOTSRECIBOSGG"
# Define share network dir for processed files
# NET_WIN_DIR_FINAL = 'GrupoDoc\\Documentos Compartidos\\BOTSRECIBOSGG\\listos'

# with SMBConnection(user_name, password, my_name=host, remote_name=remote_host, domain=domain) as smbconn:
    # "You must call this method before attempting any of the file operations with the remote server."
    # https://pysmb.readthedocs.io/en/latest/api/smb_SMBConnection.html#smb.SMBConnection.SMBConnection.connect
    # smbconn.connect(remote_host)

    # Returns: A list of "smb.base.SharedFile" instances
    # https://pysmb.readthedocs.io/en/latest/api/smb_SMBConnection.html#smb.SMBConnection.SMBConnection.listPath
    # listSharedFileObj = smbconn.listPath("GrupoDoc", "/Documentos Compartidos/BOTSRECIBOSGG")

# src = '\\\\192.168.10.236\grupodoc\Documentos Compartidos\BOTSRECIBOSGG\\recibos.zip'
# dst = './resultados/recibos.zip'

src = r"\\192.168.10.236\grupodoc\Documentos Compartidos\BOTSRECIBOSGG"
dst = r"./resultados"
file_name = "\\recibos.zip"

def get_files():

    shutil.copyfile(src + file_name, dst + file_name)

    # Pre annotate for type-hinting SharedFile object
    # item: SharedFile
    #
    # for item in listSharedFileObj:
    #     print(item.filename)

    # current_path = os.getcwd()

    # List the contents of the directory
    # zip_to_process = client.listPath(NET_WIN_DIR, "/")
    #
    # for file in zip_to_process:
    #     if fnmatch.fnmatch(file, '*.zip'):
    #         # file_path = os.path.join(root, file)
    #         shutil.move(NET_WIN_DIR+'\\'+file, current_path+'/resultados/')
    #         print('Archivo zip identificado: ', file)
    #
    # if zip_to_process == '':
    #     print('No hay archivos zip para procesar, se vuelve a consultar en 1 min...')
