import os
from ansi2html import Ansi2HTMLConverter

def get_dir(root,new):
    new_dir = join(root,str(new))
    if not os.path.isdir(new_dir): os.mkdir(new_dir)
    return new_dir

def gitdiff_convert(path):
    with open(path,'r') as f:
        ansi = f.read()
    conv = Ansi2HTMLConverter()
    html = conv.convert(ansi)
    with open(path,'w') as f:
        f.write(html)
