import importlib
import json
import os

import requests

from fhir_client import BASE_URL, HEADERS


def load(module_name, variable_name):
    """Import a resource defined in another script, without sending it."""
    return getattr(importlib.import_module(module_name), variable_name)


patient = load("03_create_patient", "patient")
condition = load("04_create_condition", "condition")
allergy = load("05_create_allergy", "allergy")
paracetamol = load("06_create_medications", "paracetamol")
duloxetine = load("06_create_medications", "duloxetine")
observations = load("07_create_observations", "observations")

resources = [patient, condition, allergy, paracetamol, duloxetine, *observations]


def to_entry(resource):
    relative_url = f"{resource['resourceType']}/{resource['id']}"
    return {
        "fullUrl": f"{BASE_URL}/{relative_url}",
        "resource": resource,
        "request": {"method": "PUT", "url": relative_url},
    }


bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [to_entry(resource) for resource in resources],
}

# Save a copy of the bundle for the portfolio
os.makedirs("output", exist_ok=True)
with open("output/transaction_bundle.json", "w", encoding="utf-8") as f:
    json.dump(bundle, f, indent=2, ensure_ascii=False)

response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(bundle), timeout=60)
print("HTTP status:", response.status_code)

result = response.json()
print("Response type:", result.get("type"))
for entry in result.get("entry", []):
    print(" -", entry["response"]["status"], entry["response"].get("location"))