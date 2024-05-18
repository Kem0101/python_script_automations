import mysql.connector
import random
from symptom_data import symptoms_data
from datetime import datetime


def populate_symptom(cursor):
    try:
        cursor.execute(
            "SELECT patient_id FROM Patient ORDER BY patient_id ASC")
        patients_id = cursor.fetchall()

        for patientid in patients_id:
            patient_id = patientid[0]

            # Select a random virus from the symptoms_data
            selected_virus = random.choice(symptoms_data['virus'])

            # Select 5 random symptoms from the selected virus
            selected_symptoms = random.sample(selected_virus['symptoms'], 5)

            # Join symptoms into a single description string
            description = ', '.join(selected_symptoms)
            date_reported = datetime.now().date()

            cursor.execute("""INSERT INTO Symptom
                              (patient_id, description, date_reported)
                              VALUES (%s, %s, %s)""",
                           (patient_id, description, date_reported))

        print("successfully populated symtoms!")

    except mysql.connector.Error as ex:
        print("Error during the insertion into Symptom:", ex)


connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Dioswithme',
    database='DoctorSource'
)

if connection.is_connected():
    cursor = connection.cursor()

    populate_symptom(cursor)

    connection.commit()
    cursor.close()
    connection.close()
else:
    print("Error: did not connect to the DB.")
