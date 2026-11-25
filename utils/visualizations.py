
import streamlit as st
import plotly.express as px


def show_energy_chart(data):
    """Display energy consumption by classroom."""

    energy_data = (
        data.groupby("classroom")["energy_kwh"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        energy_data,
        x="classroom",
        y="energy_kwh",
        color="classroom",
        title="Energy Consumption by Classroom",
        labels={
            "classroom": "Classroom",
            "energy_kwh": "Energy Consumption (kWh)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)


def show_energy_trend(data):
    """Display energy consumption over time."""

    trend_data = data.copy()

    trend_data = trend_data.sort_values("timestamp")

    fig = px.line(
        trend_data,
        x="timestamp",
        y="power_watts",
        color="classroom",
        markers=True,
        title="Classroom Electricity Usage Over Time",
        labels={
            "timestamp": "Time",
            "power_watts": "Power Consumption (Watts)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)


def show_occupancy_chart(data):
    """Display classroom occupancy."""

    occupancy_data = (
        data.groupby("classroom")["occupancy"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        occupancy_data,
        x="classroom",
        y="occupancy",
        color="classroom",
        title="Average Classroom Occupancy",
        labels={
            "classroom": "Classroom",
            "occupancy": "Number of Students"
        }
    )

    st.plotly_chart(fig, use_container_width=True)
