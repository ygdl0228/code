# @Time    : 2023/5/6 22:19
# @Author  : ygd
# @FileName: 幼儿园.py
# @Software: PyCharm

'''
http://codefun2000.com/p/P1217
'''

n = 5
high = [81, 82 ,76, 75 ,100]
ans = []
for i in range(n):
    count = 0
    num = high[i]
    for j in high[i:]:
        if num > j:
            count += 1
    ans.append(count)
for i in ans:
    print(i,end=' ')
