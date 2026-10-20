# Design Decisions & Lessons Learned

## 1. Scope: a minimal Patient Summary
The IPS is a minimal, specialty-agnostic summary for unplanned cross-border care.
A full physiotherapy assessment (function, aggravating/easing factors, pain mechanism)
was deliberately left out and planned for v2. Deciding what belongs in a summary —
and what belongs elsewhere — is part of interoperability work.

## 2. Coded data vs free text
Safety-critical data is coded (diagnosis, allergy, medications, pain score).
Clinical context (no radiation, red flags excluded, response to treatment) is kept
as free text in `Condition.note`: useful for the clinician, but not worth the
modelling cost in a minimal summary.

## 3. Terminology choices
- Allergy: coded as the **substance** (SNOMED CT 372665008 | Non-steroidal
  anti-inflammatory agent), not a "situation" concept (e.g. 416759002 | NSAIDs
  contraindicated).
- Reactions: coded separately in `reaction.manifestation` (Urticaria, Angioedema)
  instead of the pre-coordinated 241959003 | NSAID-induced angioedema-urticaria,
  to avoid double coding the causative agent.
- Pain: LOINC **72514-3** (Pain severity 0-10, point in time, quantitative) instead
  of 75893-8 (pain *in the past week*, ordinal survey item) — same number, different
  clinical meaning.

## 4. Idempotent writes (PUT with client-defined ids)
Resources are written with `PUT` to known ids, so re-running a script never creates
duplicate patients — a real patient-safety issue in integration (retries after
network failures). HAPI does not create a new version when the content is unchanged.

## 5. Transaction Bundle (all-or-nothing)
All resources are sent in one `transaction` Bundle, so the record is never left
half-updated. **Evidence** (`09_atomicity_test.py`): a Bundle with one valid change
(Condition note) and one invalid reference (Observation → non-existent Patient)
was rejected with HTTP 400 (`HAPI-1094`), and the valid change was **not** saved
(Condition `versionId` stayed at 1). A `batch` Bundle would have saved the valid
entry and rejected only the invalid one.

## 6. Finding the patient across systems
Another hospital does not know the server-assigned `id`; it knows the patient's
identifier in the source system. The first query is therefore
`Patient?identifier=system|value` — patient identification comes before any
clinical data (allergies, medications), as a patient-safety rule.