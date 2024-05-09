from mysql.connector import Error
import mysql.connector
from random_data import data

data_tuples = [(item['patient_id'], item['medical_id'],
                item['date_time'], item['state']) for item in data]


try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Dioswithme',
        db='ClinicLaboratory',
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO TestOrder(patient_id, medical_id, date_time, state)
                            VALUES(%s, %s, %s, %s)""", data_tuples)
        # print(cursor.rowcount)
        # print(len(data))
        if (len(data) == cursor.rowcount):
            connection.commit()
            print("{} rows inserted".format(len(data)))
        else:
            connection.rollback()
except Error as ex:
    print("Error during connection: {}".format(ex))
finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
