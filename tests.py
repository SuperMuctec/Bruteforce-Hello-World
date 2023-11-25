import string as str
a = "abcdefghijklmnopqrstuvwxyz"
b = a.upper()
c = "1234567890 "
d = str.punctuation
print(len(a+b+c+d))
all = c + b+a+d
cnt = 0
lines = 0
for i in range(len("py")):
    cnt+=1
    if cnt == 1:
        for j in all:
            print(j)
            lines += 1
            if j == "py"[i]:
                break
    elif cnt == 2:
        for j in all:
            print("p"+j)
            lines += 1
            if j == "py"[i]:
                break
print(lines)