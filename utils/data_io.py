import pandas as pd
import json
import os

def join_path(root:str, *path:str) -> str:
    return root + os.sep + os.sep.join(path)

def save_csv(df:pd.DataFrame, dir:str, file_name:str):
    os.makedirs(dir, exist_ok=True)
    path = join_path(dir, file_name)
    df.to_csv(path, index=False)

def save_json(obj,  dir:str, file_name:str):
    os.makedirs(dir, exist_ok=True)
    path = join_path(dir, file_name)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=4)

