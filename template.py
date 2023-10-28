import os
from pathlib import Path
import logging

while True:
    project_name=input("Enter your project name: ")
    if project_name!="":
        break

#src/_init_.py
#src/componet/_init_.py
list_of_files=[
    f"{project_name}/_init_.py",
    f"{project_name}/component/_init_.py",
    f"{project_name}/config/_init_.py",
    f"{project_name}/constant/_init_.py",
    f"{project_name}/entity/_init_.py",
    f"{project_name}/exception/_init_.py",
    f"{project_name}/logger/_init_.py",
    f"{project_name}/pipeline/_init_.py",
    f"{project_name}/utils/_init_.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        logging.info("file already present at :{filepath}")