import os
import shutil

os.chdir('E:\Ринат\PythonProjects\pythonProject')

try:
    shutil.copytree(r'my_project\mainapp\templates', r'my_project\templates\mainapp', dirs_exist_ok=True)
    shutil.copytree(r'my_project\adminapp\templates', r'my_project\templates\adminapp', dirs_exist_ok=True)
    shutil.copytree(r'my_project\authapp\templates', r'my_project\templates\authapp', dirs_exist_ok=True)
except (FileNotFoundError) as e:
    print(f'There is no such file in directory')
finally:
    print('Good bye')

