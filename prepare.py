#!/usr/bin/env python
import os
import shutil

print("Welcome to this package template")
print(f"This command 'make prepare' will do the following things")
print("1. Rename all occurrences of project_name and project-name to what you choose")
print("2. Create virtual environment in the venv folder")
print("3. Install build tools")
print("4. Install this package itself, to install deps and add project to Python dep tree")

app_name = input("Please enter project name (use - for space, they will automatically be converted to _ where necessary): ")
os.system("find . -not -path '*/\.*' -not -path venv -type f -exec sed -i \"s/project-name/" + app_name + "/g\" {} \;")
os.system("find . -not -path '*/\.*' -not -path venv -type f -exec sed -i \"s/project_name/" + app_name.replace("-", "_") + "/g\" {} \;")

shutil.move("src/project_name", f"src/{app_name.replace('-', '_')}")