#!/usr/bin/env python3
import sys, os
from scripts.collection import Collection
from aliu.string import parse_args
from aliu import repl

def get(name):
    global namespace
    if name in namespace:
        return namespace[name]
    else:
        return "NamespaceError: '" + name + "' not defined."

def set(name, value):
    global namespace
    namespace.__setitem__(name, value)

def get_help(name='help'):
    global help_text
    if name in help_text:
        return help_text[name]
    elif name in namespace and namespace[name] in help_text:
        return help_text[namespace[name]]
    else:
        return "No help text available for '" + name + "'."

def add_item(title, date, categories = [], tags = []):
    collection = get('collection')
    if date.lower() == 'today':
        date = None
    categories = categories.split(':') if isinstance(categories, str) else categories
    tags = tags.split(',') if isinstance(tags, str) else tags
    path = collection.add_item(title=title, date=date, categories=categories, tags=tags)
    return os.path.relpath(path)

def list_namespace():
    return str([key for key in namespace.keys()])

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
    add_item  : """
Add an item to the current collection.
Usage:
    add_item <title>,<date>,<categories>,<tags>
Example:
    add_item 'Hello, World!',2019-12-29,meta,first-post:meta""".strip(),
    "help"      : "Get help on something. Usage: help <command-name>",
}

class Repl(repl.Repl):

    def __init__(self):
        super().__init__(prompt = "%~ ")

    def parse(self, buffer):
        # Make this better with
        # http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#user-input
        func, txt = (buffer + ' ').split(" ", 1)
        if func.strip() == '':
            return repl.SKIP_EVALUATION
        return func,[arg.strip() for arg in parse_args(txt.strip(), sep=',')]

    def eval(self, parsed_data):
        func, args = parsed_data
        func = get(func)
        if hasattr(func, '__call__'):
            try:
                result = func(*args)
                return result if result is not None else repl.SKIP_PRINTING
            except Exception as err:
                return err.__class__.__name__ + ": " + err.__str__()
        else:
            return func

Repl().run()
