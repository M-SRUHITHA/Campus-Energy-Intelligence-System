
import pandas as pd


def detect_energy_wastage(data):
    """
    Detect possible energy wastage when a classroom
    is empty but electricity is still being consumed.
    """

    data = data.copy()

    data["energy_wastage"] = (
        (data["occupancy"] == 0) &
        (data["power_watts"] > 0)
    )

    data["alert_reason"] = data["energy_wastage"].apply(
        lambda x: (
            "Electricity wasted: Classroom is empty but power is ON"
            if x else "Normal"
        )
    )

    return data


def get_wastage_summary(data):
    """Generate a summary of energy wastage."""

    detected = data[data["energy_wastage"]]

    return {
        "total_alerts": len(detected),
        "affected_classrooms": detected["classroom"].nunique(),
        "wasted_energy_kwh": detected["power_watts"].sum() * 0.25 / 1000
    }
