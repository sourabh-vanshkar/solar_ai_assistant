def generate_report(data: dict) -> str:

    report = f"""
    🔍 **Solar Rooftop Feasibility Report**

    ✅ **Rooftop Analysis**
    - Total rooftop area: {data['total_area']} m²
    - Usable rooftop area for solar panels: {data['usable_area']} m²
    - Estimated usable surface: {data['percent_usable']}%

    ⚡ **Energy Output Estimate**
    - Daily energy generation potential: {data['daily_kwh']} kWh
    - Annual energy generation: {data['yearly_kwh']} kWh

    💸 **Installation & Cost**
    - Estimated installation cost: ₹{data['installation_cost']}
    - Approximate yearly savings on electricity: ₹{data['yearly_savings']}

    📈 **ROI and Payback**
    - ROI: {data['roi_percent']}%
    - Payback Period: {data['payback_years']} years

    📝 **Recommendation**
    Based on the current rooftop conditions and solar exposure, this property is a suitable candidate for solar panel installation. 
    Installing solar panels can lead to significant long-term savings and help reduce your carbon footprint.

    For a personalized quotation or subsidy assistance, please consult a certified solar installation provider.
    """

    return report.strip()
