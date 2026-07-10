#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path


def build_config(student_id: str) -> dict:
    student_id = student_id.strip()

    if not student_id.isdigit() or len(student_id) != 8:
        raise ValueError("Student ID must be exactly 8 digits.")

    digest = hashlib.sha256(student_id.encode("utf-8")).hexdigest()

    # Keep values stable and safe for the simulator
    buffer_threshold = 25
    imu_voltage_drift = 1.0 + (int(digest[:2], 16) % 6) / 10.0  # 1.0 to 1.5
    bus_race_delay_sec = 0.002 + (int(digest[2:4], 16) % 3) * 0.001  # 0.002 to 0.004

    return {
        "student_id": student_id,
        "signature_hash": digest[:12].upper(),
        "buffer_overflow_threshold": buffer_threshold,
        "imu_voltage_drift": round(imu_voltage_drift, 2),
        "bus_race_delay_sec": round(bus_race_delay_sec, 3),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate hardware_config.json for avionics bus simulation.")
    parser.add_argument("--id", required=True, help="8-digit student ID")
    args = parser.parse_args()

    config = build_config(args.id)
    out_path = Path("hardware_config.json")
    out_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

    print(f"[OK] Wrote {out_path}")
    print(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()