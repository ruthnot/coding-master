class Solution:

    def searchBigSortedArray(self, reader, target):
        start, end = 0, 1
        while reader.get(end) < target:
            end *= 2

        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
