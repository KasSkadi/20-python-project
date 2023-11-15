# Write your code here
import time


def set_alarm(alarm_time):
    # Split the alarm_time string into hours, minutes, and seconds
    hh, mm, ss = map(int, alarm_time.split(":"))

    # Get current time to calculate the seconds until the alarm
    current_time = time.localtime()
    current_seconds = (
        current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
    )

    # Calculate the number of seconds for the set alarm
    alarm_seconds = hh * 3600 + mm * 60 + ss

    # Calculate the difference in seconds
    difference = alarm_seconds - current_seconds

    # If the difference is negative, then the alarm is set for the next day
    if difference < 0:
        difference += 24 * 3600  # add one day in seconds

    # Sleep until the alarm time
    time.sleep(difference)

    print("Alarm ringing!")


if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (HH:MM:SS): ")
    set_alarm(alarm_time)
