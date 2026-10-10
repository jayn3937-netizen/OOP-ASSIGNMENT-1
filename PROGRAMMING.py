"""
Vaccination Tracker - PROG211 OOP1 Assignment
Domain: Health | Follows Digital Public Goods (DPG) principles.

Privacy by design: no names, phone numbers or addresses are stored.
Each person is represented only by an anonymous ID, an age group and
their vaccination history.
"""

from datetime import date

# Tuple (immutable): approved vaccines - cannot be changed accidentally
VACCINE_TYPES = ("BCG", "Polio", "Measles", "Pentavalent", "COVID-19")


class Vaccine:
    """A vaccine dose that was given."""

    def __init__(self, name, date_given=None):
        self.name = name
        self.date_given = date_given or date.today()

    def display_info(self):
        return f"{self.name} (given {self.date_given.isoformat()})"


class Patient:
    """An anonymous patient (no sensitive personal data)."""

    total_patients = 0  # class attribute shared by all objects

    def __init__(self, patient_id, age_group, district):
        self.patient_id = patient_id
        self.age_group = age_group      # e.g. "Child", "Adult"
        self.district = district        # general area only
        self.vaccinations = []          # list of Vaccine objects
        Patient.total_patients += 1

    # ---------- Instance methods ----------
    def add_vaccination(self, vaccine_name):
        """Record a vaccine dose for this patient."""
        if not Patient.is_valid_vaccine(vaccine_name):
            print(f"  [!] '{vaccine_name}' is not an approved vaccine.")
            return False
        self.vaccinations.append(Vaccine(vaccine_name))
        return True

    def update_record(self, district=None, age_group=None):
        """Update non-sensitive details."""
        if district:
            self.district = district
        if age_group:
            self.age_group = age_group

    def display_info(self):
        print(f"ID: {self.patient_id} | Group: {self.age_group} | District: {self.district}")
        if not self.vaccinations:
            print("   No vaccinations recorded.")
        for v in self.vaccinations:
            print("   -", v.display_info())

    # ---------- Class method ----------
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    @classmethod
    def from_dict(cls, data):
        """Alternative constructor: build a Patient from a dictionary."""
        return cls(data["id"], data["age_group"], data["district"])

    # ---------- Static method ----------
    @staticmethod
    def is_valid_vaccine(name):
        """Utility check - needs no object or class data."""
        return name in VACCINE_TYPES


# ---------- Data structure: dictionary {patient_id: Patient} ----------
registry = {}


def add_record(patient):
    """Add a patient to the registry."""
    if patient.patient_id in registry:
        print(f"  [!] ID {patient.patient_id} already exists.")
        return
    registry[patient.patient_id] = patient
    print(f"  Added patient {patient.patient_id}")


def display_records():
    """Display all records in the registry."""
    print("\n=== VACCINATION REGISTRY ===")
    for patient in registry.values():
        patient.display_info()
    print(f"Total patients: {Patient.get_total_patients()}")


def main():
    print("--- Adding patients ---")
    p1 = Patient("P001", "Child", "Bo")
    p2 = Patient("P002", "Adult", "Freetown")
    p3 = Patient.from_dict({"id": "P003", "age_group": "Child", "district": "Kenema"})
    for p in (p1, p2, p3):
        add_record(p)

    print("\n--- Recording vaccinations ---")
    p1.add_vaccination("BCG")
    p1.add_vaccination("Polio")
    p2.add_vaccination("COVID-19")
    p3.add_vaccination("Malaria")   # invalid -> rejected

    print("\n--- Updating a record ---")
    p2.update_record(district="Makeni")

    display_records()

    print("\n--- Look up by ID (dictionary key) ---")
    registry["P001"].display_info()


if __name__ == "__main__":
    main()