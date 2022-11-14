#sum of cube numbers
print("choice 1 is sum of cube numbers")
print("choice 2 is sum of sqaure numbers")
n=0
choice=int(input("enter the choice"))
if(choice==1):

 n=int(input("enter the number"))
sum=0
#iterating the loop up to the given number
for i in range(1,n+1):
 #adding cube sum
 sum=sum+pow(i,3)
 print(sum)
#sum of square numbers
else :
 n = int(input("enter the number"))
def squaresum(n):
    return(n*(n+1/2)*(2*n+1/3))
    print(squaresum(n))

