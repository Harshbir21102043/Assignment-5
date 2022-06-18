#ques 6
high=int(input("Enter the maximum number of range: "))
low=int(input("Enter the minimum number of range: "))
for no in range(low,high+1):
    for i in range(2,no):
        if no%i==0:
            break
    else :
        print(no)
