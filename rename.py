#!/usr/bin/env python
import os
import shutil

app_name = input("Please enter project name (use - for spaces): ")

FILES = ['setup.py', 'setup.cfg', 'src/project_name/submodule/__init__.py', 'src/project_name/submodule/b.py',
         'src/project_name/__init__.py', 'src/project_name/utils.py', 'src/project_name/a.py',
         'src/project_name/main.py']
FILES = ' '.join(FILES)

os.system("sed -i \"s/project-name/" + app_name + f"/g\" {FILES}")
os.system("sed -i \"s/project_name/" + app_name.replace("-", "_") + f"/g\" {FILES}")
shutil.move("src/project_name", f"src/{app_name.replace('-', '_')}")