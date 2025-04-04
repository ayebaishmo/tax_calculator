def calculate_tax(earning):
    if earning == 0:
        return("No tax")
    
    elif earning < 0:
        raise ValueError("Earnings cannot be negative")
    
    elif earning <= 12000:
        return 0
    
    elif earning <= 36000:
        return (earning - 12000) * 0.2
    
    else:
        return (36000 - 12000) * 0.2 + (earning - 36000) * 0.4