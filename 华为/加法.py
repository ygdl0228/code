# @Time    : 2023/5/8 21:01
# @Author  : ygd
# @FileName: 加法.py
# @Software: PyCharm


'''
http://codefun2000.com/p/P1250
'''

# n = int(input())
# str1 = str(input())
n = 14
s = "#9.@527+#4.!19"

a, b = s.split("+")

sc = {'!': 0, '@': 0, '#': 0}
sr = {
    ('!', '!'): 0,
    ('!', '@'): 13,
    ('!', '#'): 4,
    ('@', '@'): 7,
    ('@', '#'): 20,
    ('#', '#'): 5
}

if '.' in a:
    az, ax = a.split(".")
else:
    az, ax = a, '0'

if '.' in b:
    bz, bx = b.split(".")
else:
    bz, bx = b, '0'

add = 0

# 判断特殊字符是在前面还是后面
if '!' in az or '@' in az or '#' in az:
    # 特殊前面,从最后面往前面对齐
    for i in range(len(az)):
        if az[len(az) - i - 1] in sc:
            cur = -1

            if (az[len(az) - i - 1], bz[len(bz) - i - 1]) in sr:
                cur = sr[(az[len(az) - i - 1], bz[len(bz) - i - 1])]
            else:
                cur = sr[(bz[len(bz) - i - 1], az[len(az) - i - 1])]

            add = cur * (10 ** (i))
            for c in sc:
                az = az.replace(c, "0")
                bz = bz.replace(c, "0")

            break

else:
    # 特殊字符在后面，从0开始匹配
    for i in range(len(ax)):
        if ax[i] in sc:
            cur = -1
            if (ax[i], bx[i]) in sr:
                cur = sr[(ax[i], bx[i])]
            else:
                cur = sr[(bx[i], ax[i])]

            add = cur * (10 ** (-i - 1))
            for c in sc:
                ax = ax.replace(c, "0")
                bx = bx.replace(c, "0")
            break

o1 = az + "." + ax
o2 = bz + "." + bx

res = float(o1) + float(o2) + float(add)
res = round(res, 4)
res = str(res).rstrip('0').rstrip('.')
print(res)
