import os
from datetime import datetime
from nltk.corpus import stopwords
from functools import reduce


en_stopwords = set( stopwords.words('english') )
join = os.path.join
dirname = os.path.dirname

project_dir = dirname( dirname(__file__) )
collections_dir = join(project_dir,'collections')
drafts_dir = join(collections_dir,'_drafts')
posts_dir = join(collections_dir,'_posts')
blog_assets_dir = join(project_dir,'assets','blog')

format_string = '%Y-%m-%d'
parse_date = lambda string: datetime.strptime(string, format_string)
format_date = lambda date: date.strftime(format_string)

def get_dir(root,new):
    new_dir = join(root,str(new))
    if not os.path.isdir(new_dir): os.mkdir(new_dir)
    return new_dir

def make_assets_folder(title,date):
    date = parse_date(date)
    reduce(get_dir, [blog_assets_dir, date.year, date.month, title])

def capitalize_title_word(word):
    if len(word) > 5 or word not in en_stopwords:
        return word.capitalize()
    return word

def make_post(
    title, display_title=None,date=None, categories=[], tags=[],
    is_draft = True, has_assets = True):

    # Setting up vars
    output_dir = drafts_dir if is_draft else posts_dir
    date = format_date(datetime.now()) if date is None else date
    title = title.lower().strip()
    if display_title is None: display_title = title
    display_title = ' '.join( [capitalize_title_word(word) for word in display_title.split(' ')] )
    title = title.replace(' ','-')

    if has_assets: make_assets_folder(title,date)
    with open(join(output_dir, "%s-%s.md" % (date,title) ), 'x') as f:
        f.write('---\n')
        f.write('title: {}\n'.format(display_title))
        f.write('categories: [ %s ]\n' % ' ,'.join(categories) )
        f.write('tags: [ %s ]\n' % ' ,'.join(tags) )
        f.write('---\n\n')
