import json

INDENT = 4

def determine_indent(level):
    return ' ' * level * INDENT

def print_folder(name, level):
    indent = determine_indent(level)
    print(f'{indent}- {name}')

def print_bookmark(b, level):
    indent = determine_indent(level)
    name = b['name']
    url = b['url']
    print(f'{indent}    {name} ({url})')

def process_folder(folder, parent_path, parent_level_number):
    folder_name = folder['name']
    path = f"{parent_path}/{folder_name}"
    level_number = parent_level_number + 1

    print_folder(folder_name, level_number)

    for v in folder['children']:
        if v['type'] == 'url':
            print_bookmark(v, level_number)
        else:
            process_folder(v, path, level_number)

with open('/home/jlarge/.config/google-chrome/Default/Bookmarks') as f:
    bookmarks = json.load(f)

for k, v in bookmarks['roots'].items():
    if type(v) is dict:
        process_folder(v, '.', 0)
