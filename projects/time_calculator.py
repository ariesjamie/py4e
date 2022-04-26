dict_days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# calculate and print results
def time_calculator(hrs, mins, midday, n_days, days_of_the_week = None):
    
    #calculate final time
    if hrs < 12:
        if hrs == 0:
            hrs = 12
        time_result = str(hrs) + ":" + str(mins) + " AM"
    elif hrs == 12: 
        if midday == "AM":
            midday = "PM" 
            time_result = str(hrs) + ":" + str(mins) + str(" " + midday)
        elif midday == "PM":
            midday = "AM"
            hrs = hrs - 12
            time_result = str(hrs) + ":" + str(mins) + str(" " + midday)
    elif hrs > 12:
        hrs = hrs - 12
        time_result = str(hrs) + ":" + str(mins) + " PM"

    #calculate next day or n days later
    if n_days == 0:
        display_days_later = ""
    elif n_days == 1:
        display_days_later = " (next day)"
    else:   
        display_days_later = f" ({n_days} days later)"

    #calculate the display week day and final result
    if days_of_the_week:
        days_of_the_week = days_of_the_week.title()
        index = (dict_days_of_the_week.index(days_of_the_week) + n_days) % 7
        display_days_of_the_week = dict_days_of_the_week[index]
        result = time_result + "," + " " + display_days_of_the_week + display_days_later
    else:
        result = time_result + display_days_later
    
    return result

def add_time(start, duration, days_of_the_week = None):
    
    #parsing time
    start = start.split(":")
    duration = duration.split(":")
    hrs_start = int(start[0])
    mins_start = int(start[1].split(" ")[0])
    midday = start[1].split(" ")[1]
    hrs_duration = int(duration[0])
    mins_duration = int(duration[1])
    
    #convert 12-hour clock format to 24-hour clock format, processing time_result
    if midday == "PM":
        hrs_start = hrs_start + 12
    elif midday == "AM" and hrs_start == 12:
        hrs_start = 0
    
    #calculate the sum of hrs and mins
    hrs_new = (hrs_start + hrs_duration) + (mins_start + mins_duration) // 60
    mins = f"{((mins_start + mins_duration) % 60):02d}"
    hrs = hrs_new % 24
    n_days = hrs_new // 24
    
    return time_calculator(hrs, mins, midday, n_days, days_of_the_week)
  
  print(add_time("11:30 AM", "2:32", "mOnday"))
