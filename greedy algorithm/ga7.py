"""
Minimum Platforms
"""

arrival = [900, 940, 950, 1100, 1500, 1800]
deparchare = [910, 1200, 1120, 1130, 1900, 2000]

time = list(zip(arrival, deparchare))
time.sort(key= lambda x: x[0])
print(time)
platform = 0
count = 0
last_time = 0

for s, e in time:
    if s >= last_time:
        platform += 1
        last_time = e
print(platform)