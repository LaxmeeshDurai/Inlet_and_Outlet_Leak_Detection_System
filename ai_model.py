def detect_leak(data):

    boost = data["Boost"]
    turbo = data["TurboSpeed"]
    exhaust = data["ExhaustPressure"]

    if boost < 1.6 and turbo > 95000:
        return True, "Charge Air Pipe", 88

    if exhaust < 2.1:
        return True, "Exhaust System", 82

    return False, "Normal", 95 
