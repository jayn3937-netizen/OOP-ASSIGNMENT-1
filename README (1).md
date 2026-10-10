# Vaccination Tracker (PROG211 – OOP1 Assignment)

A simple Python program that tracks vaccinations using Object-Oriented Programming.
Domain: **Health – Vaccination Tracker**.

## How it meets the tasks
| Task | Where |
|---|---|
| Classes, attributes, methods, object interaction | `Patient` and `Vaccine` classes; a Patient holds Vaccine objects |
| One data structure | A **dictionary** `registry = {patient_id: Patient}` |
| Add / display function | `add_record()` and `display_records()` |
| Instance methods | `add_vaccination()`, `update_record()`, `display_info()` |
| Class method | `get_total_patients()`, `from_dict()` (`@classmethod`) |
| Static method | `is_valid_vaccine()` (`@staticmethod`) |
| Tuple (bonus) | `VACCINE_TYPES` – immutable list of approved vaccines |

## How it aligns with Digital Public Goods (DPG) standards
- **Open-source:** hosted on GitHub with its code freely available (add a licence, e.g. MIT).
- **Inclusive & accessible:** plain-language messages, no special hardware; runs on any computer with Python 3.
- **Privacy-respecting:** no names, phone numbers or addresses are stored – only an anonymous ID, age group and district.
- **Modular & reusable:** separate classes and functions; the vaccine list and fields can be adapted for other health programmes.

## Run it
```
python vaccination_tracker.py
```

## Sample output
```
--- Adding patients ---
  Added patient P001
  Added patient P002
  Added patient P003

--- Recording vaccinations ---
  [!] 'Malaria' is not an approved vaccine.

=== VACCINATION REGISTRY ===
ID: P001 | Group: Child | District: Bo
   - BCG (given 2026-10-07)
   - Polio (given 2026-10-07)
ID: P002 | Group: Adult | District: Makeni
   - COVID-19 (given 2026-10-07)
ID: P003 | Group: Child | District: Kenema
   No vaccinations recorded.
Total patients: 3
```
