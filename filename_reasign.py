import os
import fnmatch
import zipfile
from datetime import datetime

def filename_reasign(dataAws):

    # Get today
    today = datetime.now()
    today.strftime('%Y-%m-%d_%H')

    # Create a zipfile first
    z = zipfile.ZipFile('./procesos/finalizados/'+dataAws['cuit'].iloc[0]+'_'+str(today)+'.zip', 'w')

    for root, dirs, files in os.walk('./procesos/temp/'):
        for file in files:
            if fnmatch.fnmatch(file, '*.pdf'):
                source_file_path = os.path.join(root, file)

                # Split filename to get receiptNumber and convert to int
                file_split = file.split('.')
                name_split = file_split[0].split('_')
                receiptNumber = int(name_split[4])

                # Locate cuil, year, month, clearingType in dataframe
                rec = dataAws.loc[dataAws['receiptNumber'] == str(receiptNumber)]

                if len(rec) > 0:
                    # Replace the file name whit de structure required in the platform (CUIL_YEAR_MONTH_CLEARINGTYPE)
                    new_file_name = f'{rec["cuil"].iloc[0]}_{rec["year"].iloc[0]}_{rec["month"].iloc[0]}_{rec["clearingType"].iloc[0]}.pdf'
                    target_file_path = os.path.join(root, new_file_name)
                    # print(rec, receiptNumber)
                    # print(f'The file name will be: {rec["cuil"].iloc[0]}_{rec["year"].iloc[0]}_{rec["month"].iloc[0]}_{rec["clearingType"].iloc[0]}.pdf')
                    os.rename(source_file_path, target_file_path)
                    z.write(target_file_path, arcname=new_file_name)



    print('Zip generado')
    z.close()