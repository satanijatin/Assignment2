# numberlist=[89,52,68,98,97,69,56,63,35,25,24,15,16,58]
# print(numberlist[::-1])

for i in range(0,5):
    for j in range(0,8):
        if j>=i and j<=8-i:
            print("*", end=" ")
        else:
             print(" " ,end=" ")
    print()