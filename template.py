"""
Script to generate folders by automation
"""

# Importing libraries
import os, sys
from pathlib import Path
import logging


# project name
while True:
    project_name = input("Please enter your project name : ")
    if project_name:
        break
    else:
        print("Project name cannot be blank\n")

# List of files requires
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]


# creatings file by automation
for file_path in list_of_files:
    # creating a path for file
    file_path = Path(file_path)

    # accessing file directory and file name
    file_dir, file_name = os.path.split(file_path)

    if file_dir:
        # creating directory
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for file {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            logging.info(f"Creating empty {file_name} at {file_dir}")
    else:
        logging.info(f"File is already present at: {file_path}")