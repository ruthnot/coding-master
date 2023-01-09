class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if not image or not image[0]:
            return 0
        m, n = len(image), len(image[0])
        up = self.findFirst(image, 0, x, self.checkRow)
        down = self.findLast(image, x, m - 1, self.checkRow)
        left = self.findFirst(image, 0, y, self.checkColumn)
        right = self.findLast(image, y, n - 1, self.checkColumn)

        return (down - up + 1) * (right - left + 1)

    def findFirst(self, image, start, end, check_func):
        while start + 1 < end:
            mid = (start + end) // 2
            if check_func(image, mid):
                end = mid
            else:
                start = mid
        if check_func(image, start):
            return start
        return end

    def findLast(self, image, start, end, check_func):
        while start + 1 < end:
            mid = (start + end) // 2
            if check_func(image, mid):
                start = mid
            else:
                end = mid
        if check_func(image, end):
            return end
        return start

    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def checkRow(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True
        return False

