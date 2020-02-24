"""learning_logs URL Configuration"""

from django.urls import path, re_path

from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_enrty/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]