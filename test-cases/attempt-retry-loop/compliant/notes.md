# Notes: Cache Consistency

Last updated: 2026-07-23

## Records

### 0003 - Trace state transitions before patching  (2026-07-23)
The learner can localize stale state by comparing the identifiers and transitions on the write and read paths before changing timing or invalidation behavior.
**Evidence:** Resolved the stale-profile case by finding mismatched tenant prefixes on retry.
**Assistance:** hint

## Attempt Log

- 2026-07-23 S0003 cache-key diagnosis: predicted delayed invalidation -> wrong: write and read keys differed -> retry resolved [assistance: hint]

## Terms

- **Cache key identity** - The complete identifier that must match across cache writes, reads, and invalidations.

## Preferences

- Ask for a concrete prediction before offering a debugging hint.
