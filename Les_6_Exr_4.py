user_dict = {}
with open('users.csv', 'r') as f, open('hobbys.csv', 'r') as f_f:

   line = f.readline().replace('\n', '')
   line_1 = f_f.readline().replace('\n','')

   while line:
      line_list = line.split(',')
      line_1_list = line_1.split(',') if len(line_1) != 0 else None

      if line_list[0] not in user_dict:
         user_dict[line_list[0]] = []

      user_dict[line_list[0]].append(line_list[1:])
      user_dict[line_list[0]].append(line_1_list)

      line = f.readline().replace('\n', '')
      line_1 = f_f.readline().replace('\n', '')


print(user_dict)