n=int(input())
data=list(map(int,input().split()))
data.sort()
sum=0
for i in range(0,n):
  for j in range(i+1):
    sum+=data[j]
print(sum)
    