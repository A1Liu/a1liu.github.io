import logging
import sys
from scripts.collection import Collection
from aliu.string import parse_args
import readline

if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    logging.basicConfig(level=logging.DEBUG)

def get(name):
    global namespace
    if name in namespace:
        return namespace[name]
    else:
        print("NamespaceError: '" + name + "' not defined.")

def set(name, value):
    global namespace
    namespace.__setitem__(name, value)

def help(name='help'):
    global help_text
    if name in help_text:
        return help_text[name]
    else:
        print("No help text available for '" + name + "'.")

def add_item(title, date, categories = [], tags = []):
    collection = get('collection')
    categories = categories.split(',') if isinstance(categories, str) else categories
    tags = tags.split(',') if isinstance(tags, str) else tags
    collection.add_item(title=title, date=date, categories=categories, tags=tags)

namespace = {
        'add_item'  : add_item,
        'quit'      : quit,
        'q'         : quit,
        'set'       : set,
        'get'       : get,
        'help'      : help,
        'setcol'    : lambda col: set('collection', col),
        'getcol'    : lambda: get('collection'),
        'collection': Collection('posts'),
        }

namespace['namespace'] = namespace

help_text = {
        'add_item':"Add an item to the current collection.",
        }

while True:
    txt = input(">> ") + ' '
    func, txt = txt.split(" ", 1)
    args = [arg.strip() for arg in parse_args(txt.strip(), sep=',')]

    func = get(func)
    result = None
    if func is None:
        continue
    if '__call__' in dir(func):
        try:
            result = func(*args)
        except Exception as err:
            result = err.__class__.__name__ + ": " + err.__str__()
        if result is not None:
            print(result)
    else:
        print(func)
