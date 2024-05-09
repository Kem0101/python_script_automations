from datetime import datetime
# Este bloque de codigo genera los datos para poblar la tabla TestOrder

data = []

initial_patient_id = 101
initial_medical_id = 21

for patient_id in range(initial_patient_id, 5001):
    current_medical_id = initial_medical_id + \
        ((patient_id - initial_patient_id) // 5)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append({
        'patient_id': patient_id,
        'medical_id': current_medical_id,
        'date_time': current_datetime,
        'state': 'Pending'
    })
