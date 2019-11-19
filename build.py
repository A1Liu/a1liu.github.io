#!/usr/bin/env python3
import sys, os
from scripts.collection import Collection
from aliu.string import parse_args
import readline

def get(name):
    global namespace
    if name in namespace:
        return namespace[name]
    else:
        print("NamespaceError: '" + name + "' not defined.")

def set(name, value):
    global namespace
    namespace.__setitem__(name, value)

def get_help(name='help'):
    global help_text
    if name in help_text:
        return help_text[name]
    else:
        print("No help text available for '" + name + "'.")

def add_item(title, date, categories = [], tags = []):
    collection = get('collection')
    if date.lower() == 'today':
        date = None
    categories = categories.split(':') if isinstance(categories, str) else categories
    tags = tags.split(',') if isinstance(tags, str) else tags
    path = collection.add_item(title=title, date=date, categories=categories, tags=tags)
    return os.path.relpath(path)

def list_namespace():
    return '\n'.join("%s\n    %s" % (name, get_help(name)) for name in namespace.keys())

namespace = {
    'add_item'  : add_item,
    'quit'      : exit,
    'q'         : exit,
    'set'       : set,
    'get'       : get,
    'help'      : get_help,
    'setcol'    : lambda col: set('collection', col),
    'getcol'    : lambda: get('collection'),
    'collection': Collection('posts'),
    'names'     : list_namespace,
    'namespace' : list_namespace,
}

help_text = {
    "add_item"  : """
Add an item to the current collection.
Usage:
    add_item <title>,<date>,<categories>,<tags>
Example:
    add_item 'Hello, World!',2019-12-29,meta,first-post:meta""".strip(),
    "help"      : "Get help on something. Usage: help <command-name>",
}

while True:
    txt = input("%~ ") + ' '
    func, txt = txt.split(" ", 1)
    args = [arg.strip() for arg in parse_args(txt.strip(), sep=',')]

    func = get(func)
    result = None
    if func is None:
        continue
    if hasattr(func, '__call__'):
        try:
            result = func(*args)
        except Exception as err:
            result = err.__class__.__name__ + ": " + err.__str__()
        if result is not None:
            print(result)
    else:
        print(func)
