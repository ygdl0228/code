# @Time    : 2023/5/17 16:56
# @Author  : ygd
# @FileName: 510华为.py
# @Software: PyCharm

'''
https://mp.weixin.qq.com/s/x9OJGKBgcwqfocHm9YU-eQ
'''

arr = [6, 6]
st = []


def fun():
    if len(st) > 1 and st[-1] == st[-2]:
        num = st.pop()
        st.pop()
        st.append(2 * num)
        fun()
    elif len(st) > 2:
        num_sum = 0
        for i in range(len(st) - 1):
            num_sum += st[len(st) - 2 - i]
            if num_sum >= st[-1]:
                if num_sum == st[-1]:
                    for _ in range(i + 2):
                        st.pop()
                    st.append(2 * num_sum)
                    fun()
            break


for i in arr:
    st.append(i)
    fun()
for i in st:
    print(i, end=' ')

a = input()
b = int(input())
c = input()
size = len(a)


def is_vaild(s):
    return len(set(s)) == 1


ans = 0
for i in range(size):
    for j in range(3, 13):
        num = int(a[i:i + j + 1])
        if c == '+':
            if is_vaild(str(num + b)):
                ans = max(ans, num)
            elif c == '-':
                if is_vaild(str(num - b)):
                    ans = max(ans, num)
            else:
                if is_vaild(str(num * b)):
                    ans = max(ans, num)
print(ans)
