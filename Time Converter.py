#To convert 12 hour time into 24 hour time
#12:00 AM

def time_checker(x):
    if len(x) < 2:
        return "0"+x
    return x

hour = int(input("Type the hour you are in"))
minute = int(input("Type the minute you are in"))

meridian = input("Please specify if your time is in AM or PM")

stringed_hour = time_checker(str(hour))
stringed_minute = time_checker(str(minute))

if meridian == "AM":
    print(stringed_hour+":"+stringed_minute)

if meridian == "PM":
    print(str(hour + 12)+":"+stringed_minute)
