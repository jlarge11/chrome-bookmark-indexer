import json
from pathlib import Path
import os
import shutil

def process_folder(folder, parent_path, parent_level_number):
    folder_name = folder['name']
    path = f"{parent_path}/{folder_name}"
    level_number = parent_level_number + 1

    os.makedirs(path)

    for v in folder['children']:
        if v['type'] == 'url':
            name = v['name']
            url = v['url']

            with open(f'{path}/{name}.sh', 'w') as f:
                f.write('#!/bin/bash\n')
                f.write(f'google-chrome {url} &')
                
        else:
            process_folder(v, path, level_number)

user_home = str(Path.home())
with open(f'{user_home}/.config/google-chrome/Default/Bookmarks') as f:
    bookmarks = json.load(f)

bookmark_folder = f'{user_home}/bookmarks'
shutil.rmtree(bookmark_folder, ignore_errors = True)
os.makedirs(bookmark_folder)

for k, v in bookmarks['roots'].items():
    if type(v) is dict:
        process_folder(v, bookmark_folder, 0)
