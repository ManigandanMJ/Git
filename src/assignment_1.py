# program for push,pull,merge,revert,reset,check-pick
print('********* Find Leap Year ********')
year=int(input("Enter the Year to find if Leap or Note: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("Year",year," is Leap year")
    print("********** Completed **********")
else:
    print("Year ",year,"Not Leap year")
f=int(input("Enter f : "))
if f == 1:
    print("**Completed**")
else:
    print("**End***")
print("Reset commit")
print("Updated reset commit")
