
import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True

    def set_closed(self, closed):
        self.closed = closed
    
    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"

class Intervals:
    def __init__(self, intervals):
        self.intervals = intervals

    def merge_intervals(self):
        """
        Returns a list of all the intervals in the list of intervals.

        Parameters:
            self (object): The object to be represented as a string.

        Returns:
            list: A list of all the intervals in the list of intervals.
        """
        if not self.intervals:
            return []
        intervals = self.intervals
        res = []
        res.append([intervals[0][0], intervals[0][1]])

        for i in range(1, len(intervals)):
            last_added = res[len(res)-1]
            curr_start  = intervals[i][0]
            curr_end    = intervals[i][1]

            prev_end = last_added[1]

            if curr_start <= prev_end:
                res[-1][1] = max(curr_end, prev_end)
            else:
                res.append([curr_start, curr_end])

        return res

    def intervals_intersect(self, intervals_a, intervals_b):
        intersections = []
        i = j = 0

        while i < len(intervals_a) and j < len(intervals_b):
            start = max(intervals_a[i][0], intervals_b[j][0])
            end = min(intervals_a[i][1], intervals_b[j][1])

            if start <= end:
                intersections.append([start, end])
            if intervals_a[i][1] < intervals_b[j][1]:
                i += 1
            else:
                j += 1
        
        return intersections

    def emp_free_time(self, schedules):
        """
        Returns a list of all the free time intervals in the list of schedules.

        Parameters:
            self (object): The object to be represented as a string.

        Returns:
            list: A list of all the free time intervals in the list of schedules.
        """
        heap = []

        for i in range(len(schedules)):
            heap.append((schedules[i][0].start, i , 0))
        
        heapq.heapify(heap)

        res = []

        previous = schedules[heap[0][1]][heap[0][2]].start

        while heap:
            _, i, j = heapq.heappop(heap)

            interval = schedules[i][j]

            if interval.start > previous:
                res.append(Interval(previous, interval.start))
            
            previous = max(previous, interval.end)

            if j + 1 < len(schedules[i]):
                heapq.heappush(heap, (schedules[i][j+1].start, i, j+1))
        return res


def display(vec):
    string = "["
    if vec:
        for i in range(len(vec)):X
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "
    string += "]"
    return string

intr = Intervals( [[3, 7], [6, 8], [10, 12], [11, 15]])
print(intr.merge_intervals())

print(intr.intervals_intersect( [[3, 6], [8, 16], [17, 25]], [[2, 3], [10, 15], [18, 23]]))

print(display(intr.emp_free_time(         [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]])))