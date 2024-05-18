import mysql.connector


def populate_medical_history(cursor):
    try:
        cursor.execute(
            "SELECT patient_id FROM Patient ORDER BY patient_id ASC")
        patients_id = cursor.fetchall()

        for patientid in patients_id:
            patient_id = patientid[0]

            cursor.execute("""INSERT INTO MedicalHistory
            (patient_id, personal_medical_history, previous_treatments, allergies)
            VALUES (%s, %s, %s, %s)""",
                           (patient_id, None, None, None))

        print("successfully populated medical history!")

    except mysql.connector.Error as ex:
        print("Error during the insertion into Medical History:", ex)


connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Dioswithme',
    database='DoctorSource'
)

if connection.is_connected():
    cursor = connection.cursor()

    populate_medical_history(cursor)

    connection.commit()
    cursor.close()
    connection.close()
else:
    print("Error: did not connect to the DB.")
