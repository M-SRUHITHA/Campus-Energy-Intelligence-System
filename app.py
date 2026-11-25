
import streamlit as st
import pandas as pd
from pathlib import Path

from utils.data_processing import (
    load_classroom_data,
    clean_classroom_data,
    calculate_energy
)

from utils.ai_detection import (
    detect_energy_wastage,
    get_wastage_summary
)

from utils.alerts import generate_alerts

from utils.visualizations import (
    show_energy_chart,
    show_energy_trend,
    show_occupancy_chart
)


# Page configuration
st.set_page_config(
    page_title="EcoVerse",
    page_icon="🌱",
    layout="wide"
)

# Dashboard title
st.title("🌱 EcoVerse")
st.subheader("Campus Energy Intelligence System")

st.write(
    "Monitor classroom occupancy, electricity consumption, "
    "energy wastage and estimated carbon emissions."
)

st.markdown("---")

# Load classroom data
file_path = Path(__file__).parent / "data" / "classroom_data.csv"

try:
    data = load_classroom_data(file_path)
    data = clean_classroom_data(data)
    data = calculate_energy(data)

    if data.empty:
        st.warning("No classroom data available.")
        st.stop()

    # Detect energy wastage
    data = detect_energy_wastage(data)

    # Latest reading for each classroom
    latest_data = (
        data.sort_values("timestamp")
        .groupby("classroom")
        .tail(1)
    )

    # Campus overview
    st.header("🏫 Campus Overview")

    total_classrooms = data["classroom"].nunique()
    total_occupancy = latest_data["occupancy"].sum()
    total_energy = data["energy_kwh"].sum()

    summary = get_wastage_summary(data)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Classrooms Monitored", total_classrooms)
    col2.metric("Current Occupancy", int(total_occupancy))
    col3.metric("Total Energy", f"{total_energy:.2f} kWh")
    col4.metric("Wastage Alerts", summary["total_alerts"])

    st.markdown("---")

    # Classroom-wise occupancy
    st.header("👨‍🎓 Classroom Occupancy")

    st.dataframe(
        latest_data[
            ["classroom", "occupancy", "active_fans", "active_lights"]
        ].rename(columns={
            "classroom": "Classroom",
            "occupancy": "Students Present",
            "active_fans": "Active Fans",
            "active_lights": "Active Lights"
        }),
        use_container_width=True,
        hide_index=True
    )

    # Visualizations
    st.markdown("---")
    st.header("📊 Energy and Occupancy Analysis")

    show_energy_chart(data)
    show_energy_trend(data)
    show_occupancy_chart(data)

    # Alerts
    st.markdown("---")
    st.header("🚨 Energy Wastage Alerts")

    alerts = generate_alerts(data)

    if alerts:
        for alert in alerts:
            st.warning(
                f"⚠️ {alert['message']} "
                f"({alert['timestamp']})"
            )
    else:
        st.success("No energy wastage detected!")

    st.metric(
        "Estimated Wasted Energy",
        f"{summary['wasted_energy_kwh']:.2f} kWh"
    )

    st.markdown("---")
    st.success("EcoVerse dashboard is running successfully!")

except FileNotFoundError:
    st.error("Classroom CSV file not found. Check the data folder.")

except Exception as e:
    st.error(f"Something went wrong: {e}")
