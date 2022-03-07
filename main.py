number=int(input("Enter a number:"))
n1=1
n2=1
n3=0
if(number==0 or number==1):
    print("The number is Fibonacci number!")
else:
    while(n3<number):
        n3=n1+n2
        n2=n1
        n1=n3
        
        


    if(n3==number):
        print("The number is fibonacci number")
    else:
        print("The number is not fibonacci")
    
