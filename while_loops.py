"""i = 1
while i < 6:
  print(i)
  i += 1"""
i = 1
while i < 6:     # With the break statement we can stop the loop even if the while condition is true
  print(i)
  if i == 3:
    break
  i += 1