import mysql.connector
from datetime import datetime
import random
from testresult_data import results_data


def generate_result_value(test_id, results_data):
    test_id = test_id[0]
    # Find into the dictionary that match with test_id
    tests_data = next(
        (test for test in results_data if test['id'] == test_id), None)

    if tests_data is None:
        return None
    # Obtaining a random result from results
    selected_result = random.choice(tests_data['results'])

    result_value = selected_result[0]
    unit_measure = selected_result[1]
    observation = selected_result[2]

    return result_value, unit_measure, observation


def populate_test_result(cursor):
    try:
        cursor.execute(
            "SELECT t.patient_id, t.medical_id, t.order_id FROM TestOrder t")
        test_orders = cursor.fetchall()

        for order in test_orders:
            patient_id = order[0]
            medical_id = order[1]
            order_id = order[2]

            # Obtain tests asociate to the orden
            cursor.execute(
                "SELECT test_id FROM OrderDetail WHERE order_id = %s", (order_id,))
            test_ids = cursor.fetchall()

            for test_id in test_ids:
                # asign data for TestResult
                date_time = datetime.now()
                result_value, unit_measure, observation = generate_result_value(
                    test_id, results_data)
                state = "Normal"

                print("Generated data:")
                print("Patient ID:", patient_id)
                print("Test ID:", test_id[0])
                print("Medical ID:", medical_id)
                print("Date Time:", date_time)
                print("Result Value:", result_value)
                print("Unit Measure:", unit_measure)
                print("Observation:", observation)
                print("State:", state)

                # Insertar datos en TestResult
                # cursor.execute("""INSERT INTO TestResult
                #   (patient_id, test_id, medical_id, date_time, result_value, unit_measure, observation, state)
                #       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                #                (patient_id, test_id[0], medical_id, date_time, result_value, unit_measure, observation, state))

                # print("TestResult se pobló correctamente.")

    except mysql.connector.Error as ex:
        print("Error during the insertion into TestResult:", ex)


connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Dioswithme',
    database='ClinicLaboratory'
)

if connection.is_connected():
    cursor = connection.cursor()

    populate_test_result(cursor)

    connection.commit()
    cursor.close()
    connection.close()
else:
    print("Error: did not connect to the DB.")
