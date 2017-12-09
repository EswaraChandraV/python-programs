n = int(input())
sum = 0
for i in range(1,n+1):
    if(n % i == 0):
        print(i)
        sum=sum+i
print(sum)    
           
           