lst=[1,2,3,4,5,6,7,8]
while len(lst)>3:
    del lst[2]
    print(lst)
else:
    print('List too small')
    


def remove_nums(int_list):
  position = 2
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
