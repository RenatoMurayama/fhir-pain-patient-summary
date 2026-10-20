import copy
import json

import requests

from fhir_client import BASE_URL, HEADERS

with open("output/transaction_bundle.json", encoding="utf-8") as f:
    original_bundle = json.load(f)

test_bundle = copy.deepcopy(original_bundle)

for entry in test_bundle["entry"]:
    resource = entry["resource"]
    # 1) VALID change
    if resource["resourceType"] == "Condition":
        resource["note"][0]["text"] = "ATOMICITY TEST - this text must NOT be saved"
    # 2) INVALID change: reference to a patient that does not exist
    if resource["id"] == "fpps-ana-pain-2026-10-10":
        resource["subject"]["reference"] = "Patient/does-not-exist-12345"

response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(test_bundle), timeout=60)
print("Transaction HTTP status:", response.status_code)
for issue in response.json().get("issue", []):
    print("Server says:", issue.get("diagnostics"))

# Did the VALID change get saved?
condition = requests.get(
    f"{BASE_URL}/Condition/fpps-ana-condition-clbp", headers=HEADERS, timeout=30
).json()
print("Condition versionId:", condition["meta"]["versionId"])
print("Condition note starts with:", condition["note"][0]["text"][:40])