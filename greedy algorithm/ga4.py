"""
N meetings in one room
"""
start = [1, 3, 0, 5, 8, 5]
end =   [2, 4, 6, 7, 9, 9]

n = len(start)
meetings = list(zip(start, end))

# Sort meetings by end time
# here data in order so no change happen
meetings.sort(key=lambda x: x[1])

# Initialize
total_meetings = 0
schedule = []
last_end_time = 0

for s, e in meetings:
    if s >= last_end_time:
        schedule.append((s, e))
        total_meetings += 1
        last_end_time = e

print("Scheduled meetings:", schedule)
print("Total meetings:", total_meetings)

# ====with class=========

class Meeting:
    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position


class Solution:
    def maximumMeetings(self, n, start, end):
        meets = [Meeting(start[i], end[i], i + 1) for i in range(n)]
        meets.sort(key=lambda x: (x.end, x.start))
        lastTime = meets[0].end
        count = 1
        for i in range(1, n):
            if meets[i].start > lastTime:
                count += 1
                lastTime = meets[i].end
        return count
"""
Time complexity : O(n)
Space complexity : O(n)
"""