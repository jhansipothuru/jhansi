a,list = int(input()),[i for i in range(12,90) if i%10 != 0 if i%10 > i//10]
if a % 10 == 0 or a % 10 <= a // 10 or a < 10 or a > 99: print('invalid')
for j in range(len(list)-1):
  if list[j] == a:print(list[j-1],list[j+1])
if a == list[len(list)-1]:print(list[0],list[len(list)-2])

 
  
    
  
    



