from datetime import datetime
from collections import Counter

def find_peak_usage(logs):
    """
    Input: logs = list of ISO-formatted timestamp strings
           e.g. "2026-08-04T13:21:18"
    Output: integer hour 0-23 with the most logins.
            If there is a tie, return the earliest hour.
    Only uses built-in modules.
    """
    hours = []
    
    # Step 1: Extract the hour from each timestamp
    for ts in logs:
        dt = datetime.fromisoformat(ts)  # convert string to datetime object
        hours.append(dt.hour)  # get hour 0-23
    
    # Step 2: Count how many times each hour appears
    hour_counts = Counter(hours)
    
    # Step 3: Find the highest count
    max_count = max(hour_counts.values())
    
    # Step 4: Get all hours that have that max count
    peak_hours = [h for h, c in hour_counts.items() if c == max_count]
    
    # Step 5: Return the earliest hour if there’s a tie
    return min(peak_hours)

# Test it
sample_logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:00",
    "2026-08-04T09:10:05",
    "2026-08-04T13:59:59",
    "2026-08-04T09:30:12",
    "2026-08-04T09:55:00"
]

peak = find_peak_usage(sample_logs)
print(f"Peak usage hour: {peak}")