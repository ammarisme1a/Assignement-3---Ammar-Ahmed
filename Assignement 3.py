import csv

class Physician:
    __slots__ = ["__id", "__name", "__specialty"]
    def __init__(self, id, name, specialty):
        self.__id = id
        self.__name = name
        self.__specialty = specialty
    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_specialty(self, specialty):
        self.__specialty = specialty

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_specialty(self):
        return self.__specialty
    
    def __repr__(self):
        return (self.id, self.name, self.specialty)
    def __str__(self):
        return (self.id, self.name, self.specialty)

class Patient:
    __slots__ = ["__emr_id", "__name", "__gender", "__phone_number"]
    def __init__(self, emr_id, name, gender, phone_number):
        self.__emr_id = emr_id
        self.__name = name
        self.__gender = gender
        self.__phone_number = phone_number
    def set_emr_id(self, emr_id):
        self.__emr_id = emr_id
    def set_name(self, name):
        self.__name = name
    def set_gender(self, gender):
        self.__gender = gender
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_emr_id(self):
        return self.__emr_id
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def get_phone_number(self):
        return self.__phone_number

    def __repr__(self):
        return (self.emr_id, self.name, self.gender, self.phone_number)
    def __str__(self):
        return (self.emr_id, self.name, self.gender, self.phone_number)

class Encounter:
    def __init__(self, physician, patient, date, disease, medication):
        self.physician = physician
        self.patient = patient
        self.date = date
        self.disease = disease
        self.medication = medication

def print_physician(p_physician):
    print(p_physician.get_id(), p_physician.get_name(), p_physician.get_specialty())

def print_patient(p_patient):
    print(p_patient.get_emr_id(), p_patient.get_name(), p_patient.get_gender(), p_patient.get_phone_number())

def print_encounter(e_encounter):
    print(e_encounter.physician.get_name(), e_encounter.patient.get_name(), e_encounter.date, e_encounter.disease, e_encounter.medication)


def main():
    
    rows = []
    file = open('patients.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)
    file1 = open('physicians.csv')
    rows1 = []
    csvreader1 = csv.reader(file1)
    for row in csvreader1:   
        rows1.append(row) 

    patient1 = Patient(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
    patient2 = Patient(rows[1][0], rows[1][1], rows[1][2], rows[1][3])
    patient3 = Patient(rows[2][0], rows[2][1], rows[2][2], rows[2][3])
    patient4 = Patient(rows[3][0], rows[3][1], rows[3][2], rows[3][3])
    patient5 = Patient(rows[4][0], rows[4][1], rows[4][2], rows[4][3])
    patient6 = Patient(rows[5][0], rows[5][1], rows[5][2], rows[5][3])
    patient7 = Patient(rows[6][0], rows[6][1], rows[6][2], rows[6][3])
    patient8 = Patient(rows[7][0], rows[7][1], rows[7][2], rows[7][3])
    patient9 = Patient(rows[8][0], rows[8][1], rows[8][2], rows[8][3])
    patient10 = Patient(rows[9][0], rows[9][1], rows[9][2], rows[9][3])

    physician1 = Physician(rows1[0][0], rows1[0][1], rows1[0][2])
    physician2 = Physician(rows1[1][0], rows1[1][1], rows1[1][2])
    physician3 = Physician(rows1[2][0], rows1[2][1], rows1[2][2])

    encounter1 = Encounter(physician1, patient5, "7/12/2021", "Cancer", "Chemeo therapy")
    encounter2 = Encounter(physician2, patient3, "4/6/2014", "Headache", "Panadol")
    encounter3 = Encounter(physician3, patient4, "15/8/2017", "Runny nose", "Nose Spray")
    encounter4 = Encounter(physician2, patient9, "28/6/2019", "Stomach ache", "Stomach pain relief")
    encounter5 = Encounter(physician1, patient2, "22/3/2015", "Diarrhea", "Loperamide")

    print_physician(physician1)
    print_physician(physician1)
    print_physician(physician1)

    print_patient(patient1)
    print_patient(patient2)
    print_patient(patient3)
    print_patient(patient4)
    print_patient(patient5)
    print_patient(patient6)
    print_patient(patient7)
    print_patient(patient8)
    print_patient(patient9)
    print_patient(patient10)

    print_encounter(encounter1)
    print_encounter(encounter2)
    print_encounter(encounter3)
    print_encounter(encounter4)
    print_encounter(encounter5)

    with open('encounter.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        list = [
            [encounter1.physician.get_name(), encounter1.patient.get_name(), encounter1.date, encounter1.disease, encounter1.medication],
            [encounter2.physician.get_name(), encounter2.patient.get_name(), encounter2.date, encounter2.disease, encounter2.medication],
            [encounter3.physician.get_name(), encounter3.patient.get_name(), encounter3.date, encounter3.disease, encounter3.medication],
            [encounter4.physician.get_name(), encounter4.patient.get_name(), encounter4.date, encounter4.disease, encounter4.medication],
            [encounter5.physician.get_name(), encounter5.patient.get_name(), encounter5.date, encounter5.disease, encounter5.medication]
        ]
        writer.writerows(list)
        
main()