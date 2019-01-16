import os, pathlib
from datetime import datetime
from scripts.vars import DRAFTS_DIR, POSTS_DIR, BLOG_ASSETS_DIR

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
    month = f'0{n}' if date.month < 10 else date.month
    return os.path.join(BLOG_ASSETS_DIR, date.year, month, title)

def make_blog_assets_folder(title,date):
    path = pathlib.Path( blog_asset_path(title, date) )
    path.mkdir(parents=True, exist_ok=True)
    return path

def search_for_post(title, date=None):
    pass

def get_post_path(title,date=None,is_draft=True, search = True):
    title = format_title(title)
    if search is True:
        path = search_for_post(title, date)
        if path is not None: return path
    output_dir = DRAFTS_DIR if is_draft else POSTS_DIR
    date = format_date( datetime.now() if date is None else date )
    return os.path.join(output_dir, "%s-%s.md" % (date,title) )
