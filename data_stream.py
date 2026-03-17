import random
import time

def generate_data():
    return {
        "MAF": random.uniform(95,120),
        "Boost": random.uniform(1.4,2.2),
        "MAP": random.uniform(1.2,1.8),
        "TurboSpeed": random.uniform(85000,100000),
        "ExhaustPressure": random.uniform(2.0,2.6),
        "RPM": random.uniform(1400,1600)
    }
