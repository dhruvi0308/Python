def seconds_since_midnight(hour, minute, second):
    return hour * 3600 + minute * 60 + second

hours = int(input("Enter the hour(0-23): "))
minutes = int(input("Enter the minute(0-59): "))
seconds = int(input("Enter the second(0-59): "))

total_seconds = seconds_since_midnight(hours, minutes, seconds)
print(total_seconds)
