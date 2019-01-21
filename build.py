from scripts.new_post import make_post
from scripts.utils import gitdiff_convert

"""
make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    is_draft = True, has_assets = True)
"""
title = "lang-spec-of-course-prereqs" # Will raise exception if None
display_title =  "Language Specification and DB Representation of Course Prerequisites"
date = "2019-02-01"
categories = [
    'bugs-nyu','yacs'
]

tags = [
    'postgres','sql','lang-spec'
]

make_post(title, display_title=display_title, date=date, categories = categories, tags = tags)

#path =
# gitdiff_convert(path)
