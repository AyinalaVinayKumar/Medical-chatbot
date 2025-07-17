import os
from pathlib import Path
import logging

#Set up logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)   #because in windows we can use \ one but in linux we will use / one to over come the issue we can use this.
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file:{filename}")
        
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
        
    else:
        logging.info(f"{filename} is already exists")