from scripts.new_post import make_post
from scripts.utils import gitdiff_convert

"""
make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    is_draft = True, has_assets = True)
"""
title = "Explicit Captures for Rust Blocks" # Will raise exception if None
display_title ="Explicit Captures for Closures and Code Blocks in Rust"
date = "2019-03-21"
collection = 'posts'
categories = [
    'bugs-nyu', 'yacs'
]

tags = [
    'language-design'
]

make_post(
    title, display_title=display_title, date=date,
    collection=collection, categories = categories, tags = tags)

#path =
# gitdiff_convert(path)
