#  Project 5: Count Down Timer In Python
#  Description: This program will create a count down timer in Python.
#  minute and second will be taken as input from the user and the timer will start.
# Made by: Erum Azeemi Qaimkhani

import time

def count_down(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    
    while total_seconds > 0:
        min, sec = divmod(total_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(min, sec)
        print(time_format, end='\r')
        time.sleep(1)
        total_seconds -= 1
    
    print("00:00 \nTime's up!")

def main():
    while True:
        try:
            minutes = int(input("Enter the minutes: "))
            seconds = int(input("Enter the seconds: "))
            if minutes < 0 or seconds < 0 or seconds >= 60:
                print("Invalid input. Please enter non-negative minutes and seconds (seconds < 60).")
                continue

            count_down(minutes, seconds)

            # Ask user if they want to continue
            user_input = input("Do you want to continue? (y/n): ").lower()
            if user_input != 'y':
                print("Good luck!")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
