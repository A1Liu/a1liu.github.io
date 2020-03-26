#!/usr/bin/env python3
import sys, os
from scripts.collection import Collection
from scripts.repl import set_help_text, in_namespace, assignment_override, Repl

_collection = Collection('posts')

@set_help_text("The collection we're currently operating on.")
@in_namespace('col', 'collection')
def collection():
    return _collection

@assignment_override('col', 'collection')
def setcol(col):
    global _collection
    _collection = Collection(col)
    return _collection


@set_help_text("""Add an item to the current collection.
Usage:
    add_item <title>,<date>,<categories>,<tags>
Example:
    add_item 'Hello, World!',2019-12-29,meta,first-post:meta
    add_item 'Hello, World!',today,meta,first-post:meta""")
@in_namespace
def add_item(title, date, categories = [], tags = []):
    collection = _collection
    if date.lower() == 'today':
        date = None
    categories = categories.split(':') if isinstance(categories, str) else categories
    tags = tags.split(',') if isinstance(tags, str) else tags
    path = collection.add_item(title=title, date=date, categories=categories, tags=tags)
    return os.path.relpath(path)

@set_help_text("Gets the contents of the current collection.")
@in_namespace
def contents():
    return [
        ({'attributes':p['attributes'], 'content': p['content'][0:10] + '...'} if len(p['content']) > 10 else p)
        for p in _collection.list_items()
    ]

@set_help_text("Gets the category heirarchy of the current collection.")
@in_namespace
def categories():
    return _collection.categories()

@set_help_text("Gets the tag list of the current collection.")
@in_namespace
def tags():
    return _collection.tags()

repl = Repl()
repl.run()
