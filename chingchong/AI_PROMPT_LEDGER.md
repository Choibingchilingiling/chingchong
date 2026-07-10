# AI Prompt Ledger

## Bug 1 – Mutable Default Argument
Prompt:
Fix the mutable default list in TelemetryBuffer.

Reason:
Using [] as a default parameter shares the same list across instances.

Final Fix:
Use None as the default and create a new list inside __init__.

---

## Bug 2 – IMU Return Type
Prompt:
Make IMUPeripheral always return a float.

Reason:
Returning a dictionary violates the polymorphic contract.

Final Fix:
Return 0.0 instead of an error dictionary.

---

## Bug 3 – Race Condition
Prompt:
Protect the shared telemetry register using threading.Lock().

Reason:
Multiple threads modify the shared dictionary simultaneously.

Final Fix:
Wrap register updates with a mutex lock.