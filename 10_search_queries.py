import requests

from fhir_client import BASE_URL, HEADERS

PATIENT = "fpps-ana-ferreira"
IDENTIFIER_SYSTEM = "https://github.com/RenatoMurayama/fhir-pain-patient-summary/patient-id"


def search(description, resource_type, params):
    """Run a FHIR search and return the list of resources found."""
    response = requests.get(f"{BASE_URL}/{resource_type}", headers=HEADERS, params=params, timeout=30)
    entries = response.json().get("entry", [])
    print(f"\n{description}")
    print(f"  GET {response.url}")
    print(f"  HTTP {response.status_code} | results: {len(entries)}")
    return [entry["resource"] for entry in entries]


# 1) Find Ana by her source-system identifier (as another hospital would)
patients = search("1) Find patient by identifier", "Patient",
                  {"identifier": f"{IDENTIFIER_SYSTEM}|ANA-0001"})
for p in patients:
    print("  ->", p["id"], "|", p["name"][0]["given"][0], p["name"][0]["family"], "|", p["birthDate"])

# 2) Active allergies (the safety question)
allergies = search("2) Active allergies", "AllergyIntolerance",
                   {"patient": PATIENT, "clinical-status": "active"})
for a in allergies:
    print("  ->", a["code"]["text"], "| criticality:", a["criticality"])

# 3) Active medications
medications = search("3) Active medications", "MedicationStatement",
                     {"patient": PATIENT, "status": "active"})
for m in medications:
    print("  ->", m["medicationCodeableConcept"]["text"], "|", m["dosage"][0]["text"])

# 4) Most recent pain score
pain = search("4) Most recent pain score", "Observation",
              {"patient": PATIENT, "code": "http://loinc.org|72514-3", "_sort": "-date", "_count": 1})
for o in pain:
    print("  ->", o["valueQuantity"]["value"], "/10 on", o["effectiveDateTime"], "|", o["note"][0]["text"])