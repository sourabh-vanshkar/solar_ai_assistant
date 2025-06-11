import numpy as np
from PIL import Image
import random
import io

def analyze_rooftop(image: Image.Image):

    # Simulated values for now (to be replaced with ML model later)
    width, height = image.size
    total_area = (width * height) / 1000  # Simulated m^2 from pixel count
    usable_area = total_area * random.uniform(0.4, 0.75)  # Assume 40-75% is usable

    result = {
        "total_area_m2": round(total_area, 2),
        "usable_area_m2": round(usable_area, 2),
        "percent_usable": round((usable_area / total_area) * 100, 2)
    }

    return result
