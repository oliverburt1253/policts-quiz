total = 0
print("Welcome to the political quiz.")
ans1 = input("Do you support abortion? \n a)yes \n b) no \n ")
if ans1 == "a":
    total = total - 3
if ans1 == "b":
    total = total + 3
ans2 = input("Do you support hunting? \n a)yes \n b) no \n ")
if ans2 == "a":
    total = total + 3
if ans2 == "b":
    total = total - 3
ans3 = input("Do you support brexit?  \n a)yes \n b) no \n ")
if ans3 == "a":
    total = total + 1
if ans3 == "b":
    total = total - 1
ans4= input("Do you support Jeremy Corybn \n a)yes \n b) no \n ")
if ans4 == "a":
    total = total - 3
if ans4 == "b":
    total = total + 3

ans5 = input("Which party would you consider yourself to support? \n a)conservatives \n b)labour \n c)liberal democrats \n d)Ukip \n e)green \n ")
if ans5 == "a":
    total = total + 3
if ans5 == "b":
    total = total - 3
if ans5 == "c":
    total = total - 3
if ans5 == "d":
    total = total + 3
if ans5 == "e":
    total = total - 3

if total >= 3:
    print("you are right wing / conservative")

elif total <=0:
    print("you are left wing / liberal")
else:
    print("you are neutral")
