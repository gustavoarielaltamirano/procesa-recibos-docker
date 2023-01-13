import pymysql
import pandas as pd
import time

# Config variables
endpoint = 'recibos.cnz0edophtit.us-east-2.rds.amazonaws.com'
username = 'botgg'
password = 'G3$t10n#22'
dataname = 'recibos'

# Set connection
conn = pymysql.connect(host=endpoint, user=username, passwd=password, database=dataname)

# Set dataframe display columns without limits
pd.options.display.max_columns = None
pd.options.display.max_colwidth = 20

def search_record(cuit, recnros):

    # Empty dataframe to capture all records from AWS
    df = pd.DataFrame()

    try:

        cursor = conn.cursor()

        recs = ','.join(['%s'] * len(recnros))

        # Convert string element list to number
        recnros = [int(x) for x in recnros]

        # print(recnros)

        query = f'select c.cuit, r.clearingType, r.idCompany, r.month, r.year, r.receiptNumber, r.firstName, r.lastName, r.cuil, r.costCenter from receipt_user r join company c on c.idCompany = r.idCompany where c.cuit = {cuit} and r.receiptNumber in ({recs})'

        cursor.execute(query, recnros)

    except pymysql.err.OperationalError as e:
        print('Error recibido: ', e.args[0], e.args[1])
        if e.args[0] == 2006 or e.args[0] == 2013:
            print("connection reset by peer, reintentando conectar en 60seg")
            time.sleep(60)
            cursor.execute(query, recnros)
        else:
            raise e
    finally:
        # close the connection
        conn.close()

    rows = cursor.fetchall()

    # Convert tuple to pandas dataframe
    if len(rows) > 0:
        df = pd.DataFrame(rows, columns=['cuit', 'clearingType', 'idCompany', 'month', 'year', 'receiptNumber', 'firstName', 'lastName', 'cuil', 'costCenter'])

    cursor.close()

    # print(df.head())

    # TEST: We wait only 1 record, but if not, iterate on first 5
    # for row in rows:
    #     print(row)

    return df
