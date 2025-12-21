from sys import setrecursionlimit
from bisect import bisect_right
setrecursionlimit(100000)
job_amount = int(input())
#jobs = list({int(i) for i in input().split()}) + [999999999999999999999999]
jobs = [int(i) for i in input().split()] + [999999999999999999999999]
jobs.sort()
#job_amount = len(jobs)-1
slide_size = [2*10**5, 3*10**5, 4*10**5]
#print(jobs)
mem = {}




def recc(index, time, cookies, deb=""):
    #print(index, time, cookies, deb)
    #print(mem)
    if index in mem:
        #print("mem", mem[index]+cookies, index)
        return mem[index] + cookies
    if index == "nej" or index >= job_amount:
        #print("cookies", cookies)
        return cookies
    ret = 0

    for i in range(3):
        if time <= jobs[index]:
            ret = max(ret, recc(bisect_right(jobs, jobs[index]+slide_size[i]-1), jobs[index]+slide_size[i], cookies+i+2, f"sex {index}"), recc(index+1, time, cookies, "sss"))
        else:
            ret = max(ret, recc(bisect_right(jobs, time-1), time, cookies, f"asd {time}"))

    mem[index] = ret - cookies
    #print("ret",ret)
    return ret

#print(bisect_right(jobs, 871277))
print(recc(0,0,0))