import random

def cluster_complaints(complaints):
    """Simulates clustering of complaints into zones."""
    clusters = ["North Zone", "South Zone", "East Zone", "West Zone", "Central Zone"]
    return [random.choice(clusters) for _ in complaints]
