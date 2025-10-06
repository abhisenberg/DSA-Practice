from math import ceil

def minSpeedOnTime(dist, hour) -> int:

        # If there are more stations than there are hours allowed, return -1
        if len(dist) > ceil(hour):
            return -1
        
        # Checkking if destination is reachable with a given speed
        def canReach(speed):
            totalHours = 0
            for d in dist:
                print(f"Total hours: {totalHours}")
                totalHours = ceil(totalHours)
                totalHours += d/speed
            return totalHours <= hour

        # We will use binary search on solution space for this problem
        l, r = 1, max(dist)
        while (l <= r):
            mid = (l + r) // 2
            if canReach(mid):
                r = l-1
            else:
                l = r+1
        
        return l

dist = [1,3,2]
hour = 2.7
print(minSpeedOnTime(dist, hour))