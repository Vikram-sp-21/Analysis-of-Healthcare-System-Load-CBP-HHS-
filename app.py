import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Healthcare Capacity Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare Capacity Monitoring Dashboard")
st.markdown("Analysis of Healthcare System Load (CBP & HHS)")

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Healthcare_Pressure_Analysis.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------
st.sidebar.header("Dashboard Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Date"].max()
)

granularity = st.sidebar.selectbox(
    "Time Granularity",
    ["Daily", "Weekly", "Monthly"]
)

metric = st.sidebar.selectbox(
    "Metric",
    [
        "Total System Load",
        "Children in CBP custody",
        "Children in HHS Care",
        "Net Daily Intake"
    ]
)

# -------------------------------------------------------
# Filter Data
# -------------------------------------------------------
filtered = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
].copy()

# -------------------------------------------------------
# Resampling
# -------------------------------------------------------
if granularity == "Weekly":
    filtered = (
        filtered.set_index("Date")
        .resample("W")
        .mean(numeric_only=True)
        .reset_index()
    )

elif granularity == "Monthly":
    filtered = (
        filtered.set_index("Date")
        .resample("M")
        .mean(numeric_only=True)
        .reset_index()
    )

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------
st.subheader("📌 KPI Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Average System Load",
    f"{filtered['Total System Load'].mean():,.0f}"
)

c2.metric(
    "Maximum Load",
    f"{filtered['Total System Load'].max():,.0f}"
)

c3.metric(
    "Average Net Intake",
    f"{filtered['Net Daily Intake'].mean():,.0f}"
)

c4.metric(
    "Maximum Net Intake",
    f"{filtered['Net Daily Intake'].max():,.0f}"
)

st.divider()

# -------------------------------------------------------
# System Load Trend
# -------------------------------------------------------
st.subheader("📈 System Load Overview")

fig = px.line(
    filtered,
    x="Date",
    y=metric,
    markers=True,
    title=metric
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------
# CBP vs HHS Comparison
# -------------------------------------------------------
st.subheader("⚖️ CBP vs HHS Load Comparison")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=filtered["Date"],
        y=filtered["Children in CBP custody"],
        name="CBP Custody"
    )
)

fig2.add_trace(
    go.Scatter(
        x=filtered["Date"],
        y=filtered["Children in HHS Care"],
        name="HHS Care"
    )
)

fig2.update_layout(
    xaxis_title="Date",
    yaxis_title="Children",
    hovermode="x unified"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------------
# Net Intake Trend
# -------------------------------------------------------
st.subheader("📊 Net Daily Intake")

fig3 = px.bar(
    filtered,
    x="Date",
    y="Net Daily Intake",
    color="Net Daily Intake"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------------
# Rolling Average
# -------------------------------------------------------
if "7-Day Rolling Avg" in filtered.columns:

    st.subheader("📉 Rolling Average")

    fig4 = go.Figure()

    fig4.add_trace(
        go.Scatter(
            x=filtered["Date"],
            y=filtered["Total System Load"],
            name="Daily Load"
        )
    )

    fig4.add_trace(
        go.Scatter(
            x=filtered["Date"],
            y=filtered["7-Day Rolling Avg"],
            name="7-Day Average"
        )
    )

    if "14-Day Rolling Avg" in filtered.columns:

        fig4.add_trace(
            go.Scatter(
                x=filtered["Date"],
                y=filtered["14-Day Rolling Avg"],
                name="14-Day Average"
            )
        )

    st.plotly_chart(fig4, use_container_width=True)

# -------------------------------------------------------
# High Load Periods
# -------------------------------------------------------
if "Prolonged Strain" in filtered.columns:

    st.subheader("🚨 Prolonged Strain Days")

    strain = filtered[filtered["Prolonged Strain"] == True]

    st.write(f"Total Strain Days: **{len(strain)}**")

    if len(strain) > 0:

        fig5 = px.scatter(
            strain,
            x="Date",
            y="Total System Load",
            color="Total System Load"
        )

        st.plotly_chart(fig5, use_container_width=True)

# -------------------------------------------------------
# Summary Statistics
# -------------------------------------------------------
st.subheader("📋 Summary Statistics")

st.dataframe(filtered.describe())

# -------------------------------------------------------
# Data Table
# -------------------------------------------------------
st.subheader("📄 Dataset")

st.dataframe(filtered)

# -------------------------------------------------------
# Download Button
# -------------------------------------------------------
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Filtered Dataset",
    csv,
    file_name="Filtered_Healthcare_Data.csv",
    mime="text/csv"
)
