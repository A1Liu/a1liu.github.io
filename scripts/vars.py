import os

SCRIPTS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(SCRIPTS_DIR)
COLLECTIONS_DIR = os.path.join(PROJECT_DIR,'src','_collections')
DRAFTS_DIR = os.path.join(COLLECTIONS_DIR,'_drafts')
POSTS_DIR = os.path.join(COLLECTIONS_DIR,'_posts')
ASSETS_DIR  = os.path.join(PROJECT_DIR,'assets')
BLOG_ASSETS_DIR = os.path.join(ASSETS_DIR,'blog')
