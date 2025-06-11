def estimate_solar_output(usable_area_m2, panel_efficiency=0.18, sun_hours_per_day=5.5):
    
    # 1 m² of solar panel = 1,000 W * efficiency
    watts_per_m2 = 1000 * panel_efficiency
    daily_kwh = (usable_area_m2 * watts_per_m2 * sun_hours_per_day) / 1000
    yearly_kwh = daily_kwh * 365

    return {
        "daily_kwh": round(daily_kwh, 2),
        "yearly_kwh": round(yearly_kwh, 2)
    }


def estimate_costs(usable_area_m2, cost_per_watt=55, panel_efficiency=0.18):
    
    total_watt = usable_area_m2 * 1000 * panel_efficiency
    cost = total_watt * cost_per_watt
    return round(cost, 2)


def estimate_roi(yearly_savings, installation_cost):
    
    if yearly_savings == 0:
        return {"roi_percent": 0, "payback_years": "N/A"}

    roi_percent = (yearly_savings / installation_cost) * 100
    payback_years = installation_cost / yearly_savings
    return {
        "roi_percent": round(roi_percent, 2),
        "payback_years": round(payback_years, 1)
    }
