r = int(input())
c = int(input())
l,l2 = [],[]
for i in range(r):
  l = input()
  l2.append(list(l))
print('across')
for i in range(r):
  for j in range(c):
    if l2[i][j] != '*':
      print(l2[i][j],end = '')
      if j == c-1:
        print('')
    else:
      print('')
print('down')
for j in range(c):
  for i in range(r):
    if l2[i][j] != '*':
      print(l2[i][j],end = '')
      if i == r-1:
        print('')
    else:
      print('')


