import sys
user_dict = {}
with open('users.csv', 'r') as f, open('hobbys.csv', 'r') as f_f:

   line = f.readline()
   line_1 = f_f.readline()

   while line:
       user_dict[line.replace('\n', '')] = line_1.replace('\n', '') if line_1 != '' else None

       line = f.readline()
       line_1 = f_f.readline()



with open('user_dictionary.txt', 'w+', encoding='utf-8') as f:
   for key in user_dict:
         f.writelines(f'{key} имеет хобби {user_dict[key]}\n')

   f.seek(0)
   print(f.read())
sys.exit('')





