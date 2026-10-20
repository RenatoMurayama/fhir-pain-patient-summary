from fhir_client import put_resource

LOINC = "http://loinc.org"
UCUM = "http://unitsofmeasure.org"


def make_pain_observation(res_id, score, when, context):
    """Build a pain intensity (0-10 NRS) Observation for Ana."""
    return {
        "resourceType": "Observation",
        "id": res_id,
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "survey",
            }]
        }],
        "code": {
            "coding": [{
                "system": LOINC,
                "code": "72514-3",
                "display": "Pain severity - 0-10 verbal numeric rating [Score] - Reported",
            }],
            "text": "Pain intensity (0-10 NRS)",
        },
        "subject": {"reference": "Patient/fpps-ana-ferreira"},
        "effectiveDateTime": when,
        "valueQuantity": {"value": score, "unit": "{score}", "system": UCUM, "code": "{score}"},
        "note": [{"text": context}],
    }


observations = [
    make_pain_observation("fpps-ana-pain-2026-09-15", 4, "2026-09-15", "Routine follow-up"),
    make_pain_observation("fpps-ana-pain-2026-10-10", 8, "2026-10-10", "Acute flare while travelling in Spain"),
]

for observation in observations:
    put_resource(observation)