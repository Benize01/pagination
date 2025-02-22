from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:day>/<int:month>/<int:year>/<slug:post>/', 
         views.post_detail, 
         name='post_detail'),
]


