#ques5
n=int(input("Enter number of rows: "))
p=ord("A")
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(chr(p),end="")
        p+=1
    print()
