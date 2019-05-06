p = 1
while(1):
  a,b,k,l = [],[],0,0
  a1 = input()
  if a1 == 'Z':
    break
  else:
    a2,a3,a4,a5,a6 = input(),input(),input(),input(),input()
    a = [list(a1),list(a2),list(a3),list(a4),list(a5)]
    for i in range(len(a)):
      for j in range(len(a[i])):
        if a[i][j] == ' ':
          k,l = i,j
    b = list(a6)
    for m in range(len(b)):
      if b[m] == 'A':
        if k == 0:
          print('This puzzle has no configuration')
          break
        else:
          a[k][l],a[k-1][l] = a[k-1][l],a[k][l]
          k,l = k-1,l
      elif b[m] == 'B':
        if k == 4:
          print('This puzzle has no configuration')
          break
        else:
          a[k][l],a[k+1][l] = a[k+1][l],a[k][l]
          k,l = k+1,l
      elif b[m] == 'L':
        a[k][l],a[k][l-1] = a[k][l-1],a[k][l]
        if k == 0:
          print('this puzzle has no configuration')
          break
        else:
          a[k][l],a[k][l-1] = a[k][l-1],a[k][l]
          k,l = k,l-1
      elif b[m] == 'R':
        a[k][l],a[k][l+1] = a[k][l+1],a[k][l]
        if k == 5:
          print('this puzzle has no configuration')
          break
        else:
          a[k][l],a[k][l+1] = a[k][l+1],a[k][l]
          k,l = l,l+1
      else:
        print('puzzle #',end = '')
        print(p)
        for i in range(len(a)):
          for j in range(len(a[i])):
            print(a[i][j],end = ' ')
          print( )
        p += 1
        


