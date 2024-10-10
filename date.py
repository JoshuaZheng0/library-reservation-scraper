from datetime import datetime, timedelta

# Get today's date
now = datetime.now()
future_date = now + timedelta(days=7)
formatted_date = future_date.strftime("%A, %B %d, %Y").replace(" 0", " ")  # Example: "Wednesday, October 16, 2024"
room_number = 7235
time_slots = ["6:00PM", "7:00PM", "8:00PM", "9:00PM"]
time_slot_selectors = [
    f'a.fc-timeline-event[title="{time} {formatted_date} - {room_number} - Available"]' for time in time_slots
]

# Print the results
for selector in time_slot_selectors:
    print(selector)

