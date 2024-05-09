import mysql.connector
from random import sample


try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Dioswithme',
        db='ClinicLaboratory',
    )

    if connection.is_connected():
        print("Connection success")
        cursor = connection.cursor()

        cursor.execute("select test_id from LaboratoryTest")
        test_ids = cursor.fetchall()

        cursor.execute("select order_id from TestOrder")
        order_ids = cursor.fetchall()

        for order_id in order_ids:
            selected_test_ids = sample(test_ids, 5)

            for test_id in selected_test_ids:
                cursor.execute(
                    "INSERT INTO OrderDetail (test_id, order_id) VALUES(%s, %s)", (test_id[0], order_id[0]))

        connection.commit()
        print("Records inserted correctly")


except mysql.connector.Error as error:
    print("Error to connect to mysql")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
