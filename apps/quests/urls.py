from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^open/(?P<task_id>\d+)/$', views.open_task_by_id),
                       url(r'^open/(?P<task_name>[A-Za-z0-9_-]+)/$', views.open_task_by_name),

                       url(r'^answer/(?P<task_id>\d+)/$', views.answer_task_by_id),
                       url(r'^answer/(?P<task_name>[A-Za-z0-9_-]+)/$', views.answer_task_by_name),

                       url(r'^check/(?P<answer_id>\d+)/$', views.check_answer),

                       url(r'^open/(?P<task_id>\d+)/static/(?P<path>.*)$', views.get_static),
                       url(r'^open/(?P<task_name>[A-Za-z0-9_-]+)/static/(?P<path>.*)$', views.get_static),

    )
