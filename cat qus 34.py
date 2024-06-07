from datetime import datetime

# Function to calculate difference between two dates
def date_difference(date1, date2):
    # Convert string dates to datetime objects
    date_format = "%Y-%m-%d"  # Define the format of the input dates
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    # Calculate the difference
    delta = d2 - d1
    
    # Get the difference in days
    difference_in_days = delta.days
    
    return difference_in_days

# Example usage
date1 = "2023-06-01"
date2 = "2024-06-01"

difference = date_difference(date1, date2)
print(f"The difference between {date1} and {date2} is {difference} days.")
