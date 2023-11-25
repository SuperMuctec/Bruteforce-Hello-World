import string as str
a = "abcdefghijklmnopqrstuvwxyz"
b = a.upper()
c = "1234567890 "
d = str.punctuation
all = c+b+a+d
cnt = 0
lines = 0
for i in range(len("Hello World")):
    cnt += 1
    if cnt == 1:
        for j in all:
            print(j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 2:
        for j in all:
            print("H"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 3:
        for j in all:
            print("He"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 4:
        for j in all:
            print("Hel"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 5:
        for j in all:
            print("Hell"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 6:
        for j in all:
            print("Hello"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 7:
        for j in all:
            print("Hello "+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 8:
        for j in all:
            print("Hello W"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 9:
        for j in all:
            print("Hello Wo"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 10:
        for j in all:
            print("Hello Wor"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 11:
        for j in all:
            print("Hello Worl"+j)
            lines+=1
            if j == "Hello World"[i]:
                break
    elif cnt == 12:
        for j in all:
            print("Hello World"+j)
            lines+=1
            if j == "Hello World"[i]:
                break

print(f"It took {lines} lines to print 'Hello World' put the output in the text editor and check")