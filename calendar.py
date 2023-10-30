import calendar

# Create a TextCalendar for the year 2024
cal = calendar.TextCalendar(calendar.SUNDAY)

# Loop through and display each month for the year 2024
for month in range(1, 13):
    # Get the month's name and year
    month_name = cal.formatmonthname(2024, month, 0, 0)
    print(month_name)
    
    # Get the month's calendar
    month_calendar = cal.formatmonth(2024, month)
    print(month_calendar)
