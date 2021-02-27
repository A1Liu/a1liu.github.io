#!/usr/bin/env python3
import sys, os
from aliu.string import parse_args
from aliu import repl
import pprint
import traceback

_pp = pprint.PrettyPrinter(indent = 2)
_namespace = {}
_help_text = {
    '=' : "The assignment operator. Example: col= drafts",
}
_assign_overrides = {}

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

@set_help_text("List all available values and commands.")
@in_namespace('names', 'namespace')
def namespace():
    return [key for key in _namespace]

@in_namespace('q', 'quit')
def quit_repl():
    return repl.QUIT_REPL

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
            name, msg= err.__class__.__name__, err.__str__()
            # tb = traceback.format_tb(err.__traceback__)
            # return f"{name}: {msg}\n{''.join(tb).strip()}"
            return f"{name}: {msg}"


    def print(self, value):
        if value is not None and not isinstance(value, str):
            super().print(_pp.pformat(value))
        else:
            super().print(value)

