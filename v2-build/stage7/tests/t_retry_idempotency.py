"""Artifact: retry + idempotency toy. Local only, no network, no charges."""
import time

class FlakyLedger:
    """Simulates a payment backend: fails N times, then succeeds.
    Honors idempotency keys: same key twice = one charge."""
    def __init__(self, fail_times):
        self.fail_times = fail_times
        self.calls = 0
        self.charges = {}  # key -> amount

    def charge(self, key, amount_cents):
        self.calls += 1
        if key in self.charges:
            return {"status": "duplicate", "charged_cents": self.charges[key]}
        if self.calls <= self.fail_times:
            raise ConnectionError("simulated flake")
        self.charges[key] = amount_cents
        return {"status": "charged", "charged_cents": amount_cents}

def charge_with_retry(ledger, key, amount_cents, timeout_s=0.2, max_attempts=3, backoff=(0.05, 0.1)):
    start = time.monotonic()
    attempt = 0
    while True:
        attempt += 1
        try:
            return ledger.charge(key, amount_cents), attempt
        except ConnectionError:
            elapsed = time.monotonic() - start
            if attempt >= max_attempts or elapsed + timeout_s > 0.6:
                raise
            time.sleep(backoff[min(attempt - 1, len(backoff) - 1)])

# Run 1: 2 flakes then success, same business key reused on a duplicate delivery
ledger = FlakyLedger(fail_times=2)
res, attempts = charge_with_retry(ledger, "inv-1042", 4599)
print("run1:", res, "attempts:", attempts, "backend calls:", ledger.calls)
# Run 2: duplicate delivery of the same charge (network duplicate)
res2, _ = charge_with_retry(ledger, "inv-1042", 4599)
print("run2 duplicate:", res2, "total distinct charges:", len(ledger.charges))
# Run 3: outage (always fails) -> raises after max_attempts
ledger2 = FlakyLedger(fail_times=99)
try:
    charge_with_retry(ledger2, "inv-1043", 100)
    print("run3: UNEXPECTED SUCCESS")
except ConnectionError:
    print("run3: raised after", ledger2.calls, "backend calls; distinct charges:", len(ledger2.charges))
