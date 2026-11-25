
import streamlit as st
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


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EcoVerse | Campus Intelligence",
    page_icon="🌿",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM DESIGN - ECOVERSE
# --------------------------------------------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #F5F8F5 !important;
    color: #263D30 !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #F5F8F5 !important;
}

[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Main headings */
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4 {
    color: #174D35 !important;
    opacity: 1 !important;
    font-weight: 750 !important;
}

/* Paragraph text */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] p {
    color: #304B3B !important;
    opacity: 1 !important;
}

/* Labels and captions */
[data-testid="stMain"] label {
    color: #304B3B !important;
    opacity: 1 !important;
}

[data-testid="stMain"] [data-testid="stCaptionContainer"] {
    color: #648071 !important;
    opacity: 1 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #123B2B !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
    opacity: 1 !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #FFFFFF !important;
}

/* Main title */
.main-title {
    color: #174D35 !important;
    font-size: 38px;
    font-weight: 800;
    opacity: 1 !important;
}

/* Subtitle */
.subtitle {
    color: #648071 !important;
    font-size: 16px;
    opacity: 1 !important;
}

/* Section headings */
.section-heading {
    color: #174D35 !important;
    font-size: 25px;
    font-weight: 700;
    opacity: 1 !important;
}

/* Metric cards */
.metric-card {
    background: #FFFFFF !important;
    border: 1px solid #DCE9DF;
    border-radius: 15px;
    padding: 20px;
    min-height: 135px;
    box-shadow: 0 3px 12px rgba(20, 65, 40, 0.06);
}

.metric-label {
    color: #526F5D !important;
    font-size: 14px;
    font-weight: 600;
    opacity: 1 !important;
}

.metric-value {
    color: #174D35 !important;
    font-size: 29px;
    font-weight: 800;
    margin-top: 10px;
    opacity: 1 !important;
}

/* CO2 card */
.co2-card {
    background: #E7F5EA !important;
    border: 2px solid #269653;
    border-radius: 18px;
    padding: 25px;
    margin-top: 15px;
}

.co2-value {
    color: #168344 !important;
    font-size: 38px;
    font-weight: 800;
    opacity: 1 !important;
}

/* Streamlit metric widgets */
[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    border: 1px solid #DCE9DF;
    border-radius: 12px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #526F5D !important;
    opacity: 1 !important;
}

[data-testid="stMetricValue"] {
    color: #174D35 !important;
    opacity: 1 !important;
}

/* Data tables */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    opacity: 1 !important;
}

/* -----------------------------------------------
   LIGHT AI ENERGY ALERT BOXES
   ----------------------------------------------- */

.eco-alert {
    background-color: #FFF8E8 !important;
    border: 1px solid #E8C878 !important;
    border-left: 6px solid #E3A72F !important;
    border-radius: 12px !important;
    padding: 16px 20px !important;
    margin: 12px 0 !important;
    box-shadow: 0 2px 8px rgba(80, 60, 20, 0.05) !important;
}

.eco-alert-title {
    color: #79500B !important;
    font-size: 16px !important;
    font-weight: 750 !important;
    margin-bottom: 6px !important;
}

.eco-alert-message {
    color: #493B24 !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}

.eco-alert-time {
    color: #806C4B !important;
    font-size: 13px !important;
    margin-top: 8px !important;
}

/* Light green success box */
.eco-success {
    background-color: #EAF7ED !important;
    border: 1px solid #A5D5AF !important;
    border-left: 6px solid #39A45B !important;
    border-radius: 12px !important;
    padding: 16px 20px !important;
    margin: 12px 0 !important;
    color: #205C32 !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

/* Light blue information box */
.eco-info {
    background-color: #EDF6FC !important;
    border: 1px solid #B5D4E9 !important;
    border-left: 6px solid #5598C7 !important;
    border-radius: 12px !important;
    padding: 16px 20px !important;
    margin: 12px 0 !important;
    color: #244D69 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* Horizontal divider */
[data-testid="stMain"] hr {
    border-color: #DCE9DF !important;
}

/* Buttons */
[data-testid="stMain"] button {
    opacity: 1 !important;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:

    st.markdown("# 🌿 EcoVerse")

    st.caption("CAMPUS ENERGY INTELLIGENCE")

    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Overview",
            "🏫 Classroom Monitoring",
            "📊 Energy Analytics",
            "🚨 AI Energy Alerts",
            "🌍 Environmental Impact"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    st.markdown("🌱 **Smart Campus.**")
    st.markdown("⚡ **Smart Energy.**")
    st.markdown("🌍 **Sustainable Future.**")


# --------------------------------------------------
# LOAD AND PROCESS DATA
# --------------------------------------------------

file_path = Path(__file__).parent / "data" / "classroom_data.csv"

try:

    data = load_classroom_data(file_path)
    data = clean_classroom_data(data)
    data = calculate_energy(data)

    if data.empty:
        st.warning("No classroom data available.")
        st.stop()

    data = detect_energy_wastage(data)

    latest_data = (
        data.sort_values("timestamp")
        .groupby("classroom")
        .tail(1)
    )

    total_classrooms = data["classroom"].nunique()
    total_occupancy = latest_data["occupancy"].sum()
    total_energy = data["energy_kwh"].sum()

    CO2_FACTOR = 0.716
    estimated_co2 = total_energy * CO2_FACTOR

    summary = get_wastage_summary(data)
    alerts = generate_alerts(data)


    # --------------------------------------------------
    # OVERVIEW PAGE
    # --------------------------------------------------

    if page == "🏠 Overview":

        st.markdown(
            '<div class="main-title">🌿 EcoVerse Dashboard</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="subtitle">Campus Energy Intelligence System | Smart monitoring for a greener campus</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown(
            '<div class="section-heading">🏫 Campus Overview</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        metrics = [
            (col1, "🏫 Classrooms Monitored", total_classrooms),
            (col2, "👥 Current Occupancy", int(total_occupancy)),
            (col3, "⚡ Total Energy", f"{total_energy:.2f} kWh"),
            (col4, "🚨 Wastage Alerts", summary["total_alerts"])
        ]

        for col, label, value in metrics:

            with col:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">{value}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown("---")

        st.markdown(
            '<div class="section-heading">🌍 Environmental Impact</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="co2-card">
                <div style="font-size:20px;font-weight:700;color:#205D38;">
                    🌿 Estimated CO₂ Emissions
                </div>
                <div class="co2-value">
                    {estimated_co2:.2f} kg CO₂
                </div>
                <div style="color:#648071;font-size:14px;">
                    Estimated campus carbon emissions
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown("### ⚡ Energy Wastage Summary")

        st.metric(
            "Estimated Wasted Energy",
            f"{summary['wasted_energy_kwh']:.2f} kWh"
        )

        st.markdown("### 📌 Campus Snapshot")

        st.dataframe(
            latest_data[
                ["classroom", "occupancy", "power_watts"]
            ].rename(columns={
                "classroom": "Classroom",
                "occupancy": "Students Present",
                "power_watts": "Power Consumption (W)"
            }),
            use_container_width=True,
            hide_index=True
        )


    # --------------------------------------------------
    # CLASSROOM MONITORING PAGE
    # --------------------------------------------------

    elif page == "🏫 Classroom Monitoring":

        st.markdown("## 🏫 Classroom Monitoring")

        st.write(
            "Monitor occupancy, fans, lights and classroom activity."
        )

        st.dataframe(
            latest_data[
                [
                    "classroom",
                    "occupancy",
                    "active_fans",
                    "active_lights",
                    "power_watts"
                ]
            ].rename(columns={
                "classroom": "Classroom",
                "occupancy": "Students Present",
                "active_fans": "Active Fans",
                "active_lights": "Active Lights",
                "power_watts": "Power Consumption (W)"
            }),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.metric(
            "Total Current Occupancy",
            int(total_occupancy)
        )

        st.metric(
            "Classrooms Monitored",
            total_classrooms
        )


    # --------------------------------------------------
    # ENERGY ANALYTICS PAGE
    # --------------------------------------------------

    elif page == "📊 Energy Analytics":

        st.markdown("## 📊 Energy Analytics")

        st.write(
            "Explore electricity consumption and occupancy patterns."
        )

        show_energy_chart(data)

        st.markdown("---")

        show_energy_trend(data)

        st.markdown("---")

        show_occupancy_chart(data)


    # --------------------------------------------------
    # AI ENERGY ALERTS PAGE
    # --------------------------------------------------

    elif page == "🚨 AI Energy Alerts":

        st.markdown("## 🚨 AI Energy Wastage Alerts")

        st.write(
            "Identify classrooms where electricity may be wasted."
        )

        if alerts:

            for alert in alerts:

                st.markdown(
                    f"""
                    <div class="eco-alert">
                        <div class="eco-alert-title">
                            ⚠️ Energy Wastage Alert
                        </div>
                        <div class="eco-alert-message">
                            {alert['message']}
                        </div>
                        <div class="eco-alert-time">
                            🕒 {alert['timestamp']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.markdown(
                """
                <div class="eco-success">
                    🌱 No energy wastage detected!
                    All monitored classrooms are operating normally.
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

        st.markdown("### ⚡ Wastage Summary")

        st.metric(
            "Estimated Wasted Energy",
            f"{summary['wasted_energy_kwh']:.2f} kWh"
        )

        st.metric(
            "Total Wastage Alerts",
            summary["total_alerts"]
        )


    # --------------------------------------------------
    # ENVIRONMENTAL IMPACT PAGE
    # --------------------------------------------------

    elif page == "🌍 Environmental Impact":

        st.markdown("## 🌍 Environmental Impact")

        st.write(
            "Understand the estimated carbon impact of campus electricity use."
        )

        st.markdown(
            f"""
            <div class="co2-card">
                <div style="font-size:21px;font-weight:700;color:#205D38;">
                    🌿 Estimated Campus CO₂ Emissions
                </div>
                <div class="co2-value">
                    {estimated_co2:.2f} kg CO₂
                </div>
                <div style="color:#648071;font-size:14px;">
                    Calculated from estimated electricity consumption
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="eco-info">
                ℹ️ Emission estimate uses an assumed factor of
                0.716 kg CO₂ per kWh. The factor should be verified
                against an appropriate electricity-grid source.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.metric(
            "Total Energy Consumption",
            f"{total_energy:.2f} kWh"
        )

        st.metric(
            "Estimated Wasted Energy",
            f"{summary['wasted_energy_kwh']:.2f} kWh"
        )

        st.markdown(
            """
            <div class="eco-success">
                🌱 Reducing unnecessary electricity consumption
                can help lower campus carbon emissions.
            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    st.markdown("---")

    st.caption(
        "🌿 EcoVerse | Campus Energy Intelligence System"
    )


except FileNotFoundError:

    st.error(
        "Classroom CSV file not found. "
        "Please check the data folder."
    )

except Exception as e:

    st.error(f"Something went wrong: {e}")
