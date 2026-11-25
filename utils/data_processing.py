
import pandas as pd


def load_classroom_data(file_path):
    """Load classroom readings from a CSV file."""
    data = pd.read_csv(file_path)
    return data


def clean_classroom_data(data):
    """Clean and validate classroom readings."""

    data = data.copy()

    # Remove duplicate records
    data = data.drop_duplicates()

    # Convert timestamp to datetime
    data["timestamp"] = pd.to_datetime(
        data["timestamp"], errors="coerce"
    )

    # Convert numeric columns safely
    numeric_columns = [
        "occupancy",
        "active_fans",
        "active_lights",
        "power_watts"
    ]

    for column in numeric_columns:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )

    # Remove missing and invalid values
    data = data.dropna(
        subset=["timestamp", "classroom"] + numeric_columns
    )

    # Remove impossible negative readings
    data = data[
        (data["occupancy"] >= 0) &
        (data["active_fans"] >= 0) &
        (data["active_lights"] >= 0) &
        (data["power_watts"] >= 0)
    ]

    return data.reset_index(drop=True)


def calculate_energy(data):
    """Calculate energy consumption in kWh."""

    data = data.copy()

    # 15-minute interval energy calculation
    data["energy_kwh"] = (
        data["power_watts"] * 0.25 / 1000
    )

    return data
