import re

def extract_location(text):
    # Dummy location detection via pincode or area names
    pincodes = {
        "395007": "Adajan",
        "395006": "Citylight",
        "395010": "Katargam",
        "395004": "Udhna",
        "395002": "Varachha"
    }

    for code in pincodes:
        if code in text:
            return pincodes[code]

    area_keywords = {
        "adajan": "Adajan",
        "citylight": "Citylight",
        "udhna": "Udhna",
        "varachha": "Varachha",
        "katargam": "Katargam"
    }

    for key in area_keywords:
        if key in text:
            return area_keywords[key]

    return None
