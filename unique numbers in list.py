def unique_list(lst):
  x = []
  for a in lst:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))
