
stringlist = ["jaj", "yug", "abca", "hhh", "ytu", "hello","jatin"]

count = 0

for s in stringlist:
   
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1


print(count)
