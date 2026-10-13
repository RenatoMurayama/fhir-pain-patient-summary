import requests

BASE_URL = "https://hapi.fhir.org/baseR4"
HEADERS = {"Accept": "application/fhir+json"}

response = requests.get(f"{BASE_URL}/metadata", headers=HEADERS, timeout=30)
print("HTTP status:", response.status_code)

capability = response.json()
print("resourceType:", capability.get("resourceType"))
print("fhirVersion:", capability.get("fhirVersion"))
print("software:", capability.get("software", {}).get("name"))