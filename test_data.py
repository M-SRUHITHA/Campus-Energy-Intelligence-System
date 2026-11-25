
from utils.data_processing import (
    load_classroom_data,
    clean_classroom_data,
    calculate_energy
)

# Load classroom data
data = load_classroom_data("data/classroom_data.csv")

# Clean the data
data = clean_classroom_data(data)

# Calculate energy consumption
data = calculate_energy(data)

# Display the results
print(data[["classroom", "occupancy", "power_watts", "energy_kwh"]])

print("\nData processing completed successfully!")
