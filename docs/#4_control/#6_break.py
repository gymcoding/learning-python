#-- break
# ● break를 만나면 반복문 내부 블록을 벗어남
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i > 5:
    break
  print('Item: {0}'.format(i))

print('-----')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i > 5:
    break
  print('Item: {0}'.format(i))
else:
  print('Exit without break.')
print('Always this is printed')