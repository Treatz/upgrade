"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns

import story

# eventual custom patterns

patterns = [
    url(r'^chargen/', include('web.chargen.urls')),
]
custom_patterns = [
    url(r'^character/', include('web.character.urls', namespace='character', app_name='character')),
    url(r'story', story.storypage, name='Story'),
    url(r'^ff/', include('web.ff.urls', namespace='ff', app_name='ff')),
    ]

# this is required by Django.
urlpatterns = patterns + custom_patterns + urlpatterns
