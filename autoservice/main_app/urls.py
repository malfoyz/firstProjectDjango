from django.urls import path

from . import views

app_name = 'autoservice'
urlpatterns = [
    path('', views.index, name='index'),
    path('section/<int:section_id>/', views.section, name='section')
]