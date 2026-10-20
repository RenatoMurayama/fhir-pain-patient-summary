import importlib
import json
import os
import uuid
from datetime import datetime, timezone

from fhir_client import BASE_URL


def load(module_name, variable_name):
    return getattr(importlib.import_module(module_name), variable_name)


patient = load("03_create_patient", "patient")
condition = load("04_create_condition", "condition")
allergy = load("05_create_allergy", "allergy")
paracetamol = load("06_create_medications", "paracetamol")
duloxetine = load("06_create_medications", "duloxetine")

practitioner = {
    "resourceType": "Practitioner",
    "id": "fpps-dr-joana-costa",
    "name": [{"family": "Costa", "given": ["Joana"], "prefix": ["Dr."]}],
}


def ref(resource):
    return {"reference": f"{resource['resourceType']}/{resource['id']}"}


def narrative(html):
    return {"status": "generated", "div": f'<div xmlns="http://www.w3.org/1999/xhtml">{html}</div>'}


def section(title, loinc_code, loinc_display, html, entries):
    return {
        "title": title,
        "code": {"coding": [{"system": "http://loinc.org", "code": loinc_code, "display": loinc_display}]},
        "text": narrative(html),
        "entry": [ref(e) for e in entries],
    }


now = datetime.now(timezone.utc).isoformat(timespec="seconds")

composition = {
    "resourceType": "Composition",
    "id": "fpps-ana-ips-composition",
    "status": "final",
    "type": {"coding": [{"system": "http://loinc.org", "code": "60591-5", "display": "Patient summary Document"}]},
    "subject": ref(patient),
    "date": now,
    "author": [ref(practitioner)],
    "title": "International Patient Summary - Ana Ferreira",
    "section": [
        section("Problem List", "11450-4", "Problem list - Reported",
                "<p>Chronic low back pain (since 2020). No radiation, no neurological deficits; "
                "red flags excluded (MRI 2021).</p>",
                [condition]),
        section("Allergies and Intolerances", "48765-2", "Allergies and adverse reactions Document",
                "<p><b>NSAIDs - HIGH criticality.</b> Reactions: urticaria and angioedema.</p>",
                [allergy]),
        section("Medication Summary", "10160-0", "History of Medication use Narrative",
                "<ul><li>Paracetamol 1 g orally, up to 3 times per day if needed</li>"
                "<li>Duloxetine 60 mg orally, once daily</li></ul>",
                [paracetamol, duloxetine]),
    ],
}

# Resource-level narrative (fixes dom-6 best-practice warnings)
composition["text"] = narrative("<p>International Patient Summary for Ana Ferreira</p>")
patient["text"] = narrative("<p>Ana Ferreira, female, born 1981-04-12, Braga (PT)</p>")
practitioner["text"] = narrative("<p>Dr. Joana Costa, family physician</p>")
condition["text"] = narrative("<p>Chronic low back pain - active, since 2020</p>")
allergy["text"] = narrative(
    "<p><b>Allergy to NSAIDs - HIGH criticality.</b> Reactions: urticaria, angioedema</p>"
)
for med in [paracetamol, duloxetine]:
    med["text"] = narrative(f"<p>{med['medicationCodeableConcept']['text']}: {med['dosage'][0]['text']}</p>")

resources = [composition, patient, practitioner, condition, allergy, paracetamol, duloxetine]

bundle = {
    "resourceType": "Bundle",
    "id": "fpps-ana-ips-document",
    "meta": {"profile": ["http://hl7.org/fhir/uv/ips/StructureDefinition/Bundle-uv-ips"]},
    "identifier": {"system": "urn:ietf:rfc:3986", "value": f"urn:uuid:{uuid.uuid4()}"},
    "type": "document",
    "timestamp": now,
    "entry": [
        {"fullUrl": f"{BASE_URL}/{r['resourceType']}/{r['id']}", "resource": r}
        for r in resources
    ],
}

os.makedirs("output", exist_ok=True)
with open("output/patient_summary_bundle.json", "w", encoding="utf-8") as f:
    json.dump(bundle, f, indent=2, ensure_ascii=False)

print("Patient Summary saved: output/patient_summary_bundle.json")
print("Entries:", len(bundle["entry"]))