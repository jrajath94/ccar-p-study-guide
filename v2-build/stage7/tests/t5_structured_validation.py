"""Artifact T5: structured-output validation toy. Local only, no network."""
import json

SCHEMA = {
    "type": "object",
    "required": ["invoice_id", "total_cents", "currency"],
    "properties": {
        "invoice_id": {"type": "string", "minLength": 1},
        "total_cents": {"type": "integer", "minimum": 0},
        "currency": {"type": "string", "enum": ["USD", "EUR", "INR"]},
    },
    "additionalProperties": False,
}

def validate(payload: dict):
    errors = []
    if not isinstance(payload, dict):
        return ["not an object"]
    for f in SCHEMA["required"]:
        if f not in payload:
            errors.append("missing field: " + f)
    props = SCHEMA["properties"]
    for k, v in payload.items():
        if k not in props:
            errors.append("extra field: " + k)
            continue
        spec = props[k]
        if spec["type"] == "string" and not isinstance(v, str):
            errors.append(k + ": not a string")
        if spec["type"] == "integer" and not isinstance(v, int):
            errors.append(k + ": not an integer")
        if spec.get("minimum") is not None and isinstance(v, int) and v < spec["minimum"]:
            errors.append(k + ": below minimum")
        if spec.get("enum") and v not in spec["enum"]:
            errors.append(k + ": not in enum")
        if spec.get("minLength") and isinstance(v, str) and len(v) < spec["minLength"]:
            errors.append(k + ": empty string")
    return errors

cases = {
    "valid": {"invoice_id": "INV-1042", "total_cents": 4599, "currency": "USD"},
    "missing_field": {"invoice_id": "INV-1042", "currency": "USD"},
    "bad_enum": {"invoice_id": "INV-1042", "total_cents": 4599, "currency": "GBP"},
    "extra_field": {"invoice_id": "INV-1042", "total_cents": 4599, "currency": "USD", "note": "x"},
    "negative_total": {"invoice_id": "INV-1042", "total_cents": -5, "currency": "USD"},
}
for name, payload in cases.items():
    errs = validate(payload)
    print(name, "->", "PASS" if not errs else "FAIL " + "; ".join(errs))
