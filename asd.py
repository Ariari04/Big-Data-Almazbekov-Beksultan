a = input()
b = ""
c = ""
for i in range(len(a)):
    if a[i] == '=':
        b = a[0: i]
        c = a[i+1: len(a)]
if eval(b) == eval(c):
    print("YES")
else:
    print("NO")