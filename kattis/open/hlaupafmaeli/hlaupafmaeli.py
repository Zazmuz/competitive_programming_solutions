year = int(input())
def cal_year(year):
    pos = year // 4 - year // 100 + year // 400
    neg = 2020 // 4 - 2020 // 100 + 2020 // 400
    return pos - neg

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(cal_year(year))
else:
    print("Neibb")