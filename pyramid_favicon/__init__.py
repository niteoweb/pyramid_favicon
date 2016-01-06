# __init__.py
from favicon import favicon

def includeme(config):	
    config.add_route('favicon', '/favicon.ico')
    config.add_route('home', '/')
