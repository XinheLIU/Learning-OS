# Case: Patch Before Reproducing

Last updated: 2026-07-23

**Date:** 2026-07-23
**Micro-goal:** Reproduce a reported timeout before changing retry settings.
**Scenario:** A request intermittently times out in production.
**Models applied:** record 0004 - reproduce before patching
**What worked:** The learner located the request path.
**Errors made:** Changed the retry count without reproducing or isolating the timeout.

**Attempt 1:** Increased the retry count from two to five.
**Observed failure:** The timeout still occurred and generated more duplicate work.
**Hypothesis:** Two retries were insufficient for transient failures.
**Feedback:** Reproduce the timeout and identify which operation exceeds its deadline.

**Assistance used:** a little help
**Next support to remove:** use less help next time
**Takeaway:** Reproduce before tuning retries.
