import os # import re # escaped = re.escape(a_string)
from datetime import datetime
from nltk.corpus import stopwords
from functools import reduce
from scripts.utils import PROJECT_DIR,COLLECTIONS_DIR,DRAFTS_DIR,POSTS_DIR

en_stopwords = set( stopwords.words('english') )
join = os.path.join

format_string = '%Y-%m-%d'
def parse_date(string):
    return datetime.strptime(string, format_string)

def format_date(date):
    return date.strftime(format_string)

def zero_pad(n):
    return f'0{n}' if n < 10 else n

def get_dir(root,new):
    new_dir = join(root,str(new))
    if not os.path.isdir(new_dir): os.mkdir(new_dir)
    return new_dir

def make_assets_folder(title,date):
    date = parse_date(date)
    reduce(get_dir, [BLOG_ASSETS_DIR, date.year, zero_pad(date.month), title])

def capitalize_title_word(word):
    if len(word) > 5 or word not in en_stopwords:
        return word.capitalize()
    return word

def make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    is_draft = True, has_assets = True):

    # Setting up vars
    output_dir = drafts_dir if is_draft else POSTS_DIR
    date = format_date(datetime.now()) if date is None else date
    title = title.lower().strip()
    if display_title is None: display_title = title
    display_title = ' '.join( [capitalize_title_word(word) for word in display_title.split(' ')] )
    title = title.replace(' ','-')

    if has_assets: make_assets_folder(title,date)
    with open(join(output_dir, "%s-%s.md" % (date,title) ), 'x') as f:
        f.write('---\n')
        f.write('title: {}\n'.format(display_title))
        f.write('categories: [%s]\n' % ', '.join(categories) )
        f.write('tags: [ %s ]\n' % ', '.join(tags) )
        f.write('---\n\n')
