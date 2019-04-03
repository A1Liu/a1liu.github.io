import os # import re # escaped = re.escape(a_string)
from nltk.corpus import stopwords
from scripts.jekyll_utils import get_post_path, open_post, shorten_title

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

def capitalize_word(word):
    if len(word) > 1 and (len(word) > 5 or word not in en_stopwords):
        return word[0].upper()+word[1:]
    return word

def make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    collection = 'drafts', has_assets = True):

    # Setting up vars

    if display_title is None:
        title_words = shorten_title(title).split('-')
        display_title = ' '.join( [capitalize_word(word) for word in title_words] )
    output_path = get_post_path(title, date=date, collection=collection)
    open_post(os.path.basename(output_path), collection)

    with open( output_path, 'x') as f:
        f.write(format_new_post(display_title, categories, tags))
