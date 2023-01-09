from typing import (
    List,
)
import math

class Solution:
    """
    @param points: a array of points
    @param angle: a integer
    @return: return a max points with a angle beam
    """

    def angle_beam(self, points: List[List[int]], angle: int) -> int:
        # write your code here
        angle_list = self.find_angle(points)
        max_count = 0
        l, r = 0, 0
        while r < len(angle_list):
            while r < len(angle_list) and angle_list[r] <= angle_list[l] + angle:
                r += 1
            max_count = max(max_count, r - l)
            l += 1
        return max_count

    def find_angle(self, points):
        angle_list = []
        for p_x, p_y in points:
            angle = math.degrees(math.atan2(p_x, p_y))
            angle_list.append(angle)
            angle_list.append(angle + 360.0)
        return sorted(angle_list)


class Solution:  #Leet code 1610 solution
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        self.origin_count = 0
        angle_list = self.find_angle(points, location)
        max_count = 0
        l, r = 0, 0

        while r < len(angle_list):
            while r < len(angle_list) and angle_list[r] <= angle_list[l] + angle:
                r += 1
            max_count = max(max_count, r - l)
            l += 1
        return max_count + self.origin_count

    def find_angle(self, points, location):
        angle_list = []
        o_x, o_y = location[0], location[1]
        for point in points:
            p_x, p_y = point[0], point[1]
            if o_x == p_x and o_y == p_y:
                self.origin_count += 1
                continue

            angle = math.degrees(math.atan2((p_x - o_x), (p_y - o_y)))
            angle_list.append(angle)
            angle_list.append(angle + 360.0)

        return sorted(angle_list)



