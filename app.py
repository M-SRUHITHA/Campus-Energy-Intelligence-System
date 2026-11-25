
import streamlit as st

st.set_page_config(
    page_title="EcoVerse",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoVerse")
st.subheader("Campus Energy Intelligence System")

st.write(
    "Monitor classroom occupancy, electricity consumption, "
    "energy wastage and estimated carbon emissions."
)

st.info("Welcome to the EcoVerse prototype!")

st.markdown("---")

st.header("Campus Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Classrooms Monitored", "5")

with col2:
    st.metric("Total Occupancy", "120")

with col3:
    st.metric("Energy Wastage Alerts", "2")

st.success("EcoVerse dashboard is running!")
