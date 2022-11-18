# import time
#  n=int(input("enter the seconds"))
#  for i in range(n,0,-1):
#      print(i)
#      time.sleep(1)

import time

def convert_count(timer):
    minute=0
    seconds=0
    while timer >= 60:
        minute += 1
        timer -= 60
    seconds = timer
    print(minute , ":" , seconds)
    while minute > 0:
        minute = count(minute,seconds)
        seconds = 59
    for i in range(seconds ,0,-1):
        print(minute,":",i)
        time.sleep(1)
    print("Time up!")

def count(minute,seconds):
    for i in range(seconds,0,-1):
        print(minute,":",i)
        time.sleep(1)
    return minute-1
timer=int(input("enter the time in seconds:"))
convert_count(timer)