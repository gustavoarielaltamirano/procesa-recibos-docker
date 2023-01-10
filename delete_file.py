import os
import shutil

def del_folder_contain(dir_procesos, dir_temp, dir_finalizados):

    # print(dir_procesos, dir_temp)

    # Remove temp dir
    if os.path.exists(dir_temp):
        shutil.rmtree(dir_temp)
    # Remove finalizados dir
    if os.path.exists(dir_finalizados):
        shutil.rmtree(dir_finalizados)

    # recreate temp dir
    os.makedirs(dir_temp)
    # recreate finalizados dir
    os.makedirs(dir_finalizados)

    for file in os.listdir(dir_procesos):
        file_path = os.path.join(dir_procesos, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)