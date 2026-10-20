from fhir_client import put_resource

SNOMED = "http://snomed.info/sct"
UCUM = "http://unitsofmeasure.org"
ORAL_ROUTE = {"coding": [{"system": SNOMED, "code": "26643006", "display": "Oral route"}]}


def make_medication_statement(res_id, snomed_code, display, start, dosage):
    """Build a MedicationStatement for Ana (one 'mould', many medicines)."""
    return {
        "resourceType": "MedicationStatement",
        "id": res_id,
        "status": "active",
        "medicationCodeableConcept": {
            "coding": [{"system": SNOMED, "code": snomed_code, "display": display}],
            "text": display,
        },
        "subject": {"reference": "Patient/fpps-ana-ferreira"},
        "effectivePeriod": {"start": start},
        "dosage": [dosage],
    }


paracetamol = make_medication_statement(
    res_id="fpps-ana-med-paracetamol",
    snomed_code="387517004",
    display="Paracetamol",
    start="2020",
    dosage={
        "text": "1 g orally, up to 3 times per day if needed",
        "asNeededBoolean": True,
        "route": ORAL_ROUTE,
        "doseAndRate": [{"doseQuantity": {"value": 1, "unit": "g", "system": UCUM, "code": "g"}}],
        "maxDosePerPeriod": {
            "numerator": {"value": 3, "unit": "g", "system": UCUM, "code": "g"},
            "denominator": {"value": 1, "unit": "d", "system": UCUM, "code": "d"},
        },
    },
)

duloxetine = make_medication_statement(
    res_id="fpps-ana-med-duloxetine",
    snomed_code="407032004",
    display="Duloxetine",
    start="2023-03",
    dosage={
        "text": "60 mg orally, once daily",
        "timing": {"repeat": {"frequency": 1, "period": 1, "periodUnit": "d"}},
        "route": ORAL_ROUTE,
        "doseAndRate": [{"doseQuantity": {"value": 60, "unit": "mg", "system": UCUM, "code": "mg"}}],
    },
)

for medication in [paracetamol, duloxetine]:
    put_resource(medication)