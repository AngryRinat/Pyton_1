def nums_generator(max_num):
   for i in range(max_num+1):
       yield print(i)

odd_to_count = nums_generator(10)

next(odd_to_count)
next(odd_to_count)
next(odd_to_count)
next(odd_to_count)
