# Case: Diagnose Stale Cache Reads

Last updated: 2026-07-23

**Date:** 2026-07-23
**Micro-goal:** Test the cache-key hypothesis before changing invalidation logic.
**Cell:** cache consistency x can-apply
**Scenario:** A profile update succeeds, but the next API read returns the old display name. The learner must localize whether the stale value comes from the write path, cache key, or invalidation event.
**Models applied:** record 0003 - trace state transitions before patching
**What worked:** The learner reproduced the stale read and compared the write and read keys.
**Errors made:** Assumed invalidation was delayed before checking that both paths used the same key.

**Attempt 1:** Increased the invalidation consumer timeout and reran the scenario.
**Observed failure:** The stale read remained because the consumer timing was unrelated to the mismatched keys.
**Hypothesis:** The invalidation event was processed too slowly.
**Feedback:** Compare the exact cache key produced by the write path with the key used by the read path.
**Retry:** Logged both keys, found different tenant prefixes, aligned the write key, and reran the scenario.
**Result:** resolved

**Assistance used:** hint
**Next support to remove:** no hint about comparing cache keys on the next consistency case
**Takeaway:** Verify identity and state transitions before tuning timing.
