import re
from utils.location_utils import extract_location

def classify_complaint(text):
    text = text.lower()

    # Urgency detection (keyword-based)
    critical_keywords = ["fire", "spark", "blast", "wire down", "shock", "explosion", "burn", "blackout", "smoke", "live wire"]
    moderate_keywords = ["no power", "fluctuation", "flickering", "low voltage", "high voltage"]
    
    urgency = "Low"
    for word in critical_keywords:
        if word in text:
            urgency = "Critical"
            break
    if urgency != "Critical":
        for word in moderate_keywords:
            if word in text:
                urgency = "Moderate"
                break

    # Issue type classification
    if "bill" in text or "payment" in text:
        issue_type = "Billing Issue"
    elif "voltage" in text or "fluctuat" in text:
        issue_type = "Voltage Issue"
    elif "pole" in text or "wire" in text or "transformer" in text:
        issue_type = "Hardware Fault"
    elif "outage" in text or "no electricity" in text or "blackout" in text:
        issue_type = "Power Outage"
    else:
        issue_type = "General Complaint"

    # Geo-detection (basic)
    location = extract_location(text)

    return {
        "urgency": urgency,
        "issue_type": issue_type,
        "location": location
    }
