import json
import requests

BASE_URL = "https://hapi.fhir.org/baseR4"
HEADERS = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/fhir+json",
}


def put_resource(resource):
    """Create or update a FHIR resource at a known id (idempotent PUT)."""
    url = f"{BASE_URL}/{resource['resourceType']}/{resource['id']}"
    response = requests.put(url, headers=HEADERS, data=json.dumps(resource), timeout=30)
    print(f"{resource['resourceType']}/{resource['id']} -> HTTP {response.status_code}")
    if response.status_code >= 400:
        print(json.dumps(response.json(), indent=2))
    return response