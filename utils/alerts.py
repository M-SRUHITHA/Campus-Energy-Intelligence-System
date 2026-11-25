
def generate_alerts(data):
    """
    Generate alerts for classrooms wasting electricity.
    """

    alerts = []

    wastage_data = data[data["energy_wastage"] == True]

    for _, row in wastage_data.iterrows():

        message = (
            f"{row['classroom']} is empty, but "
            f"{row['active_fans']} fans and "
            f"{row['active_lights']} lights are ON. "
            f"Power consumption: {row['power_watts']} W."
        )

        alerts.append({
            "classroom": row["classroom"],
            "timestamp": row["timestamp"],
            "power_watts": row["power_watts"],
            "message": message
        })

    return alerts
