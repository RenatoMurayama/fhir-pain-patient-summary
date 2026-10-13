# Clinical Case — Ana Ferreira (synthetic patient)

> All data in this project is fictional. No real patient information is used.

## Scenario
Ana Ferreira, 45-year-old woman living in Braga, Portugal, has had chronic
low back pain for about 6 years. While travelling in Spain, she has an acute
flare and goes to an emergency department. The Spanish physician has no
access to her Portuguese health record.

## Why a Patient Summary matters here
Ana is allergic to NSAIDs (non-steroidal anti-inflammatory drugs). Without
this information, the physician could prescribe ibuprofen, a common first
choice for acute back pain. A cross-border Patient Summary (IPS-based)
makes her key clinical data available in a standard, machine-readable format.

## Clinical data to include
| Category | Data |
|---|---|
| Patient | Ana Ferreira, female, born 1981-04-12, Braga, Portugal |
| Problem | Chronic low back pain, onset 2020 |
| Allergy | NSAIDs — reaction: urticaria and facial angioedema, high criticality |
| Medication 1 | Paracetamol 1 g orally, up to 3 times per day if needed |
| Medication 2 | Duloxetine 60 mg orally, once daily |
| Observation 1 | Pain intensity 4/10 (NRS) — routine follow-up, 2026-09-15 |
| Observation 2 | Pain intensity 8/10 (NRS) — acute flare, 2026-10-10 |

## Clinical notes for the receiving physician (free text)
- Pain is usually localised to the lumbar region, with no radiation to the lower limbs and no neurological deficits in previous assessments.
- Red flags excluded: lumbar MRI (2021) showed no fracture, tumour or inflammatory disease.
- Paracetamol provides partial relief. Exercise therapy / physiotherapy has helped manage both chronic pain and previous flares.

## Out of scope (planned for v2)
A full physiotherapy assessment (functional limitations, aggravating and easing factors, pain mechanism, serial pain measurements by posture/activity) belongs in a dedicated clinical record, not in a minimal Patient Summary.