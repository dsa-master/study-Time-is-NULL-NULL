n=int(input())
count=0
if n%5==0:
  count+=n//5
  print(count)
else:
  while True:
    if n%5!=0:
      n-=3
      count+=1
 
    elif n%5==0:
      n-=5
      count+=1

    if n<3:
      break
    if n==0:
      break
  if n!=0:
    print(-1)
  else:
    print(count)