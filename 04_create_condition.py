from fhir_client import put_resource

condition = {
    "resourceType": "Condition",
    "id": "fpps-ana-condition-clbp",
    "clinicalStatus": {
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
            "code": "active",
        }]
    },
    "verificationStatus": {
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
            "code": "confirmed",
        }]
    },
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/condition-category",
            "code": "problem-list-item",
        }]
    }],
    "code": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "278860009",
            "display": "Chronic low back pain",
        }],
        "text": "Chronic low back pain",
    },
    "subject": {"reference": "Patient/fpps-ana-ferreira"},
    "onsetDateTime": "2020",
    "note": [{
        "text": (
            "Pain usually localised to the lumbar region, no radiation to the lower limbs "
            "and no neurological deficits in previous assessments. Red flags excluded: "
            "lumbar MRI (2021) showed no fracture, tumour or inflammatory disease. "
            "Paracetamol provides partial relief; exercise therapy/physiotherapy has helped."
        )
    }],
}

if __name__ == "__main__":
    put_resource(condition)
