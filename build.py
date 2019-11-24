#!/usr/bin/env python3
import sys, os
from scripts.collection import Collection
from aliu.string import parse_args
from aliu import repl

_collection = Collection('posts')
_assign_overrides = {}
_namespace = {}
_help_text = {
    '=' : "The assignment operator. Example: col= drafts",
}

def _namespace_set(name, value):
    if name in _assign_overrides:
        return _assign_overrides[name](value)
    else:
        _namespace[name] = value
        return value

def _namespace_get(name, *args):
    if name in _namespace:
        return _namespace[name]
    else:
        raise NameError(f"Name '{name}' not found.")

def in_namespace(name, *args):
    if hasattr(name, '__call__'):
        _namespace[name.__name__] = name
        return name
    elif args:
        def set_names(func):
            _namespace_set(name, func)
            for a in args:
                _namespace_set(a, func)
            return func
        return set_names
    else:
        return lambda func: _namespace_set(name, func)

def set_help_text(text):
    def dec(func):
        global _help_text
        _help_text[func] = text
        return func
    return dec

def assignment_override(name, *args):
    if hasattr(name, '__call__'):
        _assign_overrides[name.__name__] = name
        return name
    elif args:
        def dec(func):
            _assign_overrides[name] = func
            for a in args:
                _assign_overrides[a] = func
            return func
        return dec
    else:
        def dec(func):
            _assign_overrides[name] = func
            return func
        return dec

@set_help_text("Get help on something. Usage: help <command-name>")
@in_namespace
def help(name='help'):
    global _help_text
    if name in _help_text:
        return _help_text[name]
    elif name in _namespace and _namespace[name] in _help_text:
        return _help_text[_namespace[name]]
    else:
        return "No help text available for '" + name + "'."

@set_help_text("""Add an item to the current collection.
Usage:
    add_item <title>,<date>,<categories>,<tags>
Example:
    add_item 'Hello, World!',2019-12-29,meta,first-post:meta
    add_item 'Hello, World!',today,meta,first-post:meta""")
@in_namespace
def add_item(title, date, categories = [], tags = []):
    collection = _namespace_get('col')
    if date.lower() == 'today':
        date = None
    categories = categories.split(':') if isinstance(categories, str) else categories
    tags = tags.split(',') if isinstance(tags, str) else tags
    path = collection.add_item(title=title, date=date, categories=categories, tags=tags)
    return os.path.relpath(path)

@set_help_text("List all available values and commands.")
@in_namespace('names', 'namespace')
def namespace():
    return [key for key in _namespace]

@set_help_text("The collection we're currently operating on.")
@in_namespace('col', 'collection')
def collection():
    return _collection

@in_namespace('q', 'quit')
def quit_repl():
    return repl.QUIT_REPL

@assignment_override('col', 'collection')
def setcol(col):
    global _collection
    _collection = Collection(col)
    return _collection

class Repl(repl.Repl):

    def __init__(self):
        super().__init__(prompt = "%~ ")

    def parse(self, buffer):
        # Make this better with
        # http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#user-input
        func = ''
        idx = 0
        while idx < len(buffer):
            func += buffer[idx]
            if buffer[idx] in set(['=', ' ', '\t']):
                break
            idx += 1
        func = func.strip()
        txt = buffer[idx+1:].strip()
        if func == '':
            return repl.SKIP_EVALUATION
        return func,[arg.strip() for arg in parse_args(txt.strip(), sep=',')]

    def eval(self, parsed_data):
        func, args = parsed_data
        try:
            if args and not func.endswith('='):
                result = _namespace_get(func)(*args)
            elif func.endswith('='):
                func = func[0:-1]
                result = _namespace_set(func, (*args,) if len(args) > 1 else args[0])
            else:
                result = _namespace_get(func)
                if hasattr(result, '__call__'):
                    result = result()
            return result if result is not None else repl.SKIP_PRINTING
        except Exception as err:
            return err.__class__.__name__ + ": " + err.__str__()

Repl().run()
