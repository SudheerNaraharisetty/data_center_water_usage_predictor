import streamlit as st
import xgboost as xgb
import numpy as np

# ✅ Load the trained XGBoost model
model = xgb.XGBRegressor()
model.load_model("xgboost_model.json")  # Ensure this file is in the same directory

# ✅ Web App Title & Description
st.title("💧 AI Data Center Water Consumption Predictor")
st.write(
    """
    This tool estimates **water consumption** (L/kWh) in AI data centers based on energy source distribution. 
    Adjust the sliders to see how **different energy sources** impact water usage.
    """
)

# ✅ User-Friendly Input Labels & Sliders for Percentage Values
st.sidebar.header("🔹 Input Parameters")

offsite_wue = st.sidebar.slider(
    "💧 Percentage of Water Used in Power Generation (%)", 0, 100, 50
) / 100
hydro = st.sidebar.slider(
    "⚡ Electricity from Hydropower (%)", 0, 100, 20
) / 100
nuclear = st.sidebar.slider(
    "⚡ Electricity from Nuclear Power (%)", 0, 100, 30
) / 100
natural_gas = st.sidebar.slider(
    "⚡ Electricity from Natural Gas (%)", 0, 100, 40
) / 100
coal = st.sidebar.slider(
    "⚡ Electricity from Coal (%)", 0, 100, 10
) / 100
zip_code = st.sidebar.number_input(
    "📍 Enter ZIP Code for Regional Analysis (Use Numeric Values)", min_value=10000, max_value=99999, value=90210
)

# ✅ Convert input into a feature array (Ensure all 6 features are included)
input_data = np.array([[offsite_wue, hydro, zip_code, nuclear, natural_gas, coal]])

# ✅ Predict Total Water Usage
predicted_wue = model.predict(input_data)[0]

# ✅ Display Prediction Results
st.subheader("📊 Estimated Water Consumption")
st.metric("💧 Predicted Total Water Usage (L/kWh)", f"{predicted_wue:.4f}")

# ✅ Prescriptive Analytics
st.subheader("💡 Water Reduction Strategy")
wue_reduction = predicted_wue * 0.90  # Reduce by 10%
st.write(
    f"If **water usage in power generation** is reduced by **10%**, the estimated new **total water consumption** will be **{wue_reduction:.4f} L/kWh**."
)

# ✅ Yearly Water Savings Estimation
current_annual_wue = predicted_wue * 8760  # Assuming 8760 hours in a year
new_annual_wue = wue_reduction * 8760
water_savings = current_annual_wue - new_annual_wue

st.subheader("📉 Estimated Annual Water Savings")
st.write(f"💧 **Current Annual Water Usage**: {current_annual_wue:.2f} L")
st.write(
    f"💡 **Projected Annual Water Usage (After Reduction)**: {new_annual_wue:.2f} L"
)
st.success(f"🌱 **Potential Annual Water Savings**: {water_savings:.2f} L")

# ✅ Final Notes
st.info(
    "Use the sliders to simulate how different energy sourcing decisions impact total water consumption. "
    "Try reducing reliance on high-water-consuming energy sources for better sustainability."
)
