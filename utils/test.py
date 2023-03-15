import datetime
import random


if __name__=='__main__':
    x = datetime.date(2023, 1, int('01'))
    y = datetime.date(2023, 1, 31)
    c = '2023-2-1'
    print(type(x.year))
    res = [(y, 1), (x, 2)]
    print(res)
    res.sort(key=lambda x: x[0])
    print(res)
    res = [res[i][1] + res[i-1][1] for i in range(1, len(res))]
    print(res)

    x = 8.9
    y = int(x)
    print(y)


