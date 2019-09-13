import os, re
from difflib import SequenceMatcher
from aliu.string import parse_args

def get_dir(root,new):
    new_dir = join(root,str(new))
    if not os.path.isdir(new_dir): os.mkdir(new_dir)
    return new_dir

replace_str = re.compile(r'(\[1mdiff)')
def gitdiff_convert(path):
    with open(path,'r') as f:
        ansi = f.read()

    # \033[1m is white bold
    # \033[31m is red
    # \033[32m is white
    conv = Ansi2HTMLConverter()
    ansi = (ansi
            .replace("\033[1mdiff","\n\n\033[1mdiff")
            .replace("\033[1mrename from","\033[31mrename from")
            .replace("\033[1mrename to","\033[32mrename to")
            .strip()
            )
    html = conv.convert( ansi )
    with open(path,'w') as f:
        f.write(html)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def listdir_absolute(dirname):
    return [os.path.join(dirname,name) for name in os.listdir(dirname)]
