import datetime

# Get current date and time
today_date = datetime.datetime.today()

print("Current Date and Time:", today_date)

# Extract date components
print("Year:", today_date.year)
print("Month:", today_date.month)
print("Day:", today_date.day)

# Extract time components
print("Hour:", today_date.hour)
print("Minute:", today_date.minute)
print("Second:", today_date.second)

# Create a specific date
some_date = datetime.datetime(2019, 5, 27, 9, 5, 25)

print("Specific Date:", some_date)
print("Date Only:", some_date.date())
print("Time Only:", some_date.time())

# Date calculations using timedelta
print("After 90 Days:", some_date + datetime.timedelta(days=90))
print("After 3 Weeks:", some_date + datetime.timedelta(weeks=3))
print("After 48 Hours:", some_date + datetime.timedelta(hours=48))