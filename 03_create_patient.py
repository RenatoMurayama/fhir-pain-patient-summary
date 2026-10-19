import json
import requests

BASE_URL = "https://hapi.fhir.org/baseR4"
HEADERS = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/fhir+json",
}
PATIENT_ID = "fpps-ana-ferreira"

patient = {
    "resourceType": "Patient",
    "id": PATIENT_ID,
    "identifier": [
        {
            "system": "https://github.com/RenatoMurayama/fhir-pain-patient-summary/patient-id",
            "value": "ANA-0001",
        }
    ],
    "name": [{"family": "Ferreira", "given": ["Ana"]}],
    "gender": "female",
    "birthDate": "1981-04-12",
    "address": [{"city": "Braga", "country": "PT"}],
}

response = requests.put(
    f"{BASE_URL}/Patient/{PATIENT_ID}",
    headers=HEADERS,
    data=json.dumps(patient),
    timeout=30,
)

print("HTTP status:", response.status_code)
print(json.dumps(response.json(), indent=2))