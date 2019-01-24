import os # import re # escaped = re.escape(a_string)
from nltk.corpus import stopwords
from scripts.jekyll_utils import get_post_path, open_post
from scripts.utils import atom

en_stopwords = set( stopwords.words('english') )
new_post_format = """---
title: %s
categories: [%s]
tags: [%s]
---
<!-- {%% raw %%} -->
<!-- {%% include refc-small.html text="ref commit" commit="3cad965..." %%} -->
<!-- {%% include ref-commit.html text="ref commit" commit="3cad965..." %%} -->
<!-- {%% endraw %%} -->
"""

def format_new_post(title, categories, tags):
    return new_post_format % (
            title, ', '.join(categories), ', '.join(tags) )

def capitalize_title_word(word):
    if len(word) > 1 and (len(word) > 5 or word not in en_stopwords):
        return word[0].upper()+word[1:]
    return word

def make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    is_draft = True, has_assets = True):

    # Setting up vars

    if display_title is None: display_title = title
    display_title = ' '.join( [capitalize_title_word(word) for word in display_title.split(' ')] )
    output_path = get_post_path(title,date=date,is_draft=is_draft)
    open_post(os.path.basename(output_path))

    with open( output_path, 'x') as f:
        f.write(format_new_post(display_title, categories, tags))
