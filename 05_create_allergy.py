from fhir_client import put_resource

allergy = {
    "resourceType": "AllergyIntolerance",
    "id": "fpps-ana-allergy-nsaid",
    "clinicalStatus": {
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical",
            "code": "active",
        }]
    },
    "verificationStatus": {
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-verification",
            "code": "confirmed",
        }]
    },
    "type": "allergy",
    "category": ["medication"],
    "criticality": "high",
    "code": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "372665008",
            "display": "Non-steroidal anti-inflammatory agent",
        }],
        "text": "NSAIDs (non-steroidal anti-inflammatory drugs)",
    },
    "patient": {"reference": "Patient/fpps-ana-ferreira"},
    "reaction": [{
        "manifestation": [
            {
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "126485001",
                    "display": "Urticaria",
                }]
            },
            {
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "41291007",
                    "display": "Angioedema",
                }]
            },
        ],
        "severity": "severe",
    }],
}

if __name__ == "__main__":
    put_resource(allergy)
