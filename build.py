from scripts.new_post import make_post
from scripts.utils import gitdiff_convert

"""
make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    is_draft = True, has_assets = True)
"""
title = "title_for_file_and_page"
display_title = None # If not none, this becomes the displayed title
date = "2019-03-25" # Date of post
collection = 'posts'
categories = [ # Categories of the post, order matters
        'cat1'
]

tags = [ # tags of the post, unordered
        'tag1'
]

make_post(
    title, display_title=display_title, date=date,
    collection=collection, categories = categories, tags = tags)

#path =
# gitdiff_convert(path)
