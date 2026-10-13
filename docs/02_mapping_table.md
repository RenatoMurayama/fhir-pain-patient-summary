# Mapping Table — Clinical data → FHIR R4 (IPS)

| Clinical data | FHIR resource | FHIR element | Code system | Code | Display |
|---|---|---|---|---|---|
| Ana Ferreira, female, 1981-04-12, Braga | Patient | name, gender, birthDate, address | — | — | — |
| Chronic low back pain | Condition | code | SNOMED CT | 278860009 | Chronic low back pain |
| NSAID allergy (substance) | AllergyIntolerance | code | SNOMED CT | 372665008 | Non-steroidal anti-inflammatory agent |
| Reaction: urticaria | AllergyIntolerance | reaction.manifestation | SNOMED CT | 126485001 | Urticaria |
| Reaction: angioedema | AllergyIntolerance | reaction.manifestation | SNOMED CT | 41291007 | Angioedema |
| Paracetamol | MedicationStatement | medicationCodeableConcept | SNOMED CT | 387517004 | Paracetamol |
| Duloxetine | MedicationStatement | medicationCodeableConcept | SNOMED CT | 407032004 | Duloxetine |
| Pain intensity 0–10 (NRS) | Observation | code | LOINC | 72514-3 | Pain severity - 0-10 verbal numeric rating [Score] - Reported |
| Clinical notes (free text) | Condition | note | — | — | — |