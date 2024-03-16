import datetime
#1
# before = datetime.datetime.now().date()
# after = datetime.timedelta(days=5)

# new = before - after

# print(f"Current date: {before} \nFive days ago: {new}")

#2
# before = datetime.datetime.now().date()
# delta = datetime.timedelta(days=1)

# yesterday = before - delta
# tomorrow = before + delta

# print(f"Yesterday : {yesterday} \nToday : {before} n\Tomorrow : {tomorrow}")

# #3
# time = datetime.datetime.now()
# after_time = time.replace(microsecond = 0)
# print("Time without microsecond:",after_time)

# #4
date_1 = datetime.datetime(2024,2,17,12,1,0)
date_2 = datetime.datetime(2024,2,17,12,1,23)
difference = date_2 - date_1
print(difference)