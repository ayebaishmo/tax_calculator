def calculate_tax(earning):
    if earning == 0:
        return("No tax")
    
    elif earning < 0:
        raise ValueError("Earnings cannot be negative")