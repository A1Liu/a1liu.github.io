import os, pathlib
from datetime import datetime
from scripts.vars import DRAFTS_DIR, POSTS_DIR, BLOG_ASSETS_DIR
from scripts.utils import similar, listdir_absolute, atom

format_string = '%Y-%m-%d'
def parse_date(string):
    if isinstance(string, date): return string
    return datetime.strptime(string, format_string)

def format_date(date):
    try:
        return date.strftime(format_string)
    except AttributeError:
        return date

def format_title(title):
    return title.strip().lower().replace(' ','-')

def blog_asset_path(title, date):
    month = f'0{date.month}' if date.month < 10 else date.month
    return os.path.join(BLOG_ASSETS_DIR, str(date.year), str(month), title)

def make_blog_assets_folder(title,date):
    path = pathlib.Path( blog_asset_path(title, date) )
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

def open_post(post_name):
    year, month, day, *title = post_name.split('-')
    title = '-'.join(title)
    if os.path.exists(os.path.join(POSTS_DIR, post_name)):
        path = os.path.join(POSTS_DIR, post_name)
    else:
        path = os.path.join(DRAFTS_DIR, post_name)
    post_date = datetime( year=int(year), month=int(month), day=int(day) )
    assets = make_blog_assets_folder(title.replace('.md',''), post_date )
    atom(path, assets)

def get_post_path(title,date=None,is_draft=True):
    title = format_title(title)
    output_dir = DRAFTS_DIR if is_draft else POSTS_DIR
    date = format_date( datetime.now() if date is None else date )
    return os.path.join(output_dir, "%s-%s.md" % (date,title) )
