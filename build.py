from scripts.collection import Collection

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

collection = Collection(collection)
collection.add_item(title=title, date=date,categories=categories,tags=tags)
