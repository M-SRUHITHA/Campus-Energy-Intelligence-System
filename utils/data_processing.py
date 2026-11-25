
import pandas as pd


def load_classroom_data(file_path):
    """Load classroom readings from a CSV file."""

    data = pd.read_csv(file_path)

    return data


def clean_classroom_data(data):
    """Clean and prepare classroom readings."""

    data = data.drop_duplicates()

    data = data.dropna()

    data["timestamp"] = pd.to_datetime(data["timestamp"])

    return data


def calculate_energy(data):
    """Calculate energy consumption in kWh."""

    data["energy_kwh"] = data["power_watts"] * 0.25 / 1000

    return data
