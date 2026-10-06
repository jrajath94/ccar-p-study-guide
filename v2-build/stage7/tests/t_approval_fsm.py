"""Artifact: approval state machine toy. Local only, no network."""
TRANSITIONS = {
    "requested": {"approve": "approved", "deny": "denied", "expire": "expired"},
    "approved": {"execute": "executed", "expire": "expired"},
    "denied": {},
    "expired": {},
    "executed": {},
}

class Approval:
    def __init__(self, action_id):
        self.action_id = action_id
        self.state = "requested"

    def event(self, name):
        nxt = TRANSITIONS[self.state].get(name)
        if nxt is None:
            raise ValueError("illegal: %s from %s" % (name, self.state))
        self.state = nxt
        return self.state

checks = []
a = Approval("refund-881")
checks.append(a.event("approve") == "approved")
checks.append(a.event("execute") == "executed")
b = Approval("refund-882")
checks.append(b.event("deny") == "denied")
c = Approval("refund-883")
try:
    c.event("execute"); checks.append(False)   # must fail: not approved
except ValueError:
    checks.append(True)
d = Approval("refund-884")
checks.append(d.event("expire") == "expired")
try:
    d.event("approve"); checks.append(False)   # must fail: expired is terminal
except ValueError:
    checks.append(True)
e = Approval("refund-885")
e.event("approve")
try:
    e.event("approve"); checks.append(False)   # must fail: double approve
except ValueError:
    checks.append(True)
print("approval FSM checks:", checks, "->", "ALL PASS" if all(checks) else "FAIL")
