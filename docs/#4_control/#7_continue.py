#-- continue
# ● continue 이후 반복문 내부 블록을 수행하지 않고, 다음 아이템을 선택하여 내부 블록의 시작 지점으로 이동
# 예제)
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i % 2 == 0:
    continue
  print('Item: {0}'.format(i))

print('-----')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i % 2 == 0:
    continue
  print('Item: {0}'.format(i))
else:
  print('Exit without break.')
print('Always this is printed')