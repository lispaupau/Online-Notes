from django.urls import path
from .import views

app_name = 'learning_logs'
urlpatterns = [
    #home site
    path('', views.index, name='index'),
    #spisok tem
    path('topics/', views.topics, name='topics'),
    #stranica s podrobnoi infoi
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #for new theme
    path('nrw_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #dlya redactirovania
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]