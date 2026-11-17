class Hospital:
    def __init__(self):
        self.queue = []

    # 1. Add Patient (Enqueue)
    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")

        print("\nPriority:")
        print("1. Critical")
        print("2. Serious")
        print("3. Normal")

        priority = int(input("Enter Priority (1-3): "))

        if priority not in [1, 2, 3]:
            print("Invalid Priority!")
            return

        patient = {
            "id": patient_id,
            "name": name,
            "priority": priority
        }

        self.queue.append(patient)

        # Sort patients according to priority
        self.queue.sort(key=lambda x: x["priority"])

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if not self.queue:
            print("No patients waiting!")
        else:
            patient = self.queue[0]
            print("\nNext Patient to be Treated:")
            print("Patient ID:", patient["id"])
            print("Patient Name:", patient["name"])
            print("Priority:", patient["priority"])

    # 3. Remove Patient (Dequeue)
    def dequeue(self):
        if not self.queue:
            print("No patients to treat!")
        else:
            patient = self.queue.pop(0)
            print("\nPatient Treated Successfully!")
            print("Patient ID:", patient["id"])
            print("Patient Name:", patient["name"])

    # 4. Display All Waiting Patients
    def display_all(self):
        if not self.queue:
            print("No waiting patients!")
        else:
            print("\nWaiting Patients in Priority Order:")


            for patient in self.queue:
                if patient["priority"] == 1:
                    status = "Critical"
                elif patient["priority"] == 2:
                    status = "Serious"
                else:
                    status = "Normal"

                print("Patient ID:", patient["id"])
                print("Patient Name:", patient["name"])
                print("Priority:", status)


# Main Program
hospital = Hospital()

while True:
    print("\n HOSPITAL EMERGENCY MANAGEMENT ")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient (Dequeue)")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hospital.add_patient()

    elif choice == 2:
        hospital.display_next()

    elif choice == 3:
        hospital.dequeue()

    elif choice == 4:
        hospital.display_all()

    elif choice == 5:
        print("Exiting Hospital Management System...")
        break

    else:
        print("Invalid Choice! Please try again.")
