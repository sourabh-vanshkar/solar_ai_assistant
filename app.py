import streamlit as st
from PIL import Image
import io

from analysis import analyze_rooftop
from cost_estimator import estimate_solar_output, estimate_costs, estimate_roi
from llm_report import generate_report

st.set_page_config(page_title="Solar Industry AI Assistant", layout="centered")

st.title("🔆 Solar Industry AI Assistant")
st.markdown("Upload your rooftop satellite image to get a complete solar feasibility report.")

# Upload Image
uploaded_file = st.file_uploader("Upload Rooftop Image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

    if st.button("🔍 Analyze Rooftop"):
        with st.spinner("Analyzing rooftop image..."):
            # Step 1: Analyze rooftop area
            area_result = analyze_rooftop(image)
            total_area = area_result["total_area_m2"]
            usable_area = area_result["usable_area_m2"]
            percent_usable = area_result["percent_usable"]

            # Step 2: Estimate output
            output = estimate_solar_output(usable_area)
            daily_kwh = output["daily_kwh"]
            yearly_kwh = output["yearly_kwh"]

            # Step 3: Estimate cost
            installation_cost = estimate_costs(usable_area)

            # Step 4: Estimate savings and ROI
            avg_rate_per_kwh = 7  # INR/kWh (adjustable)
            yearly_savings = yearly_kwh * avg_rate_per_kwh
            roi_data = estimate_roi(yearly_savings, installation_cost)

            # Step 5: Generate report
            result_data = {
                "total_area": total_area,
                "usable_area": usable_area,
                "percent_usable": percent_usable,
                "daily_kwh": daily_kwh,
                "yearly_kwh": yearly_kwh,
                "installation_cost": installation_cost,
                "yearly_savings": round(yearly_savings, 2),
                "roi_percent": roi_data["roi_percent"],
                "payback_years": roi_data["payback_years"]
            }

            report = generate_report(result_data)

        # Display output
        st.success("Analysis complete!")
        st.markdown(report, unsafe_allow_html=True)

        # Download button
        buffer = io.BytesIO()
        buffer.write(report.encode())
        st.download_button(
            label="📄 Download Report",
            data=buffer.getvalue(),
            file_name="solar_report.txt",
            mime="text/plain"
        )
