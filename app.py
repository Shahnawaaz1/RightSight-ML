import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------- Title ----------------------
st.title("🚖 RideSight ML: Mobility Analytics & Forecasting")
st.write("An integrated platform combining Power BI dashboard & Machine Learning predictions.")

# ---------------------- Tabs ----------------------
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📂 Dataset", "🤖 ML Predictions"])

# ---------------------- Dashboard Tab ----------------------
with tab1:
    st.header("Power BI Dashboard")
    st.write("Below is the analytics dashboard created in Power BI (exported as image).")
    
    # Add your dashboard image file here (export from Power BI)
    st.image("dashboard.png", caption="Ola Booking Dashboard", use_column_width=True)

# ---------------------- Dataset Tab ----------------------
with tab2:
    st.header("Ola Booking Dataset")
    
    # Load dataset
    try:
        data = pd.read_csv("ola_booking_data.csv")  # apna dataset ka naam yaha rakho
        st.write("Sample Data from Dataset:")
        st.dataframe(data.head(10))
    except:
        st.error("Dataset file 'ola_booking_data.csv' not found. Please upload the dataset.")

# ---------------------- ML Predictions Tab ----------------------
with tab3:
    st.header("Machine Learning Predictions")
    st.write("Here we show future demand forecast based on ride booking data.")

    try:
        # Ensure Date column is datetime
        data['Date'] = pd.to_datetime(data['Date'])

        # Group by Date for demand trend
        demand = data.groupby("Date")['Booking_ID'].count()

        # Plot actual demand trend
        st.subheader("Ride Demand Trend")
        plt.figure(figsize=(8,4))
        plt.plot(demand.index, demand.values, label="Actual Rides")
        plt.xlabel("Date")
        plt.ylabel("Number of Rides")
        plt.legend()
        st.pyplot(plt)

        # Simple forecast (moving average as demo)
        st.subheader("Forecast (Next 7 Days - Simple Moving Average)")
        forecast = demand.rolling(window=3).mean().iloc[-7:]
        st.line_chart(forecast)

        st.success("This section can be extended with ML models like Prophet or Random Forest.")

    except:
        st.warning("Dataset not loaded properly. Please check 'Date' and 'Booking_ID' columns.")


