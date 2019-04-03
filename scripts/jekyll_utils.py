import os
import pathlib
import re
from datetime import datetime
from scripts.vars import COLLECTIONS_DIR, ASSETS_DIR
from scripts.utils import similar, listdir_absolute# , atom

format_string = '%Y-%m-%d'
def parse_date(string):
    if isinstance(string, date): return string
    return datetime.strptime(string, format_string)

def format_date(date):
    try:
        return date.strftime(format_string)
    except AttributeError:
        return date

def get_collection_dir(collection):
    return os.path.join(COLLECTIONS_DIR,'_'+collection)

multiple_dashes = re.compile('[\s-]+')
def shorten_title(title):
    return multiple_dashes.sub('-', title.strip())

def format_title(title):
    return shorten_title(title).lower()

def asset_path(title, date, collection):
    month = f'0{date.month}' if date.month < 10 else date.month
    collection = 'blog' if collection in ['posts','drafts'] else collection
    return os.path.join(ASSETS_DIR, collection, str(date.year), str(month), title)

def make_assets_folder(title,date, collection):
    path = pathlib.Path( asset_path(title, date, collection) )
    path.mkdir(parents=True, exist_ok=True)
    return path

def list_posts(search_key = None, limit = 10):
    # List files in _collections/_drafts and _collections/_posts, optionally
    # Sorting by relevance to a keyword
    results = listdir_absolute(DRAFTS_DIR) + listdir_absolute(POSTS_DIR)
    if search_key is None: return results
    key = format_title(search_key)
    results = sorted(results, key=lambda x: similar(os.path.basename(x),key), reverse=True )
    return results[:limit]

def open_post(post_name, collection):
    year, month, day, *title = post_name.split('-')
    title = '-'.join(title)
    collection_dir = get_collection_dir(collection)
    path = os.path.join(collection_dir, post_name)
    post_date = datetime(
        year=int(year),
        month=int(month),
        day=int(day)
    )
    assets = make_assets_folder(title.replace('.md',''), post_date, collection)
    # atom(path, assets)

def get_post_path(title, date=None, collection= 'drafts'):
    # raise Exception('Need to fix to work with arbitrary collection, or make a docs version') \
    title = format_title(title)
    output_dir = get_collection_dir(collection)
    date = format_date( datetime.now() if date is None else date )
    return os.path.join(output_dir, "%s-%s.md" % (date,title) )
