# @Time    : 2023/5/1 23:56
# @Author  : ygd
# @FileName: 华为 引擎模块初始化.py
# @Software: PyCharm

'''
http://codefun2000.com/p/P1229
'''


n = int(input())
m={}
for i in range(n):
    a=list(map(int,input().split()))
    m[i]=a[1:]
ans = 0
nums=[]
while m:
    for a,b in m.items():
        if b==[]:
            nums.append(int(a))
        else:
            if set(b)&set(nums):
                nums.append(int(a))
    ans += 1
    for a in nums:
        if str(a) in m:
            m.pop(str(a))
print(ans)


